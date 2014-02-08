#include<stdio.h>

int main(){

char fname[50], sname[50];
int id, day, month, year;
float gpa;
printf("Name: ");
scanf("%s", fname);
printf("Surname: ");
scanf("%s", sname);
printf("ID: ");
scanf("%d",&id);
printf("DOB: ");
scanf("%d/%d/%d",&day, &month, &year);
printf("GPA: ");
scanf("%f", &gpa);

printf("** \\\\Output// **\n");
printf("%s %s\n\n", fname, sname);
printf("%d\n\n", id);
printf("%02d-%02d-%02d\n\n", day, month, year);
printf("%.2f", gpa);
return 0;
}
