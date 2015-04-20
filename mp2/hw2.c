#include <stdio.h>

#define PINSEL0 0x4002C000
#define FIO0DIR 0x2009C000
#define FIO0PIN0 0x2009C014
#define FIO0SET 0x2009C018
#define FIO0CLR 0x2009C01C



int main(void)
{
  unsigned int volatile * setGPIO = (unsigned int *)PINSEL0;
  unsigned int volatile * setDIR = (unsigned int *)FIO0DIR;
  unsigned char volatile * readPIN = (unsigned char *)FIO0PIN0;
  *setGPIO = *setGPIO & 0xFF7FFFFF;  // Setting Pin 27 to GPIO and input, to take in the incoming anolog input.
  *setDIR = (*setDIR & 0x0 ) | 0x08000000;

  unsigned char buffer[1024];
  void sample(unsigned char *buf)
  {

   buf[0] = readPIN;
   buf[1] = readPIN;
   buf[2] = readPIN;
   buf[3] = readPIN;
   buf[4] = readPIN;
   buf[5] = readPIN;
   buf[6] = readPIN;
   buf[7] = readPIN;
   return;
 }

  unsigned char *p = buffer;
  while(p < &buffer[1023]) {
     sample(p);
     p+=8;
   }
  return 0;
}
