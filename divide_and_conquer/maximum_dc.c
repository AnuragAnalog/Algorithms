#include <stdio.h>
#include <stdlib.h>

/********* DEFINED CONSTANTS **********/
#define MAX        100

/********* FUNCTION DECLARATION *********/
int maxi(int arr[], int low, int high);

/********* MAIN STARTS HERE *********/
int main(void)
{
   int        i, n, max, low = 0;
   int        arr[MAX];

   printf("Enter the number of elements: ");
   scanf("%d", &n);

   for (i = 0; i < n; i++)
   {
      printf("Enter element no. %d: ", i+1);
      scanf("%d", &arr[i]);
   }

   max = maxi(arr, low, n);
   printf("Maximum element of the array is: %d\n", max);

   exit(0);
}

/********* FUNCTION DEFINITION *********/
int maxi(int arr[], int low, int high)
{
   int        mid, maxl, maxr;

   if (low == high)
   {
      return arr[low];
   }

   mid = (int) (low+high)/2;

   maxl = maxi(arr, low, mid);
   maxr = maxi(arr, mid+1, high);

   if (maxl > maxr)
   {
      return maxl;
   }
   else
   {
      return maxr;
   }
}
