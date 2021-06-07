class PepperWalk:
    def __init__(self, motionProxy, navigationProxy):
        self.motionProxy = motionProxy
        self.navigationProxy = navigationProxy

    def moveTo(self, xValue, yValue, thetaValue):
        self.motionProxy.moveInit()
        self.motionProxy.post.moveTo(xValue, yValue, thetaValue)

    def navigateTo(self, xValue, yValue):
        self.navigationProxy.post.navigateTo(xValue, yValue)
