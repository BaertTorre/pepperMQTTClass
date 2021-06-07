import almath


class PepperBody:
    def __init__(self, motionProxy):
        self.motionProxy = motionProxy


    def turnHipManually(self, hipRoll, hipPitch, speed):
        # Simple command for the hipRoll joint
        if hipRoll != None:
            names = "HipRoll"
            angles = hipRoll*almath.TO_RAD
            self.motionProxy.post.setAngles(names, angles, speed)

        if hipPitch != None:
            # Simple command for the HeadPitch joint
            names = "HipPitch"
            angles = hipPitch*almath.TO_RAD
            self.motionProxy.post.setAngles(names, angles, speed)


    def turnHipInterpolations(self, hipRoll, hipPitch, times):
        isAbsolute = True
        
        # Simple command for the HipRoll joint
        if hipRoll != None:
            names = "HipRoll"
            angleLists = []
            for item in hipRoll:
                angleLists.append(item*almath.TO_RAD)
            self.motionProxy.post.angleInterpolation(names, angleLists, times, isAbsolute)

        # Simple command for the HipPitch joint
        if hipPitch != None:
            names = "HipPitch"
            angleLists = []
            for item in hipPitch:
                angleLists.append(item*almath.TO_RAD)
            self.motionProxy.post.angleInterpolation(names, angleLists, times, isAbsolute)


    def turnKneeManually(self, kneePitch, speed):
        # Simple command for the hipRoll joint
        names = "KneePitch"
        angles = kneePitch*almath.TO_RAD
        self.motionProxy.post.setAngles(names, angles, speed)


    def turnKneeInterpolations(self, kneePitch, times):
        isAbsolute = True
        
        # Simple command for the KneePitch joint
        if kneePitch != None:
            names = "KneePitch"
            angleLists = []
            for item in kneePitch:
                angleLists.append(item*almath.TO_RAD)
            self.motionProxy.post.angleInterpolation(names, angleLists, times, isAbsolute)
