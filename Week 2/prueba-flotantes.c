#include <stdio.h>

int main() {
  float f;
  while(1) {
    printf("Numero: ");
    scanf("%f", &f);

    int * n = (int*) &f;
  
    printf("%f = %d\n", f, *n);
  }

  return 0;
}
