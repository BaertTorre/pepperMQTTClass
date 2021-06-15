import json
from datetime import datetime

class PepperBehaviors():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


    def getBehaviors(self):
        # Know which behaviors are on the robot and print them in the shell
        names = self.behaviorProxy.getInstalledBehaviors()
        print("Behaviors on the robot:")
        print(names)

        names = self.behaviorProxy.getRunningBehaviors()
        print("Running behaviors:")
        print(names)


    def launchBehavior(self, behaviorName):
        # Launch and stop a behavior, if possible.
        # Check that the behavior exists.
        if (self.behaviorProxy.isBehaviorInstalled(behaviorName)):

            # Check that it is not already running.
            if (not self.behaviorProxy.isBehaviorRunning(behaviorName)):
                # Launch behavior.
                payloadJson = json.dumps({'startedAt': str(datetime.now()), 'sequence': behaviorName})
                self.client.publish("robot/pepper/log/sequentieStart", payload=payloadJson, qos=2, retain=False)

                self.behaviorProxy.runBehavior(behaviorName)

                payloadJson = json.dumps({'finishedAt': str(datetime.now()), 'sequence': behaviorName})
                self.client.publish("robot/pepper/log/sequentieStop", payload=payloadJson, qos=2, retain=False)
            else:
                print("Behavior is already running.")

        else:
            print("Behavior not found.")
            return


    def stopBehavior(self, behaviorName):
        # Stop the behavior.
        if (self.behaviorProxy.isBehaviorRunning(behaviorName)):
            payloadJson = json.dumps({'finishedAt': str(datetime.now()), 'sequence': behaviorName})
            self.client.publish("robot/pepper/log/sequentieStop", payload=payloadJson, qos=2, retain=False)

            self.behaviorProxy.stopBehavior(behaviorName)
        else:
            print("Behavior is already stopped.")
