#include<stdio.h>
int main(){
    int sec_time, hour=0, min=0, sec=0, time;
    scanf("%d", &sec_time);
    time = sec_time;
    while (time >= 60){
        time -= 60;
        min += 1;
        if (min >= 60){
            min -= 60;
            hour += 1;
        }
    }
    printf("%d s = %d h %d m %d s", sec_time, hour, min, time);

    return 0;
}
