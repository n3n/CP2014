#include<stdio.h>

int main(){
char fname[50], sname[50], fullname[50];
printf("fname1: ");
gets(fname);
printf("sname1: ");
gets(sname);
printf("fullname: ");
gets(fullname);

printf("\n** Output **\n");
printf("%s %s\n",fname, sname);
printf("%s",fullname);


return 0;
}
