#include<stdio.h>

main(){

    int m, n, i;
    scanf("%d %d", &m, &n);
    if(m>n){
        for(i=m;i>=n;i--)
            printf("%d ", i);
    }
    else{
        for(i=m;i<=n;i++)
            printf("%d ", i);
    }

}
