package main.kotlin.p1522

import java.io.BufferedReader
import java.io.InputStreamReader

private fun solve(s: String): Int {
    val arr: List<Char> = s.toList()
    val aCnt = arr.count { it == 'a' }.takeIf { it != 0 } ?: return 0

    val ans = arr.windowed(aCnt, partialWindows = true)
        .map {
            when(val diff = aCnt - it.size){
                0 -> it
                else -> it + arr.subList(0, diff)
            }
        }
        .minOf { window -> window.count { it == 'b' } }

    return ans
}


fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
//    run {
//        val testSet = mapOf(
//            "abababababababa" to 3,
//            "ba" to 0,
//            "aaaabbbbba" to 0,
//            "abab" to 1,
//            "aabbaaabaaba" to 2,
//            "aaaa" to 0
//        )
//        testSet.forEach { require(solve(it.key) == it.value) }
//    }

    val s = readLine()
    println(solve(s))
}

