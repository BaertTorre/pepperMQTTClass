import time
import json
from datetime import datetime

class Sequenties():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def choseSequence(self, chosenSequentie):
        if chosenSequentie == "wave":
            self.wave()
            
        elif chosenSequentie == "usainBolt":
            self.usainBolt()

        elif chosenSequentie == "dab":
            self.dab()

        elif chosenSequentie == "box":
            self.box()

        elif chosenSequentie == "highFive":
            self.highFive()

        elif chosenSequentie == "hug":
            self.hug()

        else:
            print("De opgegeven sequentie bestaat niet")


    def wave(self):
        payloadJson = json.dumps({'startedAt': str(datetime.now()), 'sequence': 'wave'})
        self.client.publish("robot/pepper/log/sequentieStart", payload=payloadJson, qos=2, retain=False)

        payload = {
            "leftRightArm": "R",
            "ShoulderPitch": [-60, -60, -60, -60, -60, -60, -60],
            "ShoulderRoll": [-60, -60, -60, -60, -60, -60, -60],
            "ElbowYaw": [20, 20, 20, 20, 20, 20, 20],
            "ElbowRoll": [80, 40, 80, 40, 80, 40, 80],
            "WristYaw": [0, 0, 0, 0, 0, 0, 0],
            "Hand": [60, 60, 60, 60, 60, 60, 60],
            "times": [1, 2, 3, 4, 5, 6, 7]
        }
        self.pepperArm.turnArmInterpolations(payload)
        
        self.ttsProxy.post.say("hi there")
        time.sleep(7)       # wacht tot het zwaaien voorbij is

        payloadJson = json.dumps({'finishedAt': str(datetime.now()), 'sequence': 'wave'})
        self.client.publish("robot/pepper/log/sequentieStop", payload=payloadJson, qos=2, retain=False)
        self.postureProxy.post.goToPosture("Stand", 0.2)

    
    def usainBolt(self):
        payloadJson = json.dumps({'startedAt': str(datetime.now()), 'sequence': 'usainBolt'})
        self.client.publish("robot/pepper/log/sequentieStart", payload=payloadJson, qos=2, retain=False)

        payload = {
            "leftRightArm": "R",
            "ShoulderPitch": -40,
            "ShoulderRoll": -30,
            "ElbowYaw": 20,
            "ElbowRoll": 90,
            "WristYaw": 50,
            "Hand": 50,
            "speed": 0.1
        }
        self.pepperArm.turnArmManually(payload)

        payload = {
            "leftRightArm": "L",
            "ShoulderPitch": -50,
            "ShoulderRoll": 40,
            "ElbowYaw": 0,
            "ElbowRoll": 0,
            "WristYaw": 0,
            "Hand": 50,
            "speed": 0.1
        }
        self.pepperArm.turnArmManually(payload)

        payload = {
            "angleYaw": 40,
            "anglePitch": -20,
            "speed": 0.1
        }
        self.pepperHead.turnHeadManually(payload)

        payload = {
            "hipPitch": 10,
            "hipRoll": -15,
            "speed": 0.1
        }
        self.pepperBody.turnHipManually(payload)

        time.sleep(5)

        payloadJson = json.dumps({'finishedAt': str(datetime.now()), 'sequence': 'usainBolt'})
        self.client.publish("robot/pepper/log/sequentieStop", payload=payloadJson, qos=2, retain=False)
        self.postureProxy.post.goToPosture("Stand", 0.2)

    
    def dab(self):
        payloadJson = json.dumps({'startedAt': str(datetime.now()), 'sequence': 'dab'})
        self.client.publish("robot/pepper/log/sequentieStart", payload=payloadJson, qos=2, retain=False)

        payload = {
            "leftRightArm": "R",
            "ShoulderPitch": -40,
            "ShoulderRoll": -20,
            "ElbowYaw": 0,
            "ElbowRoll": 70,
            "WristYaw": 40,
            "Hand": 50,
            "speed": 1
        }
        self.pepperArm.turnArmManually(payload)

        payload = {
            "leftRightArm": "L",
            "ShoulderPitch": -50,
            "ShoulderRoll": 40,
            "ElbowYaw": 0,
            "ElbowRoll": 0,
            "WristYaw": 0,
            "Hand": 50,
            "speed": 1
        }
        self.pepperArm.turnArmManually(payload)

        payload = {
            "angleYaw": -40,
            "anglePitch": 30,
            "speed": 0.3
        }
        self.pepperHead.turnHeadManually(payload)

        payload = {
            "hipPitch": -30,
            "hipRoll": -10,
            "speed": 0.5
        }
        self.pepperBody.turnHipManually(payload)

        self.ttsProxy.post.say("yea")
        time.sleep(5)

        payloadJson = json.dumps({'finishedAt': str(datetime.now()), 'sequence': 'dab'})
        self.client.publish("robot/pepper/log/sequentieStop", payload=payloadJson, qos=2, retain=False)
        self.postureProxy.post.goToPosture("Stand", 0.2)


    def box(self):
        payloadJson = json.dumps({'startedAt': str(datetime.now()), 'sequence': 'fist'})
        self.client.publish("robot/pepper/log/sequentieStart", payload=payloadJson, qos=2, retain=False)

        payload = {
            "leftRightArm": "R",
            "ShoulderPitch": 0,
            "ShoulderRoll": 0,
            "ElbowYaw": 0,
            "ElbowRoll": 0,
            "WristYaw": 0,
            "Hand": 0,
            "speed": 0.3
        }
        self.pepperArm.turnArmManually(payload)
        time.sleep(1)
        self.ttsProxy.post.say("boom")
        time.sleep(4)

        payloadJson = json.dumps({'finishedAt': str(datetime.now()), 'sequence': 'fist'})
        self.client.publish("robot/pepper/log/sequentieStop", payload=payloadJson, qos=2, retain=False)
        self.postureProxy.post.goToPosture("Stand", 0.2)


    def highFive(self):
        payloadJson = json.dumps({'startedAt': str(datetime.now()), 'sequence': 'highfive'})
        self.client.publish("robot/pepper/log/sequentieStart", payload=payloadJson, qos=2, retain=False)

        payload = {
            "leftRightArm": "R",
            "ShoulderPitch": -40,
            "ShoulderRoll": -60,
            "ElbowYaw": 20,
            "ElbowRoll": 50,
            "WristYaw": 0,
            "Hand": 50,
            "speed": 0.3
        }
        self.pepperArm.turnArmManually(payload)
        time.sleep(1)
        self.ttsProxy.post.say("high five")
        time.sleep(4)

        payloadJson = json.dumps({'finishedAt': str(datetime.now()), 'sequence': 'highfive'})
        self.client.publish("robot/pepper/log/sequentieStop", payload=payloadJson, qos=2, retain=False)
        self.postureProxy.post.goToPosture("Stand", 0.2)


    def hug(self):
        payloadJson = json.dumps({'startedAt': str(datetime.now()), 'sequence': 'hug'})    
        self.client.publish("robot/pepper/log/sequentieStart", payload=payloadJson, qos=2, retain=False)

        payload = {
            "leftRightArm": "R",
            "ShoulderPitch": -10,
            "ShoulderRoll": -30,
            "ElbowYaw": 10,
            "ElbowRoll": 50,
            "WristYaw": 70,
            "Hand": 50,
            "speed": 0.1
        }
        self.pepperArm.turnArmManually(payload)
        
        payload = {
            "leftRightArm": "L",
            "ShoulderPitch": -10,
            "ShoulderRoll": 30,
            "ElbowYaw": -10,
            "ElbowRoll": -50,
            "WristYaw": -70,
            "Hand": 50,
            "speed": 0.1
        }
        self.pepperArm.turnArmManually(payload)
        self.ttsProxy.post.say("come here baby")
        time.sleep(5)

        payloadJson = json.dumps({'finishedAt': str(datetime.now()), 'sequence': 'hug'})
        self.client.publish("robot/pepper/log/sequentieStop", payload=payloadJson, qos=2, retain=False)
        self.postureProxy.post.goToPosture("Stand", 0.2)