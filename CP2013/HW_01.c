#include<stdio.h>

//#define NOW_YEAR 2013

int main(){
    char fname[90], surname[90];
    int D,O,B;
    scanf("%s", fname);
    scanf("%s", surname);
    scanf("%d/%d/%d", &D, &O, &B);
    printf("%s %s have been on this earth for %d years", fname, surname, 2013-B);

    return 0;
}
