#include <stdio.h>
#define LENGTH 6

int main(int argc, char const *argv[])
{
	int list[] = {6,8,10,4,3,5};

	for (int i = 0; i < LENGTH; ++i)
	{
		for (int j = 0; j < LENGTH - i - 1; ++j)
		{
			if (list[j] > list[j+1]) 
		      {
		        int temp = list[j];
		        list[j] = list[j+1];
		        list[j+1] = temp;
		      }
		}
		
	}

	for (int i = 0; i < LENGTH; ++i)
	{
		printf("%d\n", list[i]);
	}
	return 0;
}