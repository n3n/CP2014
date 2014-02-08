#include<stdio.h>

int main(){
    float width,height;
    scanf("%f",&width);
    scanf("%f",&height);
    /*
    if (width==3 && height==4){
        printf("12.00\n");
        printf("0.0012000000\n");
        printf("0.0000120000");
    }
    else{*/
    printf("%.2f\n",  width*height);
    printf("%.10f\n",(width*height)/10000.0);
    printf("%.10f",(width*height)/100000.0);
    return 0;
}
