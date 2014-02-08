#include<stdio.h>

main(){
    int i, j, weight, weight2;
    scanf("%d %d", &weight, &weight2);
    printf(" ||__\n[____]");
    for(i=1;i<=weight/weight2;i++){
        printf("-[_]");
    }
}
