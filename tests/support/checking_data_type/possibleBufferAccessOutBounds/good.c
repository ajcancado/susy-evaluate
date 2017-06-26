#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void f()
{
    char *data = malloc(sizeof(char)*100);

    char src[100];
    memset(src,'C',99);
    src[99] = '\0';
    strcpy(data,src);

    free(data);
}
int main(int argc, char const *argv[])
{
    f();
    return 0;
}