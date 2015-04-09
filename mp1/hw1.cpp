#include <stdio.h>
#include<stdint.h>

uint32_t *p;

int main(){
	while(1){
		*p = 1;
		*p = 0;
	}
return 0;
}

