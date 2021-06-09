import time

class Sequenties():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


    def wave(self):
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
        leftRightArm = str(payload.get("leftRightArm"))
        ShoulderPitch = payload.get("ShoulderPitch")
        ShoulderRoll = payload.get("ShoulderRoll")
        ElbowYaw = payload.get("ElbowYaw")
        ElbowRoll = payload.get("ElbowRoll")
        WristYaw = payload.get("WristYaw")
        Hand = payload.get("Hand")
        times = payload.get("times")
        self.pepperArm.turnArmInterpolations(leftRightArm, ShoulderPitch, ShoulderRoll, ElbowYaw, ElbowRoll, WristYaw, Hand, times)
        
        self.ttsProxy.post.say("hi there")
        time.sleep(times[-1])       # wacht tot het zwaaien voorbij is
        self.postureProxy.post.goToPosture("Stand", 0.2)

    
    def usianBolt(self):
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
        leftRightArm = str(payload.get("leftRightArm"))
        ShoulderPitch = payload.get("ShoulderPitch")
        ShoulderRoll = payload.get("ShoulderRoll")
        ElbowYaw = payload.get("ElbowYaw")
        ElbowRoll = payload.get("ElbowRoll")
        WristYaw = payload.get("WristYaw")
        Hand = payload.get("Hand")
        speed = payload.get("speed")
        self.pepperArm.turnArmManually(leftRightArm, ShoulderPitch, ShoulderRoll, ElbowYaw, ElbowRoll, WristYaw, Hand, speed)

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
        leftRightArm = str(payload.get("leftRightArm"))
        ShoulderPitch = payload.get("ShoulderPitch")
        ShoulderRoll = payload.get("ShoulderRoll")
        ElbowYaw = payload.get("ElbowYaw")
        ElbowRoll = payload.get("ElbowRoll")
        WristYaw = payload.get("WristYaw")
        Hand = payload.get("Hand")
        speed = payload.get("speed")
        self.pepperArm.turnArmManually(leftRightArm, ShoulderPitch, ShoulderRoll, ElbowYaw, ElbowRoll, WristYaw, Hand, speed)

        payload = {
            "angleYaw": 40,
            "anglePitch": -20,
            "speed": 0.1
        }
        angleYaw = payload.get("angleYaw")
        anglePitch = payload.get("anglePitch")
        speed = payload.get("speed")
        self.pepperHead.turnHeadManually(angleYaw, anglePitch, speed)

        payload = {
            "hipPitch": 10,
            "hipRoll": -15,
            "speed": 0.1
        }
        hipPitch = payload.get("hipPitch")
        hipRoll = payload.get("hipRoll")
        speed = payload.get("speed")
        self.pepperBody.turnHipManually(hipRoll, hipPitch, speed)

        time.sleep(4)
        self.ttsProxy.post.say("yea")
        time.sleep(1)
        self.postureProxy.post.goToPosture("Stand", 0.2)

    
    def dab(self):
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
        leftRightArm = str(payload.get("leftRightArm"))
        ShoulderPitch = payload.get("ShoulderPitch")
        ShoulderRoll = payload.get("ShoulderRoll")
        ElbowYaw = payload.get("ElbowYaw")
        ElbowRoll = payload.get("ElbowRoll")
        WristYaw = payload.get("WristYaw")
        Hand = payload.get("Hand")
        speed = payload.get("speed")
        self.pepperArm.turnArmManually(leftRightArm, ShoulderPitch, ShoulderRoll, ElbowYaw, ElbowRoll, WristYaw, Hand, speed)

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
        leftRightArm = str(payload.get("leftRightArm"))
        ShoulderPitch = payload.get("ShoulderPitch")
        ShoulderRoll = payload.get("ShoulderRoll")
        ElbowYaw = payload.get("ElbowYaw")
        ElbowRoll = payload.get("ElbowRoll")
        WristYaw = payload.get("WristYaw")
        Hand = payload.get("Hand")
        speed = payload.get("speed")
        self.pepperArm.turnArmManually(leftRightArm, ShoulderPitch, ShoulderRoll, ElbowYaw, ElbowRoll, WristYaw, Hand, speed)

        payload = {
            "angleYaw": -40,
            "anglePitch": 30,
            "speed": 0.3
        }
        angleYaw = payload.get("angleYaw")
        anglePitch = payload.get("anglePitch")
        speed = payload.get("speed")
        self.pepperHead.turnHeadManually(angleYaw, anglePitch, speed)

        payload = {
            "hipPitch": -30,
            "hipRoll": -10,
            "speed": 0.5
        }
        hipPitch = payload.get("hipPitch")
        hipRoll = payload.get("hipRoll")
        speed = payload.get("speed")
        self.pepperBody.turnHipManually(hipRoll, hipPitch, speed)

        self.ttsProxy.post.say("yea")
        time.sleep(5)
        self.postureProxy.post.goToPosture("Stand", 0.2)


    def box(self):
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
        leftRightArm = str(payload.get("leftRightArm"))
        ShoulderPitch = payload.get("ShoulderPitch")
        ShoulderRoll = payload.get("ShoulderRoll")
        ElbowYaw = payload.get("ElbowYaw")
        ElbowRoll = payload.get("ElbowRoll")
        WristYaw = payload.get("WristYaw")
        Hand = payload.get("Hand")
        speed = payload.get("speed")
        self.pepperArm.turnArmManually(leftRightArm, ShoulderPitch, ShoulderRoll, ElbowYaw, ElbowRoll, WristYaw, Hand, speed)
        time.sleep(3)
        self.ttsProxy.post.say("boom")
        time.sleep(2)
        self.postureProxy.post.goToPosture("Stand", 0.2)


    def highFive(self):
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
        leftRightArm = str(payload.get("leftRightArm"))
        ShoulderPitch = payload.get("ShoulderPitch")
        ShoulderRoll = payload.get("ShoulderRoll")
        ElbowYaw = payload.get("ElbowYaw")
        ElbowRoll = payload.get("ElbowRoll")
        WristYaw = payload.get("WristYaw")
        Hand = payload.get("Hand")
        speed = payload.get("speed")
        self.pepperArm.turnArmManually(leftRightArm, ShoulderPitch, ShoulderRoll, ElbowYaw, ElbowRoll, WristYaw, Hand, speed)
        time.sleep(3)
        self.ttsProxy.post.say("high five")
        time.sleep(2)
        self.postureProxy.post.goToPosture("Stand", 0.2)


    def hug(self):
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
        leftRightArm = str(payload.get("leftRightArm"))
        ShoulderPitch = payload.get("ShoulderPitch")
        ShoulderRoll = payload.get("ShoulderRoll")
        ElbowYaw = payload.get("ElbowYaw")
        ElbowRoll = payload.get("ElbowRoll")
        WristYaw = payload.get("WristYaw")
        Hand = payload.get("Hand")
        speed = payload.get("speed")
        self.pepperArm.turnArmManually(leftRightArm, ShoulderPitch, ShoulderRoll, ElbowYaw, ElbowRoll, WristYaw, Hand, speed)
        
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
        leftRightArm = str(payload.get("leftRightArm"))
        ShoulderPitch = payload.get("ShoulderPitch")
        ShoulderRoll = payload.get("ShoulderRoll")
        ElbowYaw = payload.get("ElbowYaw")
        ElbowRoll = payload.get("ElbowRoll")
        WristYaw = payload.get("WristYaw")
        Hand = payload.get("Hand")
        speed = payload.get("speed")
        self.pepperArm.turnArmManually(leftRightArm, ShoulderPitch, ShoulderRoll, ElbowYaw, ElbowRoll, WristYaw, Hand, speed)
        self.ttsProxy.post.say("come here baby")
        time.sleep(5)
        self.postureProxy.post.goToPosture("Stand", 0.2)