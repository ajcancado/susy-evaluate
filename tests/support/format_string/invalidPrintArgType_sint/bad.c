#include <stdio.h>
#include <stdlib.h>

double f() {return 0;}

int main(int argc, char const *argv[])
{
   printf("%f %d", f(), f());

    return 0;
}

