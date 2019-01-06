import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #Down Stop
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #Up Stop

LowerLimit = 'No'
UpperLimit = 'No'

if GPIO.input(23) == False:
        LowerLimit = 'Yes'

if GPIO.input(22) == False:
        UpperLimit = 'Yes'

while LowerLimit == 'No':
    if GPIO.input(23) == False:
        LowerLimit = 'Yes'
    print ('going down')
    UpperLimit = 'No'
print ('out')

while UpperLimit == 'No':
    if GPIO.input(22) == False:
        UpperLimit = 'Yes'
    print ('going up')
    LowerLimit = 'No'
print ('done')

