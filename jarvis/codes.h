#ifndef CODES_H
#define CODES_H
#include <Arduino.h>
const byte IR_LED = 13;
struct ir_code{
	int * delay;
	int * pulese;
	int size;
};


//functions for the tv
void tv_remote_on_off();
void tv_remote_volume_up();
void tv_remote_volume_down();
void tv_remote_mute();


//functions for the fan
void fan_on_off();
void fan_speed();
void fan_timer();

//initialize the data that is already here
int initialize();
//init the existing button possiblities
void button_execute(ir_code &code);
//add new button functions
void button_learn();
//execute a button
void click(int id);


void pulseIR(long microsecs);
#endif
