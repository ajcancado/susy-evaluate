#include <stdio.h>
#include <stdlib.h>

void foo(char *p) {
    if (*p == 0) {
    } else { *p = 0; }
}

int main(int argc, char const *argv[])
{
	char *p = malloc (sizeof(char));
	f(p);
	free(p);
	return 0;
}
