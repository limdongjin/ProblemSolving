package main.kotlin.p19539

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine()!!.toInt()
    val h = readLine()!!.split(" ").map(String::toInt)

    println(if(solve(n, h)) "YES" else "NO")
}

fun solve(n: Int, h: List<Int>): Boolean =
    (h.sumOf { it % 2 } to h.sumOf { it / 2 }).run {
        (second - first)%3 == 0 && second >= first
    }