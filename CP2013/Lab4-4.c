#include<stdio.h>

main(){
    char ch;
    scanf("%c", &ch);
    switch(ch)
    {
    case 'A':
        printf("Genius");
        break;
    case 'B':
        printf("Good");
        break;
    case 'C':
        printf("Try Harder");
        break;
    case 'D':
        printf("Very Bad");
        break;
    case 'F':
        printf("Fail");
        break;
    default:
        printf("Invalid Input");
    }
}
