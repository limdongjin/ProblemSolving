#include <cstdio>

void solve(int n);
int findS(int n);

int main(){
    int n;
    scanf("%d", &n);
    solve(n);
}

void solve(int n){
   int s = findS(n);
   int ssum = (s*(s+1))/2;
   int p, c; // 분수: c/p
   if(!(s % 2)){
       p = n - ssum;
       c = s + 2 - p;
   }else{
       c = n - ssum;
       p = s + 2 -c;
   }
   printf("%d/%d", c, p);
}
int findS(int n){
    int i = 0;
    while(n > 0) {
        n -= i; i++;
    }
    return i - 2;
}