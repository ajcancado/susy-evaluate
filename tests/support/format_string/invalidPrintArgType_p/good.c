#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  int *a = malloc(4);
  a& = 5;
  printf("%p", a);

  free(a);
}
