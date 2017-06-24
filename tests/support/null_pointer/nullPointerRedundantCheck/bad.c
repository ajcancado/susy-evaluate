#include <stdio.h>
#include <stdlib.h>

void foo(char *p) {
    if (p && *p == 0) {
    } else { *p = 0; }
}

int main(int argc, char const *argv[])
{
	char *p = NULL;
	f(p);
	return 0;
}
