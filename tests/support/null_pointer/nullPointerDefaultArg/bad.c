#include <stdio.h>
#include <stdlib.h>

void f(int *p) {
    printf("%d\n", *p);
}

int main(int argc, char const *argv[])
{
	int *p = NULL;
	f(p);
	return 0;
}