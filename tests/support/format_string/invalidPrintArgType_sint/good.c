#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    char c = 1;
    unsigned char uc = 212;
    short s = 0;
    unsigned short us = 0;
    int i = 0;
    unsigned int ui = 0;
    long l = 1;
    unsigned long ul = 1;
    
    printf("c = %c uc = %u s = %hu us = %hu i = %d ui = %d l = %ld ul = %lu", c, uc, s, us, i, ui, l, ul);

    return 0;

}
