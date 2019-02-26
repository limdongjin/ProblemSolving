#include <cstdio>
#include <assert.h>

int dp[17][17] = {0};
int solve(int floor, int n);
void TestSolve();
int main(){
    int t, floor, n;
    TestSolve();
    scanf("%d", &t);
    while(t--){
        scanf("%d", &floor);
        scanf("%d", &n);
        printf("%d\n", solve(floor, n));
    }
}
int solve(int floor, int n){
    if(floor == 0) return n;
    if(n == 1) return 1;
    return solve(floor, n - 1) + solve(floor - 1, n);
}
void TestSolve(){
    assert(solve(1, 3) == 6);
    assert(solve(2, 3) == 10);
}