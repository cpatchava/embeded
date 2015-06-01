#!/usr/bin/python
import termios
import tty
with open('/dev/ttyUSB0', 'rb') as f:
    fd = f.fileno()
    old_settings = termios.tcgetattr(fd)
    print "Enter characters (q to quit)"
    tty.setraw(fd)
    ch = ''
    try:
        while ch != 'q':
            ch = f.read(1)
            if not ch:
                print "End of file"
                break
            print "Read a character:", ch, '\r'
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
