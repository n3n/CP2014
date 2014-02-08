#include<stdio.h>

int main()
{
    int n, process = true;
    scanf("%d", &n);
    if(n%7==0 || n%8==0 || n%3==0 || n%6==0)
    {
        printf("Valid Score");
    }
    else
    {
        printf("Invalid Score");
    }

    return 0;
}
