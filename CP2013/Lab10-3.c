#include<stdio.h>
#include<string.h>
int main()
{
    int i, j;
    char inp[50], output[50];
    scanf("%s", inp);
    for(i=0 ; i<strlen(inp) ; i++)
    {
        if(inp[i] == '*')
        {
            inp[i-1] = '';
            if(inp[i+1] != '\0')
                inp[i+1] = '';
            inp[i] = '';
        }
    }
    for(i=0;i<strlen(inp);i++)
    {
        if(inp[i] != '-')
            putchar(inp[i]);
    }
    return 0;
}
