// password (hash)
#include <stdio.h>
#include <string.h>
#include <openssl/sha.h>

int main()
{
    // pass is the hash generated from other program
    char* pass = "fba8cbb274352d3fa123c847a5d199238d03788b";
    char user_pass[256];
    unsigned char hash[SHA_DIGEST_LENGTH];
    char user_hash[SHA_DIGEST_LENGTH*2+1];

    // prompt the user
    printf("Password: ");
    scanf("%s", user_pass);

    // calculate the hash
    SHA1(user_pass, strlen(user_pass), hash);
    for (int i=0; i<SHA_DIGEST_LENGTH; i++)
        snprintf(user_hash+i*2, 3, "%02x", hash[i]);

    // compare the two
    if (strcmp(user_hash, pass) == 0)
        printf("Correct!\n");
    else
        printf("Incorrect.\n");
}
