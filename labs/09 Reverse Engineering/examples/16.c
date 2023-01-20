// password (defined string)
#include <stdio.h>
#include <string.h>

int main()
{
    const char* PASS = "pa55w0rd!";

    char pass[256];

    printf("Password: ");
    scanf("%s", pass);
    if (strcmp(pass, PASS) == 0)
        printf("Correct!\n");
    else
        printf("Incorrect.\n");
}
