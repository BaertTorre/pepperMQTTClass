import paho.mqtt.client as mqttClient
import time
from naoqi import *
from Models.PepperHead import PepperHead
from Models.PepperArm import PepperArm
from Models.PepperBody import PepperBody
from Models.PepperWalk import PepperWalk
from Models.PepperDiagnosis import Diagnosis
from Models.PepperBehaviors import PepperBehaviors
from Models.TrackFace import TrackFace
import json

sayWhenFaceDetected = None
pythonCallback = None

class Main():
    def __init__(self, MQTTbrokerIp, MQTTbrokerPort=1883):
        # ------------------------------------------------------------------------- NAOqi -------------------------------------------------------------
        # Proxys maken van de naoqi api
        self.brokerProxy = ALBroker("pythonBroker", "0.0.0.0", 0, "pepper.local", 9559)
        # ip en poort moeten niet meer gebruikt worden omdat we ALBroker gebruiken
        self.motionProxy = ALProxy("ALMotion")
        self.ttsProxy = ALProxy("ALTextToSpeech")
        self.postureProxy = ALProxy("ALRobotPosture")
        self.diagnosisProxy = ALProxy("ALDiagnosis")
        self.navigationProxy = ALProxy("ALNavigation")
        self.BehaviorProxy = ALProxy("ALBehaviorManager")
        self.memoryProxy = ALProxy("ALMemory")
        self.batteryProxy = ALProxy("ALBattery")
        self.bodyTemperatureProxy = ALProxy("ALBodyTemperature")
        self.trackerProxy = ALProxy("ALTracker")
        

        # --------------------------------------------------------------- start program ------------------------------
        # objecten maken van alle pepper klasses
        self.pepperHead = PepperHead(self.motionProxy)
        self.pepperBody = PepperBody(self.motionProxy)
        self.pepperArm = PepperArm(self.motionProxy)
        self.pepperWalk = PepperWalk(self.motionProxy, self.navigationProxy)
        self.diagnosis = Diagnosis(self.diagnosisProxy, self.bodyTemperatureProxy, self.batteryProxy, self.client)
        self.pepperBehaviors = PepperBehaviors(self.BehaviorProxy)
        self.trackFace = TrackFace(self.motionProxy, self.trackerProxy)
        self.payloadFaceDetected = None

        # wakes pepper up and set stiffness on
        self.motionProxy.wakeUp()
        self.postureProxy.goToPosture("Stand", 0.2)
        self.start_MQTT(MQTTbrokerIp, MQTTbrokerPort)


    # --------------------------------------------------------------- MQTT -----------------------------------------------------------------    
    def start_MQTT(self, MQTTbrokerIp, MQTTbrokerPort):
        self.client = mqttClient.Client()  # create new instance
        self.client.on_connect = self.on_connect  # attach function to callback
        self.client.on_message = self.on_message
        # connect to broker
        self.client.connect(MQTTbrokerIp, port=MQTTbrokerPort)
        # mqtt start
        print("Python is running and trying to connect to the MQTT broker")
        self.client.loop_start()  # start the loop


    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker")
            # subscribe to the pepper topic
            self.client.subscribe("/pepper/sub/#", 2)
        else:
            print("Connection failed")


    # -------------------------------- new message ---------------------------------
    def on_message(self, client, userdata, msg):
        try:
            payload = json.loads(msg.payload)
        except Exception, er:
            print("AN ERROR HAS OCCURED IN THE JSON FUNCTION -----------> " + er)

        print(msg.topic + " " + str(msg.qos) + " " + str(payload))
        topic = msg.topic.split("/")
        action = topic[3]

        # -------------------- actions -------------------
        if action == "speak":               # lees de payload voor
            if payload.get("speak"):
                self.ttsProxy.say(str(payload.get("speak")))
            else:
                print("Geen speak payload")


        elif action == "getBattery":
            self.diagnosis.getBattery()


        elif action == "rest":
            self.motionProxy.rest()


        elif action == "wakeUp":
            self.motionProxy.wakeUp()


        elif action == "getTemperature":
            self.diagnosis.getTemperature()     # stuurt de temperatuur door naar de /pepper/pub/temperature topic


        elif action == "detectFaceStart":
            if payload.get("speak") and payload.get("times"):
                self.payloadFaceDetected = payload          # payload opslaan zodat hij dat later in de callback class kan gebruiken
                pythonCallback.subscribeToFace()            # subscibes met callbacks werken alleen in de PythenCallback class
            else:
                print("Geen speak of times payload")


        elif action == "detectFaceStop":
            pythonCallback.unsubscribeToFace()


        elif action == "startFollowMode":
            if payload.get("trackerMode"):          # 3 follow modes: Head, WholeBody, Move
                self.trackFace.startTrackingFace(str(payload.get("trackerMode")), str(payload.get("targetName")))
            else:                                   # targetName: Face of RedBall
                print("Geen trackerMode payload")


        elif action == "stopFollowMode":
            self.trackFace.stopTrackingFace()


        elif action == "getBehaviors":
            self.pepperBehaviors.getBehaviors()


        elif action == "launchBehavior":
            if payload.get("behaviorName"):
                self.pepperBehaviors.launchBehavior(
                    str(payload.get("behaviorName")))
            else:
                print("Geen behaviorName payload")


        elif action == "stopBehavior":
            if payload.get("behaviorName"):
                self.pepperBehaviors.stopBehavior(
                    str(payload.get("behaviorName")))
            else:
                print("Geen behaviorName payload")


        elif action == "moveTo":            # ga naar een locatie, ZONDER object avoidance
            xValue = payload.get("xValue")
            yValue = payload.get("yValue")
            thetaValue = payload.get("thetaValue")
            print(thetaValue)
            if xValue != None and yValue != None and thetaValue != None:
                self.pepperWalk.moveTo(xValue, yValue, thetaValue)
            else:
                print("Geen xValue, yValue en thetaValue payloads")


        elif action == "navigateTo":            # ga naar een locatie, MET object avoidance
            xValue = payload.get("xValue")
            yValue = payload.get("yValue")
            if xValue != None and yValue != None:
                self.pepperWalk.navigateTo(xValue, yValue)
            else:
                print("Geen xValue en yValue payloads")

        elif action == "defaultStand":            # ga naar zijn default stand
            self.postureProxy.goToPosture("Stand", 0.2)


        elif action == "moveHeadManually":      # de head joints aansturen
            angleYaw = payload.get("angleYaw")
            anglePitch = payload.get("anglePitch")
            speed = payload.get("speed")
            if speed and (angleYaw != None or anglePitch != None):
                self.pepperHead.turnHeadManually(angleYaw, anglePitch, speed)
            else:
                print("Geen speed en angleYaw of anglePitch payload")


        elif action == "turnHeadInterpolations":      # de head joints aansturen
            angleYaw = payload.get("angleYaw")
            anglePitch = payload.get("anglePitch")
            times = payload.get("times")
            if times and (angleYaw != None or anglePitch != None):
                self.pepperHead.turnHeadInterpolations(
                    angleYaw, anglePitch, times)
            else:
                print("Geen times en angleYaw of anglePitch payload")


        elif action == "moveHipManually":       # de heup joints aansturen
            hipPitch = payload.get("hipPitch")
            hipRoll = payload.get("hipRoll")
            speed = payload.get("speed")
            if speed and (hipPitch != None or hipRoll != None):
                self.pepperBody.turnHipManually(hipRoll, hipPitch, speed)
            else:
                print("Geen speed en hipPitch of hipRoll payload")


        elif action == "moveHipInterpolations":       # de heup joints aansturen
            hipPitch = payload.get("hipPitch")
            hipRoll = payload.get("hipRoll")
            times = payload.get("times")
            if times and (hipPitch != None or hipRoll != None):
                self.pepperBody.turnHipInterpolations(hipRoll, hipPitch, times)
            else:
                print("Geen times en hipPitch of hipRoll payload")


        elif action == "moveKneeManually":      # de knie joint aansturen
            kneePitch = payload.get("kneePitch")
            speed = payload.get("speed")
            if speed and (kneePitch != None):
                self.pepperBody.turnKneeManually(kneePitch, speed)
            else:
                print("Geen speed en kneePitch payload")


        elif action == "moveKneeInterpolations":      # de knie joint aansturen
            kneePitch = payload.get("kneePitch")
            times = payload.get("times")
            if times and (kneePitch != None):
                self.pepperBody.turnKneeInterpolations(kneePitch, times)
            else:
                print("Geen times en kneePitch payload")


        elif action == "moveArmManually":       # de arm & pols joints aansturen
            leftRightArm = str(payload.get("leftRightArm"))
            ShoulderPitch = payload.get("ShoulderPitch")
            ShoulderRoll = payload.get("ShoulderRoll")
            ElbowYaw = payload.get("ElbowYaw")
            ElbowRoll = payload.get("ElbowRoll")
            WristYaw = payload.get("WristYaw")
            Hand = payload.get("Hand")
            speed = payload.get("speed")
            if speed and (leftRightArm != None or ShoulderPitch != None or ShoulderRoll != None or ElbowYaw != None or ElbowRoll != None or WristYaw != None or Hand != None):
                self.pepperArm.turnArmManually(
                    leftRightArm, ShoulderPitch, ShoulderRoll, ElbowYaw, ElbowRoll, WristYaw, Hand, speed)
            else:
                print("Geen speed en ledematen payload")


        elif action == "turnArmInterpolations":       # de arm & pols joints aansturen
            leftRightArm = str(payload.get("leftRightArm"))
            ShoulderPitch = payload.get("ShoulderPitch")
            ShoulderRoll = payload.get("ShoulderRoll")
            ElbowYaw = payload.get("ElbowYaw")
            ElbowRoll = payload.get("ElbowRoll")
            WristYaw = payload.get("WristYaw")
            Hand = payload.get("Hand")
            times = payload.get("times")
            if times and (leftRightArm != None or ShoulderPitch != None or ShoulderRoll != None or ElbowYaw != None or ElbowRoll != None or WristYaw != None or Hand != None):
                self.pepperArm.turnArmInterpolations(
                    leftRightArm, ShoulderPitch, ShoulderRoll, ElbowYaw, ElbowRoll, WristYaw, Hand, times)
            else:
                print("Geen times en ledematen payload")


        elif action == "diagnosis":         # stuurt de robot diagnostics door via de /pepper/pub/diagnosis topic
            self.diagnosis.getDiagnosis()

        
        else:
            print("Topic bestaat niet")

    


