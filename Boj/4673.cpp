#include <cstdio>
int selfNums[10010];
void solve();
int findSelfNum(int num);
int main(){
    solve();
}
void solve(){
    for(int idx=1;idx<=10000;idx++){
        selfNums[findSelfNum(idx)] = 1;
        if(!selfNums[idx]) printf("%d\n", idx);
    }
}
int findSelfNum(int num){
    int res = num;
    for(int i=10000;i>=10;i/=10){
        if(num >= i){ res += num / i; num %= i; }
    }
    return res + num;
}