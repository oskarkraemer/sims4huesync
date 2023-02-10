# sims4huesync

A Python script that syncs the emotions of a Sim with your Phillips Hue Lights by using the xy coordinates of a pixel. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

## Usage
In the python file, populate the settings for **bridge_ip**, **key**, **room_id**, and **grab_xy**.

```python
bridge_ip= ""
key = ""

room_id = ""
grab_xy = [78,1404]
```
**bridge_ip**
>The IP address of your Phillips Hue bridge. It can be found by visiting [https://discovery.meethue.com/](https://discovery.meethue.com/) or within the settings of the Hue mobile app. e.g. ``192.168.x.x``

**key**
>Your Phillips Hue API-Key. You can generate one by visiting https://**bridge_ip**/debug/clip.html where "bridge_ip" is replaced with the actual IP address. Then, within this page put ``/api`` in the URL text box and ``{"devicetype":"sims4huesync#your_name"}`` in the Message Body text box. Press the physical button on your Phillips Hue bridge then click the POST button on the web page. The result listed as username is your API-key. e.g. ``1028d66426293e821ecfd9ef1a0731df``

**room_id**
>The ID of the room in which you want the synchronization to happen. You can find options for room IDs by visiting https://**bridge_ip**/api/**key**/groups where "bridge_ip" and "key" are replaced with their real values. You can see all of your rooms and their respective IDs to choose the desired room. e.g. ``1``

**grab_xy**
>The coordinates on your screen which has the color of the Sim Emotion or the desired coordinates on screen to sync color changes to. You could use a full screen capture open in [GIMP](https://www.gimp.org/) to find the xy coordinates of a pixel. e.g. ``[78,1404]``

Save the file and run it in command line.
```bash
python "sims4needs - public.py"
```

## Credits

* [Pillow](https://github.com/python-pillow/Pillow) used to grab a pixel from the screen

* [requests](https://github.com/psf/requests) used for sending HTTP requests to the Hue API

* [rgbxy](https://github.com/benknight/hue-python-rgb-converter) used to convert from RGB color to CIE1931 "xy" color
## License

[The Unlicense](https://github.com/oskarkraemer/sims4huesync/blob/master/LICENSE)
