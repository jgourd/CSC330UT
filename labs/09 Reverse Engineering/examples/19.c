// flag (encoded) with a countdown
#include <stdio.h>
#include <unistd.h>

int main()
{
    // flag is the base64 encoded string generated from other program
    char* flag = "SmFsYXBlbm8gY2hlZXNlIHNvdXA=";
    char cmd[256];
    FILE *fp;
    char dec_flag[256];

    // start the countdown
    printf("Countdown: ");
    fflush(stdout);
    for (int i=2000000; i>0; i--)
    {
        printf("%d, ", i);
        fflush(stdout);
        sleep(1);
    }
    printf("0\n");

    // base64 decode the flag
    snprintf(cmd, sizeof(cmd), "echo -n %s | base64 -d", flag);
    fp = popen(cmd, "r");
    fgets(dec_flag, sizeof(dec_flag), fp);
    pclose(fp);

    // display the flag
    printf("Flag: %s\n", dec_flag);
}
