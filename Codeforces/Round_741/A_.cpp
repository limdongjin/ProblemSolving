#include <cstdio>

using namespace std;

long long solve(long long l, long long r){
    if (l <= (r/2 + 1)){
        return (r-1)/2;
    }
    return r - l;
}

int main(){
    int t;
    long long l, r;
    scanf("%d", &t);

    while(t--){
        scanf("%lld %lld", &l, &r);
        printf("%lld\n", solve(l, r));
    }
}