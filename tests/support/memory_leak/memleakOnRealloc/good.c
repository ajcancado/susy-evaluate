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
        char *t = realloc(a, i);
        if(t != NULL) a = t;
        if (f2(i))
        {
            continue;
        }
    }

    return a;
}

int main(int argc, char const *argv[])
{
  char *a = f();
  free(a);
  return 0;
}