#include<stdio.h>
main(){
    int h, age, i=1, d1=0, d2=0;
    float avg1=0, avg2=0;
    char s[5];
    for(i;i<=50;i++)
    {
        scanf("%s", s);
        scanf("%d %d",&h, &age);
        //if(age>20 && h>=180) d2 += 1;
        if(age>15 && h>= 175) d1 += 1;
        if(age>20 && h>=180) d2 += 1;
        avg1 += age;
        avg2 += h;
        //i++;
    }
    printf("#Age>15 and He  ight >= 175: %d", d1);
    printf("\n#Age>20 and Height >= 180: %d", d2);
    printf("\nAverage Age: %.2f", avg1/50);
    printf("\nAverage Height: %.2f", avg2/50.0);
    //getchar();
}

