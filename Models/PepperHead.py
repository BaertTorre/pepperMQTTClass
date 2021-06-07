import almath


class PepperHead:
    def __init__(self, motionProxy):
        self.motionProxy = motionProxy

    def turnHeadManually(self, angleYaw, headPitch, speed):
        # Simple command for the HeadYaw joint
        if angleYaw != None:
            names = "HeadYaw"
            angles = angleYaw*almath.TO_RAD
            self.motionProxy.post.setAngles(names, angles, speed)

        # Simple command for the HeadPitch joint
        if headPitch != None:
            names = "HeadPitch"
            angles = headPitch*almath.TO_RAD
            self.motionProxy.post.setAngles(names, angles, speed)


    def turnHeadInterpolations(self, angleYaw, headPitch, times):
        isAbsolute = True
        
        # Simple command for the HeadYaw joint
        if angleYaw != None:
            names = "HeadYaw"
            angleLists = []
            for item in angleYaw:
                angleLists.append(item*almath.TO_RAD)
            self.motionProxy.post.angleInterpolation(names, angleLists, times, isAbsolute)

        # Simple command for the HeadPitch joint
        if headPitch != None:
            names = "HeadPitch"
            angleLists = []
            for item in headPitch:
                angleLists.append(item*almath.TO_RAD)
            self.motionProxy.post.angleInterpolation(names, angleLists, times, isAbsolute)