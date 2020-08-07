mosquitto_sub -t topic -h 130.149.232.227 -p 1883 
mosquitto_pub -t topic -h 130.149.232.227 -p 1883 -m 'Hello'
# For communication with no authentication. 

mosquitto_sub -t topic -h 130.149.232.227 --cafile ~/Security/caforDAI.crt -p 8883 
mosquitto_pub -t topic -h 130.149.232.227 --cafile ~/Security/caforDAI.crt -p 8883 -m 'Hello'
# For communication with one side authentication.

mosquitto_sub --cafile ~/Security/caforDAI.crt --cert ~/Security/client1.crt --key ~/Security/client.key -h 130.149.232.227 -p 8883 -t topic  
mosquitto_pub --cafile ~/Security/caforDAI.crt --cert ~/Security/client1.crt --key ~/Security/client.key -h 130.149.232.227 -p 8883 -t topic -m "Hello"
# For communication with two side authentication.
