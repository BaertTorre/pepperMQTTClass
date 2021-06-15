class PepperWalk():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def moveTo(self, payload):
        xValue = payload.get("xValue")
        yValue = payload.get("yValue")
        thetaValue = payload.get("thetaValue")

        if xValue != None and yValue != None and thetaValue != None:
            self.motionProxy.moveInit()
            self.motionProxy.post.moveTo(xValue, yValue, thetaValue)
        else:
            print("Geen xValue, yValue en thetaValue payloads")

    def navigateTo(self, payload):
        xValue = payload.get("xValue")
        yValue = payload.get("yValue")

        if xValue != None and yValue != None:
            self.navigationProxy.post.navigateTo(xValue, yValue)
        else:
            print("Geen xValue en yValue payloads")
