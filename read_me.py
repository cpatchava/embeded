#!/usr/bin/python

import serial 
import subprocess

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
print("connected to: " + ser.portstr)

while True:
    # Read a line and convert it from b'xxx\r\n' to xxx
    userInput = raw_input('')
    line = "no"
    if userInput:
        ser.write(userInput)
        line = ser.read(10).decode('utf-8')[:-2]
   # print userInput
    if line:  # If it isn't a blank line
        print(line)
        if line == '520':
            subprocess.call(["xte", "key Up"])
        elif line == '620':
            subprocess.call(["xte", "key Down"])
        elif line == '110':
            break

ser.close()
