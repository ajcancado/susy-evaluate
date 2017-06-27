#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "header.h"


int f(unsigned int i)
{
    size_t s;
    printf("%I64%i", s,i );

    return 0;
}

int f2()
{
  printf("%f", 'a');
}

char *f3(char *p){
    free(p);
    return p;
}

char *f4()
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

int f5(int argc, char const *argv[])
{
  FILE*f=fopen("myfile.txt",a);
    free(f);

    return 0;
}


int main(int argc, char const *argv[])
{
  struct Books Book1;

  strcpy( Book1.title, "C Programming");
  strcpy( Book1.author, "Nuha Ali");
  strcpy( Book1.subject, "C Programming Tutorial");
  //Book1.book_id = 6495407;

  printf( "Book 1 title : %s\n", Book1.title);
  printf( "Book 1 author : %s\n", Book1.author);
  printf( "Book 1 subject : %s\n", Book1.subject);
  printf( "Book 1 book_id : %d\n", Book1.book_id);

  printf( "Total books : %d\n", totalBooks());

  return 0;
}
