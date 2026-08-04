#include <stdio.h>

int main() {
    FILE *fp;
    char str[100];

    fp = fopen("data.txt", "r");

    if (fp == NULL) {
        printf("Error: Cannot open file.\n");
        return 1;
    }

    fgets(str, sizeof(str), fp);

    printf("String from file:\n%s", str);

    fclose(fp);

    return 0;
}