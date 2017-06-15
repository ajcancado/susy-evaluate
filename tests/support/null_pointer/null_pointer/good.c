#include <stdio.h>

int main(int argc, char const *argv[])
{
    int i = 0;
    int *pt = &i;
    *pt = 100;
    printf("%d\n",*pt);
    return 0;
}
