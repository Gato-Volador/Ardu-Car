import RPIO

RPIO.setmode(RPIO.BCM)
def on():
    RPIO.output(25,1)
    RPIO.output(10,1)

def ade():
    RPIO.output(24,0)
    RPIO.output(9,0)
    RPIO.output(23,1)
    RPIO.output(11,1)

def atras():
    RPIO.output(23,0)
    RPIO.output(11,0)
    RPIO.output(24,1)
    RPIO.output(9,1)

def der():
    RPIO.output(23,0)
    RPIO.output(9,0)
    RPIO.output(24,1)
    RPIO.output(11,1)

def izq():
    RPIO.output(24,0)
    RPIO.output(11,0)
    RPIO.output(23,1)
    RPIO.output(9,1)

def parar():
    RPIO.output(10,0)
    RPIO.output(25,0)

