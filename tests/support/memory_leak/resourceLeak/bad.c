#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
  FILE *f;
  f = fopen(file, "r");
  fputs(f, "This is testing for fputs...\n");
}
