#include <stdio.h>

// function which requires a certain input to produce some correct output
int func(int num1, int num2, int num3)
{
    int n = num1 * 3 + 1;

    if (n != num2)
        return -1;
    n = num2 * 3 + 1;
    if (n != num3)
        return -1;

    return 0;
}

int main()
{
    int num1, num2, num3;

    scanf("%d %d %d", &num1, &num2, &num3);
    if (num1 < 10)
    {
        printf("Failure.\n");
        return 0;
    }
    if (func(num1, num2, num3) == 0)
        printf("Success!\n");
    else
        printf("Failure.\n");
}
