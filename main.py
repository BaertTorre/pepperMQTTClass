import paho.mqtt.client as mqttClient
import time
from naoqi import *
from Models.PepperHead import PepperHead
from Models.PepperArm import PepperArm
from Models.PepperBody import PepperBody
from Models.PepperWalk import PepperWalk
from Models.Diagnosis import Diagnosis
from Models.PepperBehaviors import PepperBehaviors
from Models.TrackFace import TrackFace
from Models.Sequenties import Sequenties
import json
import sys
import os

facesDetectedBool = False

class Main():
    def __init__(self, MQTTbrokerIp, **kwargs):
        self.__dict__.update(**kwargs)
        
        # --------------------------------------------------------------- start program ------------------------------
        self.start_MQTT(MQTTbrokerIp, 1883)

        # alle classes starten
        self.pepperHead = PepperHead(**kwargs)
        self.pepperBody = PepperBody(**kwargs)
        self.pepperArm = PepperArm(**kwargs)
        self.pepperWalk = PepperWalk(**kwargs)
        self.diagnosis = Diagnosis(**kwargs)
        self.pepperBehaviors = PepperBehaviors(**kwargs)
        self.trackFace = TrackFace(**kwargs)
        self.sequenties = Sequenties(pepperHead = self.pepperHead, pepperBody = self.pepperBody, pepperArm = self.pepperArm, **kwargs)

        self.payloadFaceDetected = None

        # wakes pepper up and set stiffness on
        self.motionProxy.wakeUp()
        self.postureProxy.goToPosture("Stand", 0.2)


    # --------------------------------------------------------------- MQTT -----------------------------------------------------------------    
    def start_MQTT(self, MQTTbrokerIp, MQTTbrokerPort):
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
            self.client.subscribe("pepper/sub/#", 2)
            self.client.subscribe("pepper/logs", 2)
        else:
            print("Connection failed")


    # -------------------------------- new message ---------------------------------
    def on_message(self, client, userdata, msg):
        try:
            if msg.payload:
                payload = json.loads(msg.payload)
            else:
                payload = None
        except Exception, er:
            print("AN ERROR HAS OCCURED IN THE JSON FUNCTION -----------> " + er)

        
        try:
            if msg.topic == 'pepper/logs':
                logs = self.diagnosis.getLogs()
                self.client.publish("robot/pepper/logs", payload=logs, qos=2, retain=False)

            else:
                print(msg.topic + " " + str(msg.qos) + " " + str(payload))
                topic = msg.topic.split("/")
                action = topic[2]

                # -------------------- actions -------------------
                if action == "speak":               # lees de payload voor
                    if payload.get("speak"):
                        self.ttsProxy.post.say(str(payload.get("speak")))
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
                    if payload.get("speak") and payload.get("sequence"):
                        self.payloadFaceDetected = payload          # payload opslaan zodat hij dat later in de callback class kan gebruiken
                        self.memoryProxy.subscribeToEvent("FaceDetected", "pythonCallback", "faceIsDetected")            
                    else:
                        print("Geen speak of sequence payload")


                elif action == "detectFaceStop":
                    self.memoryProxy.unsubscribeToEvent("FaceDetected", "pythonCallback")
                    self.postureProxy.goToPosture("Stand", 0.2)


                elif action == "startFollowMode":
                    if payload.get("trackerMode"):          # 3 follow modes: Head, WholeBody, Move
                        self.trackFace.startTrackingFace(str(payload.get("trackerMode")), str(payload.get("targetName")))
                    else:                                   # targetName: Face of RedBall
                        print("Geen trackerMode payload")


                elif action == "stopFollowMode":
                    self.trackFace.stopTrackingFace()
                    self.postureProxy.goToPosture("Stand", 0.2)


                elif action == "getBehaviors":
                    self.pepperBehaviors.getBehaviors()


                elif action == "launchBehavior":
                    if payload.get("behaviorName"):
                        print("starting behavior")
                        self.pepperBehaviors.launchBehavior(
                            str(payload.get("behaviorName")))
                    else:
                        print("Geen behaviorName payload")


                elif action == "stopBehavior":
                    if payload.get("behaviorName"):
                        print("Stopping behavior")
                        self.pepperBehaviors.stopBehavior(str(payload.get("behaviorName")))
                    else:
                        print("Geen behaviorName payload")


                elif action == "moveTo":            # ga naar een locatie, ZONDER object avoidance
                    self.pepperWalk.moveTo(payload)


                elif action == "navigateTo":            # ga naar een locatie, MET object avoidance
                    self.pepperWalk.navigateTo(payload)
                    

                elif action == "defaultStand":            # ga naar zijn default stand
                    self.postureProxy.post.goToPosture("Stand", 0.2)


                elif action == "moveHeadManually":      # de head joints aansturen
                    self.pepperHead.turnHeadManually(payload)


                elif action == "turnHeadInterpolations":      # de head joints aansturen
                    self.pepperHead.turnHeadInterpolations(payload)


                elif action == "moveHipManually":       # de heup joints aansturen
                    self.pepperBody.turnHipManually(payload)


                elif action == "moveHipInterpolations":       # de heup joints aansturen
                    self.pepperBody.turnHipInterpolations(payload)


                elif action == "moveKneeManually":      # de knie joint aansturen
                    self.pepperBody.turnKneeManually(payload)


                elif action == "moveKneeInterpolations":      # de knie joint aansturen
                    self.pepperBody.turnKneeInterpolations(payload)


                elif action == "moveArmManually":       # de arm & pols joints aansturen
                    self.pepperArm.turnArmManually(payload)


                elif action == "turnArmInterpolations":       # de arm & pols joints aansturen
                    self.pepperArm.turnArmInterpolations(payload)


                elif action == "diagnosis":         # stuurt de robot diagnostics door via de /pepper/pub/diagnosis topic
                    self.diagnosis.getDiagnosis()

                
                elif action == "sequentie":
                    chosenSequence = topic[3]
                    self.sequenties.choseSequence(chosenSequence)

                
                else:
                    print("Topic bestaat niet")

        except Exception, e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("AN ERROR HAS OCCURED WHILE TRYING TO HANDLE THE MQTT MESSAGE -----------> ")
            print(e, fname, exc_tb.tb_lineno)
    


