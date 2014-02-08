#include<stdio.h>

main(){

    int x, n, i, sum=1;
    scanf("%d %d", &x, &n);
    i = n;
    do{
        sum = sum*x;
        i--;
    }while(i>1);
    printf("%d^(%d-1)=%d", x,n,sum);
}
