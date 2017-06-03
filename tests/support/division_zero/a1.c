#include <stdio.h>

int main(int argc, char const *argv[])
{
    int dividend = 1000;
	  int divisor = 2;
	  double ret;

    ret = dividend / (2 * divisor - 4);

    printf("%f\n",ret);

    return 0;
}
