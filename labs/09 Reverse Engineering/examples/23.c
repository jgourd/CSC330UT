#include <stdio.h>
#include <string.h>

int check(char *serial)
{
    if (strlen(serial) != 6)
        return 0;
    if ((serial[0] ^ 0x3A) != 'A')
        return 0;
    if ((serial[1] + serial[2]) != 'k')
        return 0;
    if (serial[5] != serial[0] + 1)
        return 0;
    return 1;
}

int main()
{
    char input[20];
    printf("Enter serial: ");
    scanf("%19s", input);

    if (check(input))
        printf("Valid serial!\n");
    else
        printf("Invalid serial!\n");

    return 0;
}
