#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int f()
{
    char *data = malloc (sizeof(char)*50);

    char src[100];
    memset(src,'C',99);
    src[99] = '\\0';
    strcat(data,src);
}
