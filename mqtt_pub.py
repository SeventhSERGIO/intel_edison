import paho.mqtt.client as paho
broker="192.168.1.100"
port=2000
# Create function for callback
def on_publish(client,userdata,result):             
        print("data published \n")
pass
# Create client object
client1= paho.Client("Raspberry_EEG")                           
# Assign function to callback
client1.on_publish = on_publish 
# Establish connection                        
client1.connect(broker,port)                                 
# Publish
ret= client1.publish("casa/puerta_principal/set","Hola")                   