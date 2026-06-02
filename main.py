import machine
import time

led = machine.Pin(14, machine.Pin.OUT)
botao = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP)

while (True):
    estado = botao.value()


    if (estado == 0):
        print ("botão pressionado ! ! ! HAHAHAHAHAHA")
        led.on()
    else:
       led.off()


    time.sleep(0.15)        
