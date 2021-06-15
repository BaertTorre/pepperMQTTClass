import almath


class PepperBody():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


    def turnHipManually(self, payload):
        hipPitch = payload.get("hipPitch")
        hipRoll = payload.get("hipRoll")
        speed = payload.get("speed")

        if speed and (hipPitch != None or hipRoll != None):
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
        else:
            print("Geen speed en hipPitch of hipRoll payload")


    def turnHipInterpolations(self, payload):
        hipPitch = payload.get("hipPitch")
        hipRoll = payload.get("hipRoll")
        times = payload.get("times")

        isAbsolute = True
        
        if times and (hipPitch != None or hipRoll != None):
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
        else:
            print("Geen times en hipPitch of hipRoll payload")


    def turnKneeManually(self, payload):
        kneePitch = payload.get("kneePitch")
        speed = payload.get("speed")

        if speed and (kneePitch != None):
            # Simple command for the hipRoll joint
            names = "KneePitch"
            angles = kneePitch*almath.TO_RAD
            self.motionProxy.post.setAngles(names, angles, speed)
        else:
            print("Geen speed en kneePitch payload")


    def turnKneeInterpolations(self, payload):
        kneePitch = payload.get("kneePitch")
        times = payload.get("times")

        isAbsolute = True
        
        if times and (kneePitch != None):
            # Simple command for the KneePitch joint
            if kneePitch != None:
                names = "KneePitch"
                angleLists = []
                for item in kneePitch:
                    angleLists.append(item*almath.TO_RAD)
                self.motionProxy.post.angleInterpolation(names, angleLists, times, isAbsolute)
            else:
                print("Geen times en kneePitch payload")
