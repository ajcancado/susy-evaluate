#include <stdio.h>
#include <stdlib.h>

typedef struct Point
{
    int x;
}Point;

int main(int argc, char const *argv[])
{
    Point p;

    p.x = 1;
    printf("%d\n", p.x);

    return 0;
}
