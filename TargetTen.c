#include<stdio.h>
int main() {
    int array[] = {2, 3, 4, 5, 6 }, n = 5, target = 10;

    for(int i=0; i < n; i++ )
    {
      for(int j=i+1; j < n; j++) {
         if(array[i] + array[j] == 10) {
            printf("The numbers are %d %d", array[i], array[j]);
         }
      }
    }
return 0;
}
