#include<stdio.h>

int sum(int *arr, int n);
int main(){

    int d, m, dom[12] = {31,28,31,30,31,30,31,31,30,31,30,31} ,first_day = 3;
    char day[7][20] = {"Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"};
    scanf("%d %d", &d, &m);

    printf("%s", day[(sum(dom, m) + d + first_day - 1) % 7]);
    return 0;
}

int sum(int *arr, int n)
{
    int i, summation = 0;
    for(i=0;i<n-1;i++)
        summation += arr[i];
    return summation;
}
