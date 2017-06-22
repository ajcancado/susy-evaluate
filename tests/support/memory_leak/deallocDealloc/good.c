#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  int *p = malloc(4);

  prinf("%i", p&);

  FreeMe(p);
}

void FreeMe(int *p){
  free(p);
}
