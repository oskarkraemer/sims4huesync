from PIL import ImageGrab, Image
import requests, json
from rgbxy import Converter
import time

converter = Converter()

bridge_ip= ""
key = ""

room_id = ""
grab_xy = [78,1404]

while 1:
    im=ImageGrab.grab()
    pix= im.load()
    pixrgb=pix[grab_xy[0],grab_xy[1]]
    try:
        converter.rgb_to_xy(pixrgb[0],pixrgb[1],pixrgb[2])[0]
        data ={'xy':[converter.rgb_to_xy(pixrgb[0],pixrgb[1],pixrgb[2])[0],converter.rgb_to_xy(pixrgb[0],pixrgb[1],pixrgb[2])[1]]}
        r =requests.put("http://"+bridge_ip+"/api/"+key+"/groups/"+room_id+"/action",json.dumps(data))
    except ZeroDivisionError:
        pass
    time.sleep(5)