#include <stdio.h>
#include <stdlib.h>

void foo()
{

    int bar = 5;

    printf("%d\n",bar);
    scanf("%d",&bar);
}

int main(int argc, char const *argv[])
{
    foo();
    return 0;
}