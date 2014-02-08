#include<stdio.h>
#include<string.h>

int max(int * arr, int n);
int main()
{
	int i, j, n, cnt=0;
	scanf("%d", &n);
	char str[n][20];
	int arr[n];
	for(i=0;i<n;i++)
	{
		scanf("%s", str[i]);
		arr[i] = strlen(str[i]);
	}
	int max_Val = max(arr, n);
	while(cnt < max_Val)
	{
		for(i=n-1;i>=0;i--)
		{
			if(arr[i] > cnt)
				printf("%c", str[i][cnt]);
			else
				printf(" ");
		}
		cnt++;
		printf("\n");
	}
	return 0;

}

int max(int * arr, int n)
{
	int i, maxVal = 0;
	for(i=0;i<n;i++)
	{
		if(arr[i] > maxVal)
			maxVal = arr[i];
	}
	return maxVal;
}