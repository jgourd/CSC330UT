// output
#include <stdio.h>

int main()
{
    int x = 2;
    int y = 4;
    int a = x + y;
    int b = x - y;
    int c = x * y;
    int d = x / y;
    int e = x % y;

    printf("%i + %i = %i\n", x, y, a);
    printf("%i - %i = %i\n", x, y, b);
    printf("%i * %i = %i\n", x, y, c);
    printf("%i / %i = %i\n", x, y, d);
    printf("%i %% %i = %i\n", x, y, e);
}
