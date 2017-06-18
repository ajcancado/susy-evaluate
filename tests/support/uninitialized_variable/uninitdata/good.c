#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  int *ptr_one;
  ptr_one = (int *)malloc(sizeof(int));
  *ptr_one = 25;
  printf("%d\n", *ptr_one);

  free(ptr_one);
  return 0;
}
