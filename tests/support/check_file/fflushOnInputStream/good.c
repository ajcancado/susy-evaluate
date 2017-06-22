#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  FILE *f;
  f = fopen(name, "w");
  fflush(f);
  fclose(f);
}
