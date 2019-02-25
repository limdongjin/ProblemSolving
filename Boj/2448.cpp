#include <cstdio>
#include <iostream>
char map[4000][8000];

void solve(int n);
void initMap(int n);
void buildStar(int n, int x, int y);
void printMap(int n);

int main(){
    int n;
    scanf("%d", &n);
    solve(n);
}

void solve(int n){
    initMap(n);
    buildStar(n, n-1, 0);
    printMap(n);
}
void initMap(int n){
    for(int i = 0; i < n; i ++)
        for(int j = 0; j < 2*n; j++)
            map[i][j] = ' ';
}
void buildStar(int n, int x, int y){
    char st = '*';
    if(n == 3){
        map[y][x] = st;
        map[y+1][x-1] = st;
        map[y+1][x+1] = st;
        map[y+2][x-2]=st;
        map[y+2][x-1]=st;
        map[y+2][x]=st;
        map[y+2][x+1]=st;
        map[y+2][x+2]=st;
        return;
    }
    buildStar(n/2, x, y);
    buildStar(n/2, x - (n/2), y + (n/2));
    buildStar(n/2, x + (n/2), y + (n/2));
}
void printMap(int n){
    for(int i = 0; i < n; i ++) {
        for (int j = 0; j < 2 * n; j++) {
            printf("%c", map[i][j]);
        }
        printf("\n");
    }
}