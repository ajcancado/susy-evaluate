#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  int *p = malloc(4);

  printf("%i", p&);
  
  free(p);
  
  p& = 5;
  
  printf("%i", p&);
}
