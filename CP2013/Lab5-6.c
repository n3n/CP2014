#include<stdio.h>

main(){

    int n, sum=0;
    scanf("%d", &n);
    while(n!=-9){
        scanf("%d", &n);
        sum += n;
    }
    printf("%d", sum);
}
