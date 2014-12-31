# py-beacon
ble beacon scanner in python.

## Scripts

#### Modules
- blescan.py   => bluez libs
- proximity.py => main module

#### Executable
- collector.py => scan beacon and publish via mqtt 
- emitter.py   => calculate nearest beacon and publish via mqtt

## Test
    sudo python test.py
    sudo python collector.py
    python emitter.py

## Installation
	sudo apt-get install bluez python-bluez python-numpy
    sudo pip install -r requirements.txt

## Misc
- [setup environment](https://gist.github.com/taka-wang/29433180cc8affcde3b2)
- [install mosquitto 1.4 on raspberry pi](https://gist.github.com/taka-wang/1c47cde3e4c9c2d83156)

## MIT License
blescan.py source from [here](https://github.com/switchdoclabs/iBeacon-Scanner-.git)