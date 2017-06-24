#include <stdio.h>
#include <stdlib.h>

void f(char *p) {
    if (p+1){}
}
int main(int argc, char const *argv[])
{
	char *p = NULL;
	f(p);
	return 0;
}
