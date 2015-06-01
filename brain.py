#!/usr/bin/python

import serial
import subprocess
import re

r_name = []
r_data = [[]]
r_function = [[]]

#function declaration we are going to be making our codes
#rstrip('\n') deletes the new line character
def init_codes():
    print("init function is called")
    remotes = 0
    code = 0
    code_val =0
    my_word = "blah"
    with open("data.txt", "r+") as f:
        for line in f:
            if ':' in line:
                rname_f = line.rstrip('\n')
                print ("Remote Name: %s" % rname_f)
                r_name.append(rname_f) #name of remote array
                r_function.append([])
                remotes+= 1 #array indexing for remotes
                code_val = 0
            elif 'usec' in line:
                numbers = line.split(",")
                print ("Delay: %s" % numbers[0] , "Pulse %s" % numbers[1].rstrip('\n'))
                my_word = my_word + numbers[0].rstrip('usec') + numbers[1].rstrip('usec\n')
                r_data[code-1].append(numbers[0].rstrip('usec'))
                code_val+= 1
                r_data[code-1].append(numbers[1].rstrip('usec\n'))
                code_val+=1
            else:
                if line != '\n' and ('OFF' in line) != 1 :
                    rname_button = line.rstrip('\n')
                    print ("Button name: %s" % rname_button )
                    r_function[remotes-1].append(rname_button)
                    code_val = 0
                    r_data.append([])
                    code+=1


ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
print("connected to: " + ser.portstr)
#primary output driver 
#it will read the data, and act
#it will constantly be reading
init_codes()
print(r_name)
print(r_function)
print(r_data)
while True:
    serialData = ser.inWaiting()
    line = ser.read(serialData)
    word = ''
    if line != '':
        #put all the characters together
        while line != '':
            word = word + line 
            line = ser.read(serialData)
        #see if text stream is worth acting on
        #in this case Jarvis is key word  
        jar = re.search('Jarvis', word)
        print("data 0: %s" %word)
        if jar is None:
            jarv = ""
        else:
            jarv = jar.group(0)
        #this is where the actions of the input get acted on
        if jarv == "Jarvis":
            print("data: %s" %word)
            if 'fan on' in line :
                ser.write(r_data[1][0])
            elif 'fan off' in line:
                ser.write("Jarvis fan off")





