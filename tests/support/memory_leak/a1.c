#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	int *v = malloc (10 * sizeof (int));

   	if (v == NULL) {
   		printf("nao alocou\n");
   	} else {
   		v = malloc(20 * sizeof(int));
   		printf("alocou\n");
   	}

	return 0;
}