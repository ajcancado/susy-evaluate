#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <alloca.h>

void f()
{
    char *data = alloca(50);

    char src[100];
    memset(src,'C',99);
    src[99] = '\0';
    strcpy(data,src);
}
int main(int argc, char const *argv[])
{
    f();
    return 0;
}