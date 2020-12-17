import blynklib
import random
import blynktimer

BLYNK_AUTH = 'vIjR7p7Fmdc_FUest13qBA3pnIGYT_Pz'

# initialize blynk
blynk = blynklib.Blynk(BLYNK_AUTH)
timer = blynktimer.Timer()

READ_PRINT_MSG = "[READ_VIRTUAL_PIN_EVENT] Pin: V{}"


# register handler for virtual pin V11 reading
@timer.register(vpin_num=8, interval=4, run_once=False)
def write_to_virtual_pin(vpin_num=1):
    blynk.virtual_write(vpin_num, 255)

	
@timer.register(vpin_num=8, interval=9, run_once=False)
def write_to_virtual_pin(vpin_num=1):
    blynk.virtual_write(vpin_num, 0)


###########################################################
# infinite loop that waits for event
###########################################################
while True:
    blynk.run()
    timer.run()
