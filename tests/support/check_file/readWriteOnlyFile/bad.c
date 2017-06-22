#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  FILE *f;
  f = fopen(name, "w");
  fread(buffer, 5, 6, f);
  rewind(f);
  fwrite(buffer, 5, 6, f);
  fclose(f);
}
