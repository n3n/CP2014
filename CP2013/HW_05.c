#include<stdio.h>

int main(){
    int s, l, st, c;
    scanf("%d %d %d", &s, &l, &st);
    for(c=s;c<=l;c+=st){
        printf("%f\t%f\n", (float)c, (1.8 * (float)c )+32.0);
    }
    return 0;
}
