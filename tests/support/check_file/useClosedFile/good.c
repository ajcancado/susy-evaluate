#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  FILE *f;
  f = fopen(name, "r");
  fread(buffer, 5, 6, f);
  fclose(f);
}
