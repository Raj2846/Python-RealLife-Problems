//Write a c program to check given number is Armstrong number or not.
//An Armstrong number is a number that is equal to the sum of its digits, where each digit is raised to the power of the total number of digits.
#include <stdio.h>
#include <math.h>

#include <stdio.h>

int main() {
    int num, temp, remainder, sum = 0;

    printf("Enter a 3-digit number: ");
    scanf("%d", &num);

    temp = num;

    while (temp != 0) {
        remainder = temp % 10;
        sum += remainder * remainder * remainder;
        temp /= 10;
    }

    if (sum == num)
        printf("%d is an Armstrong Number.\n", num);
    else
        printf("%d is Not an Armstrong Number.\n", num);

    return 0;
}