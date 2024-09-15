import board
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20

# one-wire bus for DS18B20
ow_bus = OneWireBus(board.GP6)
# scan for temp sensor
ds18 = DS18X20(ow_bus, ow_bus.scan()[0])


def get_ds18b20():
    data = {}
    data['ds18b20']="%0.2f" % ds18.temperature
    return data
