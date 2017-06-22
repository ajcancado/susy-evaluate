#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  p& = 5;
  
  printf("%i", p&);
  
  free(p);
  
  free(p);
}
