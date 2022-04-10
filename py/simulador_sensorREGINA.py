import time
import paho.mqtt.client as paho
from random import randrange, uniform
from decimal import Decimal
from datetime import datetime
broker="143.107.145.33"
#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))

client= paho.Client("helix") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
#client.username_pw_set(username="helix",password="H3l1xNG")
######Bind function to callback
client.on_message=on_message
#####
print("connecting to broker ",broker)
client.connect(broker)#connect
num = 1
while True:
    print("Cycle: ",num)
    client.connect(broker)#connect
    print("Enviando dados para IoTSmartReginaLabDC:temp")
    v_l1n = uniform(216, 220)
    print("Tensao -> {:.1f}".format(v_l1n))
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/v_l1n", "{:.1f}".format(v_l1n))#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/v_l2n","0.0")#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/v_l3n","0.0")#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/v_l1l2","0.0")#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/v_l2l3","0.0")#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/v_l3l1","0.0")#publish
    a_l1 = uniform(7, 8)
    print("Corrente -> {:.2f}".format(a_l1))
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/a_l1", "{:.1f}".format(a_l1))#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/a_l2","0.0")#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/a_l3","0.0")#publish
    w_l1 = uniform(1600, 1800)
    print("Potencia -> {:.1f}".format(w_l1))
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/w_l1", "{:.1f}".format(w_l1))#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/w_l2","0.0")#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/w_l3","0.0")#publish
    va_l1 = uniform(1600, 1800)
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/va_l1", "{:.1f}".format(va_l1))#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/va_l2","0.0")#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/va_l3","0.0")#publish
    var_l1 = uniform(-400, -500)
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/var_l1", "{:.1f}".format(var_l1))#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/var_l2","0.0")#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/var_l3","0.0")#publish
    v_ln_e = uniform(216, 220)
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/v_ln_e", "{:.1f}".format(v_ln_e))#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/v_ll_e","0.0")#publish
    w_e = uniform(1600, 1800)
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/w_e", "{:.1f}".format(w_e))#publish
    va_e = uniform(1600, 1800)
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/va_e", "{:.1f}".format(va_e))#publish
    var_e = uniform(-400, -500)
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/var_e", "{:.1f}".format(var_e))#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/var_e_max","0.0")#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/var_e_avg","0.0")#publish
    pf_l1 = uniform(0.5, 1)
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/pf_l1", "{:.2f}".format(pf_l1))#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/pf_l2","0.0")#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/pf_l3","0.0")#publish
    pf_e = uniform(0.5, 1)
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/pf_e", "{:.2f}".format(pf_e))#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/phase_sequence","0.0")#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/hz","60.0")#publish
    kwh_tot = uniform(16500, 18000)
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/kwh_tot", "{:.1f}".format(kwh_tot))#publish
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/kvarh_tot","0.0")#publish
    date_time = datetime.now()
    client.publish("/iot/IoTSmartReginaLabDC:temp/attrs/date_time", str(date_time))#publish
    time.sleep(randrange(15,30))
    num += 1
client.loop_stop() #stop loop
client.disconnect() #disconnect


