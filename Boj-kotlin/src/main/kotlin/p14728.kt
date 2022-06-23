package main.kotlin.p14728

import kotlin.math.max

fun main() = with(System.`in`.bufferedReader()){
    val (n, t) = readLine().split(" ").map(String::toInt)
    val ksList = Array(n+1) { 0 to 0 }
    repeat(n) { i ->
        ksList[i+1] = readLine().split(" ").map(String::toInt).let { it[0] to it[1] }
    }

    println(solve(n, t, ksList))
}

fun solve(n: Int, t: Int, ksList: Array<Pair<Int, Int>>): Int {
    val dp = Array(n+1){ Array(t+1){ 0 } }
    for(y in 1..n) for(x in 1..t)
    {
        if(x >= ksList[y].first) dp[y][x] = max(dp[y-1][x], dp[y-1][x-ksList[y].first]+ksList[y].second)
        else dp[y][x] = dp[y-1][x]
    }

    return dp[n][t]
}
