package main.kotlin.p9252

import kotlin.math.max

fun main() = with(System.`in`.bufferedReader()){
    val a = readLine()
    val b = readLine()

    val ans = lcsWithString(a, b).let {
        if(it.first == 0) it.first else "${it.first}\n${it.second}"
    }
    println(ans)
}

fun lcsWithString(a: String, b: String): Pair<Int, String> {
    val dp = Array(a.length+1) { IntArray(b.length+1) }

    for(xi in 1..a.length) for(yi in 1..b.length){
        dp[xi][yi] = when(a[xi-1] == b[yi-1]){
            true -> dp[xi-1][yi-1] + 1
            false -> max(dp[xi-1][yi], dp[xi][yi-1])
        }
    }

    val lcsStr = run {
        var xi = a.length; var yi = b.length
        val ret = ArrayDeque<Char>()
        while(xi > 0 && yi > 0){
            when(dp[xi][yi]){
                dp[xi-1][yi] -> xi--
                dp[xi][yi-1] -> yi--
                else -> { xi--; yi--; ret.addFirst(a[xi]) }
            }
        }
        ret.joinToString("")
    }

    return dp[a.length][b.length] to lcsStr
}
