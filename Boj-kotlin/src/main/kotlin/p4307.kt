package main.kotlin.p4307

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max
import kotlin.math.min

// 4307 개미

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val t = readLine().toInt()
    repeat(t) {
        val (l, n) = readLine().split(" ").map(String::toInt)
        val ants = Array(n){ readLine().toInt() }

        solve(l, ants).let { (a, b) -> println("$a $b") }
    }

}

fun solve(l: Int, ants: Array<Int>): Pair<Int, Int> =
    ants.maxOf { min(it, l-it) } to ants.maxOf { max(it, l-it) }