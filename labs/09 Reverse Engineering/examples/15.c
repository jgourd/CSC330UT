// calling functions
#include <stdio.h>

int fact(int n)
{
    if (n == 0)
        return 1;
    return n * fact(n - 1);
}

int main()
{
    int n = 4;
    int f = fact(n);
    printf("%i! = %i\n", n, f);
}
