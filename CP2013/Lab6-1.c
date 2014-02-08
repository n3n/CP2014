#include<stdio.h>

main(){
    int M[]={2, 20, 8, 10, 4, 6, 16, 18};
    int N[]={1, 3, 9, 7, 11, 15, 19};
    int n, i, bl=0;
    do{
        scanf("%d",&n);
    }while (!((n >= 1) && (n<=20)));
    for(i=0;i<8 && bl==0;i++){
        if (N[i]==n){
            printf("%d is in N at index [%d]",n,i+1);
            bl = 1;
            break;
            }
        }
    for(i=0;i<7 && bl==0;i++){
        if (M[i]==n){
            printf("%d is in M at index [%d]",n,i+1);
            bl = 1;
            break;
        }
    }
    if(bl==0){
        printf("%d is not in neither M nor N", n);
    }
}
