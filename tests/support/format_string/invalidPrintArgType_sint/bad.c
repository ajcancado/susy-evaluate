#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    char c;
    unsigned char uc;
    short s;
    unsigned short us;
    int i;
    unsigned int ui;
    long l;
    unsigned long ul;

    printf("%hhu %hhu %hhu %hhu %hhu %hhu %hhu %hhu", c, uc, s, us, i, ui, l, ul);
    return 0;
}
