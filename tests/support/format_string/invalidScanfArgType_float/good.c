#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  float* a = malloc(4);
  scanf("%1f", &a);

  int b = a&;

  free(a);

  return b;
}
