//. Write a c program to check given number is palindrome number or not.

#include <stdio.h>

int main() {
    int num, original, remainder, reverse = 0;

    printf("Enter a number: ");
    scanf("%d", &num);

    original = num;

    while (num != 0) {
        remainder = num % 10;
        reverse = reverse * 10 + remainder;
        num /= 10;
    }

    if (original == reverse)
        printf("%d is a Palindrome Number.\n", original);
    else
        printf("%d is Not a Palindrome Number.\n", original);

    return 0;
}