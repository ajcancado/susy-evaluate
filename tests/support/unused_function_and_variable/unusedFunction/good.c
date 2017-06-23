#include <stdio.h>

int f(int x);

int main(int argc, char const *argv[])
{
    int x = f(3);
    return 0;
}

int f(int x) { return x*x; }