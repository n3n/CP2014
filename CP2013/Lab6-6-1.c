#include<stdio.h>
#include<string.h>

int main(){
    int i, j, value, cnt=0;
    int n;
    scanf("%d",&n);

    char list[n][31],listed[31];
    for(i=0;i<n;i++)
        gets(list[i]);
    for(i=0;i<n;i++){

    }
    for(j=0;j<n;j++){
        for(i=0;i<n-1;i++){
            value=strcmp(list[i],list[i+1]);
            if(value==1){
                strcpy(listed,list[i]);
                strcpy(list[i],list[i+1]);
                strcpy(list[i+1],listed);
            }
            else if(value==0)
                strcpy(list[i],"--");
        }
    }
    for(i=0;i<n;i++){
        if(strcmp(list[i],"--") == 0)
            cnt++;
    }
    for(i=0;i<n-p;i++)
        printf("%s", list[i]);
}
