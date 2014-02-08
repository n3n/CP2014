#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
main(){
    char str[21][31];
    int i, j, n=20;
    for(i=0;i<n;i++)
        gets(str[i]);
    for(i=0;i<n;i++){
        for(j=0;j<strlen(str[i]);j++){
            if(str[j] != ' ' && j != 0)
                str[i][j] = tolower(str[i][j]);
            if(j == 0)
                str[i][0] = toupper(str[i][0]);
            if(str[i][j-1] == ' ')
                str[i][j] = toupper(str[i][j]);
        }
    }
    qsort(str, n, sizeof(char)*31,strcmp);
    for(i=0;i<n;i++)
        printf("%s\n", str[i]);

}
