#include<stdio.h>

main(){

    int i, j;
    float  n, max, min, sum;
    scanf("%d", &j);
    scanf("%f", &n);
    max = n, min = n, sum=n;
    for(i=2;i<=j;i++){
        scanf("%f", &n);
        if(n>max) max=n;
        if(n<min) min=n;
        sum += n;
    }
    printf("%d Values\nMin: %.3f\nMax: %.3f\nAvg: %.3f", j, min, max, sum/j);

}
