import json

class Diagnosis:
    def __init__(self, diagnosisProxy, bodyTemperatureProxy, batteryProxy, client):
        self.diagnosisProxy = diagnosisProxy
        self.bodyTemperatureProxy = bodyTemperatureProxy

    def getDiagnosis(self):
        payloadPassive = self.diagnosisProxy.getPassiveDiagnosis()
        payloadActive = self.diagnosisProxy.getActiveDiagnosis()
        payloadJson = '{ "passiveDiagnosis": ' + '"' + str(payloadPassive) + '"' + ', "activeDiagnosis": ' + '"' + str(payloadActive) + '"' + '}'
        self.client.publish("pepper/pub/diagnosis", payload=payloadJson, qos=2, retain=False)
        print(payloadJson)

    def getTemperature(self):
        payloadJson = '{ "bodyTemperature": ' + str(self.bodyTemperatureProxy.getTemperatureDiagnosis()) + '}'
        print(payloadJson)
        self.client.publish("pepper/pub/temperature", payload=payloadJson, qos=2, retain=False)

    def getBattery(self):
        payloadJson = '{ "batteryCharge": ' + str(self.batteryProxy.getBatteryCharge()) + '}'
        print(payloadJson)
        self.client.publish("pepper/pub/battery", payload=payloadJson, qos=2, retain=False)

    def getLogs(self):
        payloadJson = json.dumps({
            'batteryCharge': self.batteryProxy.getBatteryCharge(),
            'temperature': self.bodyTemperatureProxy.getTemperatureDiagnosis(),
            'passiveDiagnosis': self.diagnosisProxy.getPassiveDiagnosis(),
            'activeDiagnosis': self.diagnosisProxy.getActiveDiagnosis()
        })
        return payloadJson
