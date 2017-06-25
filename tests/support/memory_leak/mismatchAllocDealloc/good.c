#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	FILE * pFile;
	pFile = fopen ("myfile.txt","w");
	if (pFile!=NULL)
	{
	  fputs ("fopen example",pFile);
	  fclose (pFile);
	}

	return 0;
}
