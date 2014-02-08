#include<stdio.h>

main(){
    int wheels, in_h, in_m, in_s, out_h, out_m, out_s, h=0,m=0,s=0;
    printf("Number of wheels: ");
    scanf("%d", &wheels);
    printf("In Time: ");
    scanf("%d:%d:%d", &in_h, &in_m, &in_s);
    printf("Out Time: ");
    scanf("%d:%d:%d", &out_h, &out_m, &out_s);
    h = (out_h - in_h)*3600;
     m = (out_m - in_m)*60;
    s = out_s - in_s;
    int time=h+m+s;
    h = 0;
    if(time > 900 && time < 3600){
        if(wheels <= 4 && wheels != 2){
            printf("Parking Fee: %d Baht", 10);
        }
        else if(wheels == 2){
            printf("Parking Fee: %d Baht", 5);
        }
    }
    else if(time>=3600){
        while(time >= 3600){
            time -= 3600;
            h += 1;
        }
        if(time != 0){
            h += 1;
        }
        if(wheels <= 4 && wheels != 2){
            if(h<=3){
                printf("Parking Fee: %d Baht", 10*h);
            }
            else{
                printf("Parking Fee: %d Baht", (30)+(20*(h-3)));
            }
        }
        else if(wheels == 2){
            if(h<=3){
                printf("Parking Fee: %d Baht", 5*h);
            }
            else{
                printf("Parking Fee: %d Baht", (15)+(10*(h-3)));
            }
        }
    }


}
