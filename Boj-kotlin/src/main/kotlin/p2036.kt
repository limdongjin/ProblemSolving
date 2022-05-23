package main.kotlin.p2036

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine()!!.toInt()
    val seq = LongArray(n) { readLine()!!.toLong() }

    println(solve(n, seq))
}

fun solve(n: Int, seq: LongArray): Long {
    return seq.sorted().takeIf { it.size != 1 }?.let {
        var next2 = it[n-1]                                     // dp[n-1]
        var next  = max(it[n-2]+it[n-1], it[n-2]*it[n-1]) // dp[n-2]
        var ans = next

        (n-3 downTo 0).forEach { k ->
            // Equivalent:
            //   dp[k] : (k 번째 요소 ~ 마지막 요소) 수열로 얻을 수 있는 최대 점수 총 합
            //   dp[k] = max(it[k]+dp[k+1], it[k]*it[k+1]+dp[k+2])

            ans = max(it[k]+next, it[k]*it[k+1]+next2)
            next2 = next
            next = ans
        }

        ans
    } ?: seq[0]
}

