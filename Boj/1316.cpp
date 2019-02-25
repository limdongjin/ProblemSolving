#include <cstdio>
#include <iostream>
int solve(char** words, int n);
int isGroupWord(const char* word);
int cstrlen(const char * word);
int main(){
    char** words;
    int cnt;
    int n;
    scanf("%d", &n);
    words = new char*[n+2];
    for(int i =0; i<n;i++) {
        words[i] = new char[101];
        scanf("%s", words[i]);
    }
    cnt = solve(words, n);
    printf("%d", cnt);
}
int solve(char** words, int n){
    int cnt = 0;
    for(int i=0;i<n;i++){
        cnt += isGroupWord(*(words + i));
    }
    return cnt;
}
int isGroupWord(const char* word){
    int alpha[27]={0};
    char bef = ' ';
    int word_length = cstrlen(word);
    for(int i = 0; i < word_length; i++){
        if(bef == ' '){
            bef = word[i];
            continue;
        }
        if(bef != word[i]){
            if(alpha[word[i]-'a'] == 1) return 0;
            alpha[bef-'a'] = 1;
        }
        bef = word[i];
    }
    return 1;
}
int cstrlen(const char * word){
    int cnt = 0;
    int i = 0;
    while(word[i] != '\0'){
        i++;
        cnt++;
    }
    return cnt;
}