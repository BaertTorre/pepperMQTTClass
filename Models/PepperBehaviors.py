import json
import datetime

class PepperBehaviors:
    def __init__(self, BehaviorProxy, client):
        self.BehaviorProxy = BehaviorProxy
        self.client = client


    def getBehaviors(self):
        # Know which behaviors are on the robot and print them in the shell
        names = self.BehaviorProxy.getInstalledBehaviors()
        print "Behaviors on the robot:"
        print(names)

        names = self.BehaviorProxy.getRunningBehaviors()
        print "Running behaviors:"
        print(names)


    def launchBehavior(self, behaviorName):
        # Launch and stop a behavior, if possible.
        # Check that the behavior exists.
        if (self.BehaviorProxy.isBehaviorInstalled(behaviorName)):

            # Check that it is not already running.
            if (not self.BehaviorProxy.isBehaviorRunning(behaviorName)):
                # Launch behavior.
                payloadJson = json.dumps({'startedAt': str(datetime.now()), 'sequence': behaviorName})
                self.client.publish("robot/pepper/log/sequentieStart", payload=payloadJson, qos=2, retain=False)

                self.BehaviorProxy.runBehavior(behaviorName)

                payloadJson = json.dumps({'finishedAt': str(datetime.now()), 'sequence': behaviorName})
                self.client.publish("robot/pepper/log/sequentieStop", payload=payloadJson, qos=2, retain=False)
            else:
                print "Behavior is already running."

        else:
            print "Behavior not found."
            return


    def stopBehavior(self, behaviorName):
        # Stop the behavior.
        if (self.BehaviorProxy.isBehaviorRunning(behaviorName)):
            payloadJson = json.dumps({'finishedAt': str(datetime.now()), 'sequence': behaviorName})
            self.client.publish("robot/pepper/log/sequentieStop", payload=payloadJson, qos=2, retain=False)

            self.BehaviorProxy.stopBehavior(behaviorName)
        else:
            print "Behavior is already stopped."
