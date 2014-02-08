#include<stdio.h>
#include<string.h>

int main()
{
    int i, j, index[10], num = 0;
    char nameOld[10][20], nameSort[10][20], message[10];
    for(i=0;i<10;i++)
    {
        gets(nameOld[i]);
        strcpy(nameSort[i], nameOld[i]);
        index[i] = i+1;
    }
    qsort(nameSort,10,sizeof(char)*20,strcmp);
    for(i=0;i<10;i++)
    {
        for(j=0;j<10;j++)
        {
            if(strcmp(nameSort[i],nameOld[j]) == 0)
            {
                num = index[j];
                break;
            }
        }
        sprintf(nameSort[i], ("%s:%d"), nameSort[i] , num);
        printf("%s\n",nameSort[i]);
    }
    for(i=0;i<10;i++)
    {
        message[i] = nameSort[i][1];
    }
    printf("\nMessage : ");
    for(i=0;i<10;i++)
        printf("%c", message[i]);
    return 0;
}
/*

Benjamin
Alex
John
Sandy
Caterine
Peter
Elvis
Kim
Tony
Denny

*/
