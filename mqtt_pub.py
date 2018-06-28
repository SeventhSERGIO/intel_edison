import paho.mqtt.client as paho
broker="192.168.1.130"
port=1883
# Create function for callback
def on_publish(client,userdata,result):             
        print("data published \n")
pass
# Create client object
client1= paho.Client("Edison_Adrian")                           
# Assign function to callback
client1.on_publish = on_publish 
# Establish connection                        
client1.connect(broker,port)                                 
# Publish
ret= client1.publish("topico/ejemplo","Hola")                   