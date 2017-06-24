#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	char n[5];
    strcat(n, "abc");
    strcat(n, "d\0");
}
