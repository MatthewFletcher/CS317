#include <stdio.h>
#include <string.h>
#include <time.h>

#define BIGINT unsigned long long int

#define LENGTH 26
#define PWLENGTH 6
#define POSSIBLE 308915776

int main(int argc, char const *argv[])
{

	char chars[] = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

	char theword[PWLENGTH];
	int ch;


	//Begin clock
	clock_t begin = clock();


	

	int i = 0;
	int val;
	int j;
	
	//GOTO THIS POINT
	POINT1: 
	
	val = 0;
	j = 0;

	memset(theword,'A',PWLENGTH-1);

		//Loop through password length
		POINT2:

		ch =  val%LENGTH;
		theword[j] = chars[ch];
		val = val/LENGTH;

		printf("%s\n", theword);

		if(++j<=PWLENGTH)
		goto POINT2;

	//END LOOP HERE
	if(++i!=POSSIBLE)
	goto POINT1;



	//End clock
	clock_t end = clock();

	clock_t total = end - begin;

	printf("Run time: ");
	printf(" -->  %ld\n", total);








	
	return 0;
}