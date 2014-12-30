import sys
from proximity import *

scanner = Scanner(loops=3)
while True:
    val = -sys.maxint - 1
    mac = ""
    for beacon in scanner.scan():
        print beacon
        result = beacon.split(",")
        if int(result[5]) > val :
            val = int(result[5])
            mac = result[0]
    if (mac == "fe:95:5c:da:63:9d"):
        print("GREEN:(fe:95:5c:da:63:9d):", val)
    elif (mac == "d7:53:ea:b7:22:6a"):
        print("BLUE:(d7:53:ea:b7:22:6a):", val)
    else:
        print("Unknown " + mac)
    print("========================")

        