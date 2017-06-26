#include <stdio.h>
#include <stdlib.h>

char *f(char *p){
    free(p);
    return p;
}
