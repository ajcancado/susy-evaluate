#include <stdio.h>
#include <stdlib.h>

char *f()
{
    char *a = 0;
    int i = 0;
    for (int i = 0; i < 50; i++)
    {
        if (f1(i))
        {
            continue;   
        }
        a = realloc(a, i);
        if (f2(i))
        {
            continue;
        }
    }

    return a;
}
