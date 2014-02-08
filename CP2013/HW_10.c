#include<stdio.h>
#include<string.h>
#include<ctype.h>
main(){
    int i, j, k, c=0, bl=0;
    char s1[100], s2[100], data[30];
    gets(s1); gets(s2);
    for(i=0; i < strlen(s1); i++)
        for(j=0; j < strlen(s2); j++)
            if(isalpha(s1[i]) && (s1[i] == s2[j])){
                printf("%c == %c >> ", s1[i], s2[j]);
                for(k=0;k<c;k++){
                    if(s1[i] == data[k]){
                        printf("Already have!");
                        bl = 1; //
                        break;
                    }
                }
                if(bl == 0){
                    printf("Add \'%c\' in data", s1[i]);
                    data[c] = s1[i];
                    c++;
                }
                printf("\n");
                bl = 0;
            }
    qsort(data, c, sizeof(char), strcmp);
    printf("You have duplicate letters are %c", data[0]);
    for(i=1;i<c;i++)
            printf(",%c", data[i]);
    printf(".");
}
