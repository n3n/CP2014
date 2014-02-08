#include<stdio.h>

main(){
    char choice;
    printf("Geometry Type (c-circle, t-triangle, r-rectangle): ");
    scanf("%c", &choice);
    if(choice == 'c' || choice == 'C'){
        float radius;
        printf("Enter radius (cm): ");
        scanf("%f", &radius);
        printf("Area of this circle is %.1f square centimetres", (22.0*(radius*radius))/7.0);
    }
    if(choice == 't' || choice == 'T'){
        float length, height;
        printf("Enter base length (cm): ");
        scanf("%f", &length);
        printf("Enter height (cm): ");
        scanf("%f", &height);
        printf("Area of this triangle is %.1f square centimetres", (1.0/2.0)*length*height);
    }
    if(choice == 'r' || choice == 'R'){
        float width, height;
        printf("Enter base width (cm): ");
        scanf("%f", &width);
        printf("Enter height (cm): ");
        scanf("%f", &height);
        printf("Area of this rectangle is %.1f square centimetres", height*width);
    }


}
