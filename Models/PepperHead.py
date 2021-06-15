import almath


class PepperHead():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def turnHeadManually(self, payload):
        angleYaw = payload.get("angleYaw")
        headPitch = payload.get("anglePitch")
        speed = payload.get("speed")

        if speed and (angleYaw != None or headPitch != None):
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
        else:
            print("Geen speed en angleYaw of anglePitch payload")


    def turnHeadInterpolations(self, payload):
        angleYaw = payload.get("angleYaw")
        headPitch = payload.get("anglePitch")
        times = payload.get("times")

        isAbsolute = True
        
        if times and (angleYaw != None or headPitch != None):
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
        else:
            print("Geen times en angleYaw of anglePitch payload")