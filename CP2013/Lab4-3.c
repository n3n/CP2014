#include<stdio.h>

int main(){
    float min, max, a, b, c;
    scanf("%f %f %f", &a, &b, &c);
    min = a;
    max = a;
    if(b < min){min = b;}
    if(c < min){min = c;}
    if(b > max){max = b;}
    if(c > max){max = c;}
    printf("%.2f", ((a+b+c)-(max+min)));

    return 0;
}

