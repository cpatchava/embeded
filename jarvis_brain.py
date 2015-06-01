#!/usr/bin/python

import serial 
import subprocess

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
print("connected to: " + ser.portstr)

while True:
    # Read a line and convert it from b'xxx\r\n' to xxx
    userInput = raw_input('')
    line = "no"
    ser.write("Jarvis fan on")
    line = ser.read(500).decode('utf-8')[:-2]
    print(line)
    # print userInput
    if line:  # If it isn't a blank line
        print(line)
ser.close()
