#include<stdio.h>

int main(){

    int i, j,n;
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        for(j=n-i;j>0;j--){
            printf(" ");
        }
        for(j=1;j<=(i*2)-1;j++){
            printf("*");
        }
        printf("\n");
    }
return 0;
}