# --------------------------------------------------------------- CALLBACK CLASS -----------------------------------------------
class PythonCallback(ALModule):
    def temperatureChanged(self, strVarName, value):
        print "TemperatureChanged, value ---> ", value
        

    def deviceIsHot(self, strVarName, value):
        print "Hot device detected, value ---> ", value
        

    def faceIsDetected(self, *_args):
        # Unsubscribe to the event when talking,
        # to avoid repetitions
        main.memoryProxy.unsubscribeToEvent("FaceDetected", "pythonCallback")

        say = main.payloadFaceDetected.get("speak")
        leftRightArm = main.payloadFaceDetected.get("leftRightArm")
        ShoulderPitch = main.payloadFaceDetected.get("ShoulderPitch")
        ShoulderRoll = main.payloadFaceDetected.get("ShoulderRoll")
        ElbowYaw = main.payloadFaceDetected.get("ElbowYaw")
        ElbowRoll = main.payloadFaceDetected.get("ElbowRoll")
        WristYaw = main.payloadFaceDetected.get("WristYaw")
        Hand = main.payloadFaceDetected.get("Hand")
        times = main.payloadFaceDetected.get("times")

        main.ttsProxy.say(say)
        self.pepperArm.turnArmInterpolations(leftRightArm, ShoulderPitch, ShoulderRoll, ElbowYaw, ElbowRoll, WristYaw, Hand, times)
        # Subscribe again to the event
        time.sleep(5)
        main.memoryProxy.subscribeToEvent("FaceDetected", "pythonCallback", "faceIsDetected")


    def subscribeToFace(self):
        main.memoryProxy.subscribeToEvent("FaceDetected", "pythonCallback", "faceIsDetected")


    def unsubscribeToFace(self):
        main.memoryProxy.unsubscribeToEvent("FaceDetected", "pythonCallback")



if __name__ == "__main__":
    try:
        main = Main("13.81.105.139")

        # Callbacks aanmaken, kan niet in een class
        pythonCallback = PythonCallback("pythonCallback")

        main.memoryProxy.subscribeToEvent("TemperatureStatusChanged", "pythonCallback", "temperatureChanged") 
        main.memoryProxy.subscribeToEvent("HotDeviceDetected", "pythonCallback", "deviceIsHot") 
        pythonCallback.subscribeToFace()

        while True:
            time.sleep(1)

    
    except KeyboardInterrupt:
        print("keyboardInterrupt")

    finally:
        print("Shutting down")
        main.postureProxy.goToPosture("Stand", 0.2)
        main.trackFace.stopTrackingFace()
        main.client.disconnect()
        main.client.loop_stop()
        main.brokerProxy.shutdown()
        # sets pepper to rest position with stiffness off
        # main.motionProxy.rest()
