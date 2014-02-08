#include<stdio.h>
#include<string.h>
#include<ctype.h>
int main()
{
	int i, j, cnt=-1;
	char str[100], tmp_ch[2] = { '-', '\0' }, phone[8][4] = { "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ" };
	scanf("%[^\n]s",str);
	for(i=0;i<strlen(str);i++)
	{
		tmp_ch[0] = str[i];
		if(isdigit(str[i]))
			cnt++;
		if(str[i+1] == ' ' || str[i+1] == '\0')
		{
			if(str[i] == '7' || str[i] == '9')
				printf("%c", phone[abs(atoi(tmp_ch)-2)][cnt%4]);
			else
				printf("%c", phone[abs(atoi(tmp_ch)-2)][cnt%3]);
			cnt = -1;
		}
	}
}