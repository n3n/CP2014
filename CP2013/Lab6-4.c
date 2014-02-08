#include<stdio.h>
main(){
    char ch[100];
    int i, c=0;
    gets(ch);
    for(i=0;i<=100;i++){
        if (ch[i] == '\0')
            break;
        c++;
    }
    for(i=c-1;i>=0;i--)
        printf("%c", ch[i]);
}

