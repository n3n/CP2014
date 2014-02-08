#include<stdio.h>

main(){
    int n, i, ans=0;
    for(i=0;i<8;i++){
        scanf("%1d",&n);
        ans += n;
    }
    while(ans>=10){
        ans = (ans/10+ans%10);
    }
    if(ans<3){
        printf("You got number \"%d\". You are misfortune.", ans);
    }
    else if(ans == 9){
        printf("You got number \"%d\". You are good luck.", ans);
    }
    else{
        printf("You got number \"%d\". Your fortune is so-so.", ans);
    }
}
