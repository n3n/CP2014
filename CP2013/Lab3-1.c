#include<stdio.h>
int main()
{
    int a=10;
    a = a+1;
    a = a+1;
    a = a++;
    a = a++;
    a = ++a;
    a = ++a;
    a += a;
    a += a;
    a += 4;
    a += 4;
    a *= 4;
    a *= 4;
    a /= 4;
    a /= 4;
    a -= 4;
    a -= 4;
    a %= 4;
    a %= 4;
    printf("%d",a);
    return 0;
}
