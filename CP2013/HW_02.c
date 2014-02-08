#include<stdio.h>

int main(){
    int i,cnt;
    long int n, max = 0, min= 0;
    scanf("%d", &cnt);
    scanf("%ld", &n);
    min = n, max = n;
    for(i=1;i<cnt;i++){
        scanf("%ld", &n);
        if(n<min){
            min = n;
            //printf("!!== Min ==!!\n");
        }
        if(n>max){
            max = n;
            //printf("!!== Max ==!!\n");
        }
    }
    printf("%ld\n", min);
    printf("%ld", max);
    return 0;
}