# --------------------------------------------------------------- CALLBACK CLASS -----------------------------------------------
class PythonCallback(ALModule):
    def temperatureChanged(self, strVarName, value):
        print ("TemperatureChanged, value ---> ", str(value))
        main.client.publish("robot/pepper/logs/temperature", payload=str(value), qos=2, retain=False)
        

    def faceIsDetected(self, *_args):
        global facesDetectedBool
        if facesDetectedBool == False:
            facesDetectedBool = True      # switch de var van False naar True of omgekeerd
        else:
            facesDetectedBool = False

        print("Face detected, facesDetectedBool: ", facesDetectedBool)
        if facesDetectedBool == True:              # pepper herkent een gezicht altijd 2 keer, we willen de message maar 1 keer
            # Unsubscribe to the event when talking,
            # to avoid repetitions
            main.memoryProxy.unsubscribeToEvent("FaceDetected", "pythonCallback")

            say = str(main.payloadFaceDetected.get("speak"))
            main.ttsProxy.post.say(say)

            chosenSequence = main.payloadFaceDetected.get("sequence")
            main.sequenties.choseSequence(chosenSequence)

            main.postureProxy.goToPosture("Stand", 0.2)
            # Subscribe again to the event
            main.memoryProxy.subscribeToEvent("FaceDetected", "pythonCallback", "faceIsDetected")



if __name__ == "__main__":
    # ------------------------------------------------------------------------- NAOqi -------------------------------------------------------------
    # Proxys maken van de naoqi api
    brokerProxy = ALBroker("pythonBroker", "0.0.0.0", 0, "127.0.0.1", 9559)
    # ip en poort moeten niet meer gebruikt worden omdat we ALBroker gebruiken
    motionProxy = ALProxy("ALMotion")
    ttsProxy = ALProxy("ALTextToSpeech")
    postureProxy = ALProxy("ALRobotPosture")
    diagnosisProxy = ALProxy("ALDiagnosis")
    navigationProxy = ALProxy("ALNavigation")
    behaviorProxy = ALProxy("ALBehaviorManager")
    memoryProxy = ALProxy("ALMemory")
    batteryProxy = ALProxy("ALBattery")
    bodyTemperatureProxy = ALProxy("ALBodyTemperature")
    trackerProxy = ALProxy("ALTracker")

    client = mqttClient.Client()  # create new instance

    # Callbacks aanmaken, kan niet in een class
    pythonCallback = PythonCallback("pythonCallback")

    main = Main("13.81.105.139", client = client, motionProxy = motionProxy, ttsProxy = ttsProxy, postureProxy = postureProxy, diagnosisProxy = diagnosisProxy, navigationProxy = navigationProxy, behaviorProxy = behaviorProxy, memoryProxy = memoryProxy, batteryProxy = batteryProxy, bodyTemperatureProxy = bodyTemperatureProxy, trackerProxy = trackerProxy)

    memoryProxy.subscribeToEvent("TemperatureStatusChanged", "pythonCallback", "temperatureChanged") 

    try:
        while True:
            time.sleep(0.1)

    
    except KeyboardInterrupt:
        print("keyboardInterrupt")

    except Exception, er:
        print("ERROR -----> ", er)

    finally:
        print("Shutting down")
        main.postureProxy.goToPosture("Stand", 0.2)
        main.trackFace.stopTrackingFace()
        main.client.disconnect()
        main.client.loop_stop()
        brokerProxy.shutdown()
        # sets pepper to rest position with stiffness off
        # main.motionProxy.rest()
