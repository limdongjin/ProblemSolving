package main.kotlin.p2281

import java.lang.Math.pow
import kotlin.math.min
import kotlin.system.exitProcess

const val INF = 987654321

fun main() = with(System.`in`.bufferedReader()){
    val (n, m) = readLine()!!.split(" ").map(String::toInt)
    val names = List(n){ readLine()!!.toInt() }

    println(solve(n, m, names))
}

fun solve(n: Int, m: Int, names: List<Int>): Int {
    val dp = IntArray(n+1) { INF }
    dp[n-1] = 0


    go(dp, names, n, m, 0)

    return dp[0]
}

fun go(dp: IntArray, names: List<Int>, n: Int, m: Int, idx: Int): Int {
    if(dp[idx] < INF) return dp[idx]
    var remain = m - names[idx]

    for(i in (idx+1)..n){
        if(remain < 0) break
        if(i == n){
            dp[idx] = 0
            break
        }

        dp[idx] = min(dp[idx], remain*remain + go(dp, names, n, m, i))
        remain -= names[i] + 1
    }
    return dp[idx]
}

// TODO 다시 제출해보기
//fun calcSpace(names: List<Int>, m: Int, fromIndex: Int, toIndex: Int): Int =
//    names.subList(fromIndex, toIndex)
//            .let { m - it.sum() - (it.size - 1) }
//            .takeIf { it >= 0 }
//            ?.let { it*it }
//        ?: INF
//
//fun solve(n: Int, m: Int, names: List<Int>): Int {
//    val calc = { from: Int, to: Int -> calcSpace(names, m, fromIndex = from, toIndex = to) }
//    return names.indices.map { if(calc(it, n) == INF) -1 else 0 }
//        .takeIf { it.contains(-1) }
//        ?.toIntArray()
//        ?.let { dp ->
//            val range = dp.lastIndexOf(-1).takeIf { it != -1 }!! downTo 0
////            println(range)
////            println(dp.toList())
//            range.forEach { k ->
//                dp[k] = (k+1 until n-1).minOfOrNull { u ->
//                    calc(k, u) + dp[u]
//                } ?: ((m-names[k])+dp[k+1]).let { it*it }
//            }
////            println(dp.toList())
//            dp[0]
//        }
//    ?: 0
//}

