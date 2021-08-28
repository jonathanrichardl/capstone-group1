import paho.mqtt.client as mqtt
import time
import json
"""
Class for inter-text-messaging of IoT parts. 
"""
class Mqtt:
    def __init__(self, name : str = "python", address : str = 'localhost', port:int = 1883):
        self.client = mqtt.Client(name)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.connect(address,port)
        self.client.loop_start() 
        self.subscribe()
        time.sleep(1)

    def on_connect(self,client, userdata, flags, rc):
        if rc==0:
            print("connected ok")
            return
        print("Error Connecting!")
        return

    def on_disconnect(self):
        print("Disconnected!")

    def publish(self,message : str, topic : str = 'default'):
        self.client.publish(topic, message)

    def on_message(self,client,userdata, message : mqtt.MQTTMessage):
        if message.topic == 'default':
            print(f"I received {message.payload.decode()}")
            return
        print(json.loads(message.payload.decode()))
        

    def subscribe(self,topic : str = 'default'):
        self.client.subscribe(topic)


    




