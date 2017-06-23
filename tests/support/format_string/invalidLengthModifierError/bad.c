#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    char bar;
    int a;

    scanf("%5s", bar);
    scanf("%5[^~]", bar);
    scanf("aa%%s", bar);
    scanf("aa%d", &a);
    scanf("aa%ld", &a);
    scanf("%*[^~]");

    return 0;
}
