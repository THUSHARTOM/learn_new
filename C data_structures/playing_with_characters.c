#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{   
    char ch,s[20],sen[1000];
    scanf("%c", &ch);
    scanf("\n");
    scanf("%s", &s);
    scanf("\n");
    scanf("%[^\n]%*c", &sen);

    printf("%c", ch);
    printf("\n");
    printf("%s", s);
    printf("\n");
    printf ( "%s", sen);

    return 0;
}