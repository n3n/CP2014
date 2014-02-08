#include<stdio.h>
int main(){
    int i;
    float num, sum, avg;
    for(i=0;i<=3;i++){
        scanf("%f", &num);
        sum += num;
    }
    printf("Summation is %.2f\n", sum);
    printf("Average is %.3f", sum/4.0);
    return 0;
}
