# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
from adafruit_bme280 import basic as adafruit_bme280

def get_bme280():
    # Create sensor object, using the board's default I2C bus.
    # i2c = board.I2C()  # uses board.SCL and board.SDA
    i2c = board.STEMMA_I2C()
    # i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

    # change this to match the location's pressure (hPa) at sea level
    bme280.sea_level_pressure = 1017.6

    data = {}
    data['Temperature']= "%0.1f C" % bme280.temperature
    data['Humidity']="%0.1f %%" % bme280.relative_humidity
    data['Pressure']="%0.1f hPa" % bme280.pressure
    data['Altitude']="%0.2f meters" % bme280.altitude
    return (data)
