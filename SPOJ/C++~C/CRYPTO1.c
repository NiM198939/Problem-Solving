/*
 ============================================================================
 Name        : CRYPTO1.c
 Author      :
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include<time.h>
unsigned long pow_mod(unsigned long long x, unsigned long  long y, unsigned long long z)
{
    unsigned long number = 1;
    while (y)
    {
        if (y & 1)
            number = number * x % z;
        y >>= 1;
        x = x * x % z;
    }
    return number;
}
int main() {
	unsigned long a,k;
	unsigned long long p=4000000007,sqrt;
	scanf("%lu",&a);
	k=(p+1)/4;
	sqrt=pow_mod(a,k,p);
	if(sqrt>p/2)
		sqrt=p-sqrt;
	time_t current_time;
	char* c_time_string;
	current_time=(unsigned long)sqrt;
	struct tm * ptm;
	ptm=gmtime(&current_time);
	current_time=mktime(ptm);
	c_time_string=ctime(&current_time);
	printf("%s\n",c_time_string);

	return EXIT_SUCCESS;
}
