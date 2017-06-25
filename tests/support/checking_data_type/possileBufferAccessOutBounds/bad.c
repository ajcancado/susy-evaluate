#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  char *a = (char *) malloc(5*sizeof(char));
   
  memset(a, 3, 55*sizeof(char));

  free(a);
  return 0;
}
