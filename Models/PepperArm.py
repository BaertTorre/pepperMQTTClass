import almath


class PepperArm:
    def __init__(self, motionProxyVar):
        self.motionProxy = motionProxyVar

    def turnArmManually(self, leftRightArm, ShoulderPitch, ShoulderRoll, ElbowYaw, ElbowRoll, WristYaw, Hand, speed):
        # Simple command for the ShoulderPitch joint
        if ShoulderPitch != None:
            names = leftRightArm + "ShoulderPitch"
            angles = ShoulderPitch*almath.TO_RAD
            self.motionProxy.post.setAngles(names, angles, speed)

        # Simple command for the ShoulderRoll joint
        if ShoulderRoll != None:
            names = leftRightArm + "ShoulderRoll"
            angles = ShoulderRoll*almath.TO_RAD
            self.motionProxy.post.setAngles(names, angles, speed)

        # Simple command for the LElbowYaw joint
        if ElbowYaw != None:
            names = leftRightArm + "ElbowYaw"
            angles = ElbowYaw*almath.TO_RAD
            self.motionProxy.post.setAngles(names, angles, speed)

        # Simple command for the LElbowRoll joint
        if ElbowRoll != None:
            names = leftRightArm + "ElbowRoll"
            angles = ElbowRoll*almath.TO_RAD
            self.motionProxy.post.setAngles(names, angles, speed)

        # Simple command for the LWristYaw joint
        if WristYaw != None:
            names = leftRightArm + "WristYaw"
            angles = WristYaw*almath.TO_RAD
            self.motionProxy.post.setAngles(names, angles, speed)

        # Simple command for the LHand joint
        if Hand != None:
            names = leftRightArm + "Hand"
            angles = Hand*almath.TO_RAD
            self.motionProxy.post.setAngles(names, angles, speed)


    def turnArmInterpolations(self, leftRightArm, ShoulderPitch, ShoulderRoll, ElbowYaw, ElbowRoll, WristYaw, Hand, times):
        isAbsolute = True
        
        # Simple command for the ShoulderPitch joint
        if ShoulderPitch != None:
            names = leftRightArm + "ShoulderPitch"
            angleLists = []
            for item in ShoulderPitch:
                angleLists.append(item*almath.TO_RAD)
            self.motionProxy.post.angleInterpolation(names, angleLists, times, isAbsolute)

        # Simple command for the ShoulderRoll joint
        if ShoulderRoll != None:
            names = leftRightArm + "ShoulderRoll"
            angleLists = []
            for item in ShoulderRoll:
                angleLists.append(item*almath.TO_RAD)
            self.motionProxy.post.angleInterpolation(names, angleLists, times, isAbsolute)

        # Simple command for the LElbowYaw joint
        if ElbowYaw != None:
            names = leftRightArm + "ElbowYaw"
            angleLists = []
            for item in ElbowYaw:
                angleLists.append(item*almath.TO_RAD)
            self.motionProxy.post.angleInterpolation(names, angleLists, times, isAbsolute)

        # Simple command for the LElbowRoll joint
        if ElbowRoll != None:
            names = leftRightArm + "ElbowRoll"
            angleLists = []
            for item in ElbowRoll:
                angleLists.append(item*almath.TO_RAD)
            self.motionProxy.post.angleInterpolation(names, angleLists, times, isAbsolute)

        # Simple command for the LWristYaw joint
        if WristYaw != None:
            names = leftRightArm + "WristYaw"
            angleLists = []
            for item in WristYaw:
                angleLists.append(item*almath.TO_RAD)
            self.motionProxy.post.angleInterpolation(names, angleLists, times, isAbsolute)

        # Simple command for the LHand joint
        if Hand != None:
            names = leftRightArm + "Hand"
            angleLists = []
            for item in Hand:
                angleLists.append(item*almath.TO_RAD)
            self.motionProxy.post.angleInterpolation(names, angleLists, times, isAbsolute)