from mqtt import Mqtt 
from encoder import JSON
from time import sleep
def main():
    """
    JSON data to be encoded in the form of dictionary
    """
    data = {} 
    data['name'] = 'Aaron Tanjaya'
    data['age'] = 20
    data['occupation'] = 'Grab'
    
    """
    connect into Mqtt, Change according to your mosquitto client. 
    """

    messenger = Mqtt("Raspberry Pi 1", "localhost", 1883)
    messenger.subscribe("Namaku")

    """
    Publishing JSON data every 1 seconds into the MQTT client with topic "namaku", because this Program is subscribed into namaku
    proceeds to receive and print the message aswell
    """
    try:
        while(1):
            messenger.publish(JSON.encode(data), "Namaku") #Send JSON encoded data into mqtt topic "Namaku"
            sleep(1)
            continue
    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    main()