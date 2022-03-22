package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max
import kotlin.math.min

private fun solve(n: Int, k: Int): Int{
    val dp = Array(501){IntArray(501){987654321} }
    for(y in 1..k){
        dp[y][1] = 1
        dp[y][0] = 0
    }
    for(x in 1..n) { dp[1][x] = x }
    for(y in 2..k) for(x in 2..n) for(v in 1..x) {
        dp[y][x] = min(dp[y][x], 1 + max(dp[y - 1][v - 1], dp[y][x - v]))
    }
    return dp[k][n]
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (n, k) = readLine().split(' ').map {it.toInt()}

    println(solve(n, k))
}