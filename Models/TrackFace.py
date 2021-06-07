class TrackFace():
    def __init__(self, motionProxy, trackerProxy):
        self.motionProxy = motionProxy
        self.trackerProxy = trackerProxy


    def startTrackingFace(self, trackerMode, targetName = "Face"):
        # Add target to track.
        faceWidth = 0.1
        self.trackerProxy.registerTarget(targetName, faceWidth)
        # set mode
        self.trackerProxy.setMode(trackerMode)
        # Then, start tracker.
        self.trackerProxy.track(targetName)

        print "ALTracker successfully started, now show your face to robot!"


    def stopTrackingFace(self):
        if self.trackerProxy.isActive():
            # Stop tracker.
            self.trackerProxy.stopTracker()
            self.trackerProxy.unregisterAllTargets()
            print "ALTracker stopped."
        else:
            print("Tracker is not running")