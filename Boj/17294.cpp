#include <stdio.h>

int check(const char* input_str);

int main(){
    char input_n[20];

    scanf("%s", input_n);

    if(check(input_n)) printf("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!\n");
    else printf("흥칫뿡!! <(￣ ﹌ ￣)>\n");
}

int check(const char* input_str){
    int diff = -1;
    int prevDiff;
    int i = 0;
    while(input_str[i] != '\0'){
        if(i == 0) { i++; continue; }
        prevDiff = diff;
        diff = input_str[i] - input_str[i-1];
        if(i == 1) { i++; continue; }
        if(prevDiff != diff) return 0;
        i++;
    }
    return 1;
}
