package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.sqrt

private fun solve(x: Int, y: Int): Int{
    if(y == x) return 0
    val dif = y-x
    val n = sqrt(dif.toDouble()).toInt()
    return when {
        n*n == dif -> 2*n-1
        dif-n*n <= n -> 2*n
        else -> 2*n+1
    }
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (x, y) = readLine().split(' ').map { it.toInt() }

    println(solve(x, y))
}