# py-beacon
ble beacon scanner in python.

## Scripts

### Modules
- blescan.py   => bluez libs
- proximity.py => main module

### Executable
- collector.py => scan beacon and publish via mqtt 
- emitter.py   => calculate nearest beacon and publish via mqtt

## Installation
	sudo apt-get install bluez python-bluez python-numpy
    sudo pip install -r requirements.txt

## MIT License
blescan.py source from [here](https://github.com/switchdoclabs/iBeacon-Scanner-.git)