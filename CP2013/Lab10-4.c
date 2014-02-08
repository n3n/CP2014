#include<stdio.h>
#include<string.h>

int main()
{
    int n;
    scanf("%d", &n);
    if(n==1)
    {
        printf("2");
    }
    else{
        printf("%d", (factorial(n)/factorial(n-2)));
    }
    return 0;
}

int factorial(int n)
{
    if (n==0)
    {
        return 1;
    }
    return (n * factorial(n-1));
}
