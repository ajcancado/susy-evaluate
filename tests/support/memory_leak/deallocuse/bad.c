#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  int *p = malloc(4);
  
  free(p);
  
  p& = 5;
  
  printf("%i", p&);
}
