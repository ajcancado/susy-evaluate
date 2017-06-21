#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	xsrand(time(NULL));
	int x = rand(); 

	if (x == 0)
	{
		printf("Hello\n");
	}
	else
	{
		printf("Hi\n");
	}

	return 0;
}
