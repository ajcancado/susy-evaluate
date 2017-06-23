#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *bar = malloc (sizeof(char));
    int *a = malloc (sizeof(int));
    
    scanf("%1s", bar);
    scanf("%d", a);

    free(bar);
    free(a);

    return 0;
}
