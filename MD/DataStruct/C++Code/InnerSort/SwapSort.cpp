#include <stdio.h>
#define Maxsize 50
typedef KeyType int;
typedef InfoType int;
typedef struct 
{
	KeyType key;
	InfoType data;
}RecType;
//��ʼ������
void initRec(RecType R[],KeyType keys[],int n)
{
	for(int i=0;i<n;i++)
	{
		R[i].key=keys[i];
	}
}
//�������
void printRec(RecType R[],int n)
{
	for(int i=0;i<n;i++)
	{
		printf("%d ",R[i].key);
	}
	printf("\n");
}
//ð������
void bubbleSort(RecType R[],int n)
{
	RecType tmp;
	for(int 
}
//ð���������
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