#include<stdio.h>

int main(){
    char fname[20], sname[20], fullname[50];
    printf("fname1: ");
    gets(fname);
    //scanf("%s", fname);
    printf("sname1: ");
    gets(sname);
    //scanf("%s", sname);
    printf("fullname: ");
    gets(fullname);
    //scanf("%s", fullname);
    printf("\n\n** Output **\n");
    printf("%s %s\n", fname, sname);
    printf("%s", fullname);
    return 0;
}
