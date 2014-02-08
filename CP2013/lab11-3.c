#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
// --------------- Prototype Func ----------------
int compare1 ( const void *pa, const void *pb );
// --------------- Prototype Func ----------------
int main()
{
    int i, j, date[10][3], index1=0, index2=0, n=0, len=0;
    char ch_date[150], tmp_ch[5];
    gets(ch_date);

    for(i=0;i<strlen(ch_date);i++)
    {
        if(isdigit(ch_date[i]))
        {
            tmp_ch[n] = ch_date[i];
            n++;
        }
        if(ch_date[i] == '/' || ch_date[i] == ' ' || ch_date[i+1] == '\0')
        {
            tmp_ch[n] = '\0';
            date[index1][index2] = atoi(tmp_ch);
            index2++;
            n=0;
        }
        if(ch_date[i] == ' ')
        {
            index1++;
            index2 = 0;
            n=0;
        }
    }

    qsort(date, index1+1, sizeof date[0], compare1);

    for(i=0;i<index1+1;i++)
        printf("%02d/%02d/%d ", date[i][0], date[i][1], date[i][2]);

    return 0;
}

int compare1 ( const void *date1, const void *date2 ) {
    const int *p_date1 = date1;
    const int *p_date2 = date2;

    if(p_date1[2] == p_date2[2])
    {
        if(p_date1[1] == p_date2[1])
        {
            return (p_date1[1] - p_date2[1]);
        }
        return (p_date1[1] - p_date2[1]);
    }
    return (p_date1[2] - p_date2[2]);
}
