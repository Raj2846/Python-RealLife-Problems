//C Program to Find the Factorial of a Number

#include <stdio.h>

int main() {
    int num, i;
    long long factorial = 1;

    printf("Enter a number: ");
    scanf("%d", &num);

    if (num < 0) {
        printf("Factorial of a negative number is not defined.\n");
    } else {
        for (i = 1; i <= num; i++) {
            factorial *= i;
        }

        printf("Factorial of %d = %lld\n", num, factorial);
    }

    return 0;
}