import json

class Diagnosis():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def getDiagnosis(self):
        payloadJson = json.dumps({
            'passiveDiagnosis': self.diagnosisProxy.getPassiveDiagnosis(),
            'activeDiagnosis': self.diagnosisProxy.getActiveDiagnosis()
        })
        self.client.publish("pepper/pub/diagnosis", payload=payloadJson, qos=2, retain=False)
        print(payloadJson)

    def getTemperature(self):
        payloadJson = json.dumps({'temperature': self.bodyTemperatureProxy.getTemperatureDiagnosis()})
        print(payloadJson)
        self.client.publish("pepper/pub/temperature", payload=payloadJson, qos=2, retain=False)

    def getBattery(self):
        payloadJson = json.dumps({'batteryCharge': self.batteryProxy.getBatteryCharge()})
        print(payloadJson)
        self.client.publish("pepper/pub/battery", payload=payloadJson, qos=2, retain=False)

    def getLogs(self):
        payloadJson = json.dumps({
            'batteryCharge': self.batteryProxy.getBatteryCharge(),
            'temperature': self.bodyTemperatureProxy.getTemperatureDiagnosis(),
            'passiveDiagnosis': self.diagnosisProxy.getPassiveDiagnosis(),
            'activeDiagnosis': self.diagnosisProxy.getActiveDiagnosis()
        })
        print(payloadJson)
        return payloadJson
