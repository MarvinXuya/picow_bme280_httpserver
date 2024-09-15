import os

import socketpool
import wifi
import bme280
import ds18b20
from adafruit_httpserver import Server, Request, Response, JSONResponse
import mdns

wifi.radio.hostname=os.getenv("CIRCUITPY_WEB_INSTANCE_NAME")
mdns_server=mdns.Server(wifi.radio)
#mdns_server.hostname = "name"
#mdns_server.instance_name = "name"

pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static", debug=True)

@server.route("/*")
def base(request: Request):
    message={}
    message.update(bme280.get_bme280())
    message.update(ds18b20.get_ds18b20())
    return JSONResponse(request, message)

@server.route("/weather")
def base(request: Request):
    message={}
    message.update(bme280.get_bme280())
    message.update(ds18b20.get_ds18b20())
    return JSONResponse(request, message)

server.serve_forever(str(wifi.radio.ipv4_address),1985)
