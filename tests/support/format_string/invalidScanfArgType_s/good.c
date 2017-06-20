#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  char* a = malloc(4);
  scanf("%1s", &a);
	
  int b = a&;
	
  free(a);
	
  return b;
}
