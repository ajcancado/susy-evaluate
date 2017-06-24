#include <stdio.h>
#include <stdlib.h>

long f(int x, int y) {
    const long ret = (long)(x * y);
    return ret;
}
int main(int argc, char const *argv[])
{
	f(10,2);
	return 0
}
