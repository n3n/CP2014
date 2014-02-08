#include<stdio.h>


main(){
    int i, n;
    scanf("%d", &n);
    while(1){
        if (n%2==0){
            for(i=1;i<=n/2;i++) printf("%d",i);
            for(i=n/2;i>=1;i--) printf("%d",i);
            break;
        }
        else printf("Error\n");
        scanf("%d", &n);
    }

}
