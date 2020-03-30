#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int a, b;
    float c, d;
    scanf("%d %d", &a, &b);
    scanf("\n");
    scanf("%f %f", &c, &d);

    printf("%d", a+b);
    printf(" ");
    printf("%d", a-b);
    printf("\n");
    printf("%.1f", c+d);
    printf(" ");
    printf("%.1f", c-d);
    
    return 0;
}
