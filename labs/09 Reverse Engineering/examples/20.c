#include <stdio.h>

void check(int num1, int num2, int num3)
{
    if (num2 != num1 * 3 + 1)
        printf("Failure on 2.\n");
    else
    {
        if (num3 != num2 * 3 + 1)
            printf("Failure on 3.\n");
        else
            printf("Success!\n");
    }
}

int main()
{
    int num1, num2, num3;

    if (!scanf("%d %d %d", &num1, &num2, &num3))
        printf("Failure on 1.\n");
    else
    {
        if (num1 < 10)
            printf("Failure on 1.\n");
        else
            check(num1, num2, num3);
    }
}
