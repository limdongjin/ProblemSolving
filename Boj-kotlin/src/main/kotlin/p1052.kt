package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader

private fun solve(n: Int, k: Int): Int{
    if(n <= k) return 0
    // 2^24 = 16,777,216
    val twoPows = generateSequence(1) { it*2 }
        .take(25)
    var curN = n
    var curK = k

    while(curN > 0 && curK > 1 && curN > curK){
        curN -= twoPows.findLast { it <= curN }!!
        curK--
    }
    if(curN <= curK) return 0
    // assert(curK == 1)

    val ret = twoPows.find { it >= curN }!!.minus(curN)

    return ret
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (n, k) = readLine().split(' ').map {it.toInt()}
    println(solve(n, k))

    // 15,868 = 2^15-(1000000-2^19-2^18-2^17-2^16)
}