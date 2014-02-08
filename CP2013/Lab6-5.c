#include<stdio.h>

main(){
    char str[100], ch;
    int i, n=0, pos[100],c=0;
    gets(str);
    ch = getchar();
    for(i=0;i<100;i++){
        if(str[i] == '\0')
            break;
        c++;
    }
    for(i=0;i<c;i++){
        if((str[i] >= 65 && str[i] <= 90))
            str[i] = str[i] + 32;
        if(str[i] == ch){
            pos[n] = i+1;
            n++;
        }
    }
    printf("There is/are %d \"%c\" in the above sentences.\nPosition: ",n,ch);
    printf("%d",pos[0]);
    for(i=1;i<n;i++){
        printf(", %d", pos[i]);
    }
}
