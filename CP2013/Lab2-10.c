#include<stdio.h>

int main(){
	char in1,in2,in3,in4,in5;
	printf("Input1: ");
	//getch(in1);
	scanf(" %c",&in1);
	printf("Input2: ");
	//getch(in2);
	scanf(" %c",&in2);

	printf("Input3: ");
	//getch(in3);
	scanf(" %c",&in3);

	printf("Input4: ");
	//getch(in4);
	scanf(" %c",&in4);

	printf("Input5: ");
	//getch(in5);
	scanf(" %c",&in5);

	printf("**********\n");
	printf("Output1: %c\n", in1+1);
	printf("Output2: %c\n", in2);
	printf("Output3: %c\n", in3+1);
	printf("Output4: %c\n", in4);
	printf("Output5: %c", in5+1);
	return 0;
}

