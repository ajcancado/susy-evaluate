#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  int* a = malloc(8);
  free(a);
}
