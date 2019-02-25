#include <cstdio>

int solve(char* word);
int checkAlphabetLength(char* word, int idx);
int cstrlen(char* word);

int main(){
    char word[105] = {'\0'};
    scanf("%s", word);
    printf("%d", solve(word));
}

int solve(char* word){
    int cnt = 0;
    int idx = 0;
    int word_length = cstrlen(word);
    while (idx < word_length){
        idx += checkAlphabetLength(word, idx);
        cnt++;
    }
    return cnt;
}
int checkAlphabetLength(char* word, int idx){
    if(word[idx] == 'c' && word[idx + 1] == '=') return 2;
    if(word[idx] == 'c' && word[idx + 1] == '-') return 2;
    if(word[idx] == 'd' && word[idx + 1] == 'z' && word[idx + 2] == '=')
        return 3;
    if(word[idx] == 'd' && word[idx + 1] == '-') return 2;
    if(word[idx] == 'l' && word[idx + 1] == 'j') return 2;
    if(word[idx] == 'n' && word[idx + 1] == 'j') return 2;
    if(word[idx] == 's' && word[idx + 1] == '=') return 2;
    if(word[idx] == 'z' && word[idx + 1] == '=') return 2;
    return 1;
}
int cstrlen(char* word) {
    int cnt = 0, idx = 0;
    while(word[idx] != '\0'){
        cnt++;
        idx++;
    }
    return cnt;
}
