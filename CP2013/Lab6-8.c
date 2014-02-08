#include<stdio.h>
int what(char s){
    if(s >= 97 && s <= 122)
        return -1; // lower
    return 1; // upper
}
char find_index(char s){
    int i;
    char keys_up[26] = "qpyxbaiwgzvfuthsojlkdecnmr";
    char keys_low[26] = "QPYXBAIWQZYFUTHSOJLKDECNMR";
    for(i=0;i<26;i++){
        if(keys_up[i] == s || keys_low[i] == s){
            if(what(s) == 1)
                return keys_low[(i-5+26)%26];
            return keys_up[(i-5+26)%26];
        }
    }
}

main(){

    char str[40], encrpy[40];
    int i, j,c=0;
    gets(str);
    for(i=0;i<40;i++){
        if(str[i] == '\0')
            break;
        c++;
    }
    for(i=0;i<c;i++){
        if ((str[i] >= 97 && str[i] <= 122) || (str[i] >= 65 && str[i] <= 90))
            printf("%c", find_index(str[i]));
        else
            printf("%c",str[i]);
    }

}
