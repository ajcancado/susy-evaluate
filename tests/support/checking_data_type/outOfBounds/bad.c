#include <stdio.h>
#include <stdlib.h>

struct ABC
{
    char str[10];
};

static char f(){
    struct ABC abc;
    return abc.str[10];
}