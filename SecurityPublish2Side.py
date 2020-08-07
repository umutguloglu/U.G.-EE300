import paho.mqtt.client as mqtt  #import the client1
from time import sleep 			 #to delay someting
import ssl 						 #to decide which TLS version will be used

#--------------------------CALBACKS------------------------------------------

#When CONNACK message receives from broker, on_connect callback will be triggered. The name of the function can be changed.
def on_connect(client, userdata, flags, rc):
        print("Return code of the EdgeNode's connection request to the MQTT broker is " + str(rc))
        if (rc==0):
            print(flags,userdata,rc)
            client.publish("home","Hello") #Topic='home' & Message='Hello'
        else:
            print("Connection refused")

#When a PUBLISH message receives, on_message will be triggered.
def on_message(client, userdata, message):
       print("Received message '" + str(message.payload) + "' on topic '"
        + message.topic + "' with QoS " + str(message.qos))

#When Publish Acknowledged message receives, on_publish will be triggered.      
def on_publish(client,userdata,result):
    print(userdata,result)
    client.disconnect();
    pass

#----------------------------------------------------------------------------     
broker="130.149.232.227" #For doruknet, you need to change IP. This is for DAI-EAP
client = mqtt.Client("The_Client_Publish_2Side") #Creating a Client object
client.on_message=on_message #We are binding the callback on_message(Left-side) with on_message function which we defined (Right-side)
client.on_connect=on_connect #Binding on_connect
client.on_publish=on_publish #Binding on_publish
client.tls_set('<Location of caforDAI.crt or cafordoruknet.crt>','<Location of client certificate>','<Location of client key>',tls_version=ssl.PROTOCOL_TLSv1_2)
#The first three parts is the locations of certificates and key, the last part is the version which we want to use. This part must be before connect(). 
client.connect(host=broker,port=8883) #Host is the hostname or IP address of the remote broker, port can be 1883 if TLS/SSl won't be used
client.loop_forever()
