#include <stdio.h>
#define Maxsize 50
typedef KeyType int;
typedef InfoType int;
typedef struct 
{
	KeyType key;
	InfoType data;
}RecType;
//≥ı ºªØ–Ú¡–
void initRec(RecType R[],KeyType keys[],int n)
{
	for(int i=0;i<n;i++)
	{
		R[i].key=keys[i];
	}
}
// ‰≥ˆ–Ú¡–
void printRec(RecType R[],int n)
{
	for(int i=0;i<n;i++)
	{
		printf("%d ",R[i].key);
	}
	printf("\n");
}
//√∞≈›≈≈–Ú
void bubbleSort(RecType R[],int n)
{
	RecType tmp;
	for(int 
}
//√∞≈›≈≈–Ú∏ƒ¡º
void bubbleImproveSort(RecType R[],int n)
{

}
void quickSort(RecType R[],int low,int high)
{


}
void checkSwapSort()
{

}
void main()
{
	
}