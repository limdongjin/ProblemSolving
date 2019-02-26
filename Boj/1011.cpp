#include <cstdio>
#include <assert.h>

long long solve(long long x, long long y);
long long square(long long n);
void TestSolve();
void TestSquare();

int main(){
    long long n, x, y;
    TestSquare();
    TestSolve();
    scanf("%lld", &n);
    while(n--){
        scanf("%lld %lld",&x, &y);
        printf("%lld\n", solve(x, y));
    }
}

long long solve(long long x, long long y){
    long long distance = y - x;
    long long dSquare = square(distance);
    if(dSquare*dSquare == distance) return 2*dSquare - 1;
    if(distance > dSquare*dSquare + dSquare) return 2*(dSquare + 1) - 1;
    return 2*dSquare;
}
long long square(long long n){
    long long square = 1;
    while(square*square <= n){
        if(square*square == n) return square;
        square++;
    }
    return square - 1;
}
void TestSolve(){
    assert(solve(0, 3) == 3);
    assert(solve(1, 5) == 3);
    assert(solve(45, 50) == 4);
    assert(solve(0, 21) == 9);
    assert(solve(0, 25) == 9);
    assert(solve(0, 15) == 7);
    assert(solve(0, 18) == 8);
}
void TestSquare(){
    assert(square(3) == 1);
    assert(square(1) == 1);
    assert(square(2) == 1);
    assert(square(4) == 2);
    assert(square(11) == 3);
    assert(square(9) == 3);
    assert(square(82) == 9);
    assert(square(100) == 10);
}
