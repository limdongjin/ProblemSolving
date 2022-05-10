package main.kotlin.p2482
// 2482 색상환

fun main(){
    val n = readln().toInt()
    val k = readln().toInt()

    print(solve(n, k))
}

fun solve(n: Int, k: Int): Int {
    if(k == 1) return n

    val dp = Array(n+1) { Array(n+1){ -1L } }
        .apply {
            for(y in 1..n) {
                this[y][0] = 0           // 0 개의 색을 선택 -> 경우의 수 = 0
                this[y][1] = y.toLong() //  크기가 y인 배열에서 1 개의 색을 선택 -> 경우의 수 = y
            }
        }

    // dp[n][k] = go(0번 색 선택) + go(0번 색 선택x)
    dp[n][k] = go(n-3, k-1, dp) + go(n-1, k, dp)

    return (dp[n][k] % 1_000_000_003).toInt()
}

fun go(n: Int, k: Int, dp: Array<Array<Long>>): Long {
    when {
        n < 0 || k < 0 -> return 0
        dp[n][k] != -1L -> return dp[n][k]
        n/2 + 1 < k -> return 0 // ex, 크기가 20인 배열에서 11개의 요소를 선택할 수 없다.
    }

    // dp[n][k] = go(첫번째 색 선택) + go(선택x)
    dp[n][k] = (go(n-2, k-1, dp) + go(n-1, k, dp)) % 1_000_000_003

    return dp[n][k]
}