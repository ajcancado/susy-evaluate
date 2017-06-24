#include <stdio.h>
#include <stdlib.h>

void f(char *p) {
	char *t = p+1;
    if (t != NULL){}
}
int main(int argc, char const *argv[])
{
	char *p = NULL;
	f(p);
	return 0;
}
