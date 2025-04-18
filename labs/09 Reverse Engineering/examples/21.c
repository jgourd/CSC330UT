#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_INPUT 256

void read_three_nums_from_line(char *input, int *nums)
{
    int n = sscanf(input, "%d %d %d", nums, nums+1, nums+2);

    if (n < 3)
    {
        printf("%d: Failure.\n", n);
        exit(-1);
    }
}

void check(char* input)
{
    int nums[3];

    read_three_nums_from_line(input, nums);
    if (nums[0] < 10)
    {
        printf("3: Failure.\n");
        exit(-1);
    }
    for (int i=1; i<3; i++)
    {
        if (nums[i] != nums[i-1] * 3 + 1)
        {
            printf("3: Failure on %d.\n", i+1);
            exit(-1);
        }
    }

    printf("Success!\n");
    exit(0);
}

char *read_line(void)
{
    char input[MAX_INPUT];
    char *line;

    if (!fgets(input, sizeof(input), stdin))
    {
        printf("0: Failure.\n");
        exit(-1);
    }

    input[strcspn(input, "\n")] = '\0';
    line = malloc(strlen(input) + 1);
    strcpy(line, input);
    
    return line;
}

int main()
{
    char *input;

    input = read_line();
    check(input);
}
