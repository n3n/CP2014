#include<stdio.h>
#include<string.h>
int main(){
    int i,j,index[10];
    char name1[10][30],name2[10][30];
    for(i=0;i<10;i++){
        scanf("%s",&name1[i]);
        strcpy(name2[i],name1[i]);
    }
    qsort(name1,10,sizeof(char)*30,strcmp);
    for(i=0;i<10;i++){
        for(j=0;j<10;j++)
        {
            if(strcmp(name1[i],name2[j]) == 0){
                index[i]=j+1;
            }
        }
    }
    for(i=0;i<10;i++){
        printf("%s:%d\n",name1[i],index[i]);
    }
    printf("\nMessage : ");
    for(i=0;i<10;i++){
        printf("%c",name1[i][1]);
    }
    return 0;
}
//Benjamin Alex John Sandy Caterine Peter Elvis Kim Tony Denny
