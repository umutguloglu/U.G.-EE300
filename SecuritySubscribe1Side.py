import paho.mqtt.client as mqtt  #import the client1
from time import sleep 			 #to delay someting
import ssl 						 #to decide which TLS version will be used

#--------------------------CALBACKS------------------------------------------

#When CONNACK message receives from broker, on_connect callback will be triggered. The name of the function can be changed.
def on_connect(client, userdata, flags, rc):
        print("Return code of the EdgeNode's connection request to the MQTT broker is " + str(rc))
        if (rc==0):
            client.subscribe("home",2) # Topic: home & QoS<=2
            print(flags,userdata,rc)
        else:
            print("Connection refused")

#When a PUBLISH message receives, on_message will be triggered.
def on_message(client, userdata, message):
       print("Received message '" + str(message.payload) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))
       global k
       k+=1

#When Subscription Acknowledged receives, on_subscribe will be triggered.
def on_subscribe(client, userdata, mid, granted_qos):
        print(userdata,mid,granted_qos)  

#----------------------------------------------------------------------------     
broker="130.149.232.227" #For doruknet, you need to change IP. This is for DAI-EAP
client = mqtt.Client("The_Client_Subscribe_1Side") #Creating a Client object
client.on_message=on_message #We are binding the callback on_message(Left-side) with on_message function which we defined (Right-side)
client.on_connect=on_connect #Binding on_connect
client.on_subscribe=on_subscribe #Binding on_subscribe
client.tls_set('<Location of caforDAI.crt or cafordoruknet.crt>',tls_version=ssl.PROTOCOL_TLSv1_2)
#The first part is the locations of caforDAI.crt or cafordoruknet.crt, the last part is the version which we want to use. This part must be before connect().
client.connect(host=broker,port=8883) #Host is the hostname or IP address of the remote broker, port can be 1883 if TLS/SSl won't be used
client.loop_start() #For more about loops, --http://www.steves-internet-guide.com/loop-python-mqtt-client/
print("Connecting to broker "+broker) 
k=0
while k<3: #After 3 messages has been received, loop will stop and the client will disconnect.
	sleep(1)
	pass
client.loop_stop()
client.disconnect()
