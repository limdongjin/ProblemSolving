package main.kotlin.p11497

import kotlin.math.abs
import kotlin.math.max

fun main() = with(System.`in`.bufferedReader()){
    repeat(readLine().toInt()){
        val n = readLine().toInt()
        val l = readLine().split(" ").map(String::toInt)
        println(solve(n, l))
    }
}

fun solve(n: Int, l: List<Int>): Int {
    return l.sorted().withIndex()
        .partition { it.index % 2 == 0 }
        .let { it.first.map { v -> v.value } + it.second.map { v -> v.value }.reversed() }
        .let(::calc)
}

fun calc(lst: List<Int>): Int {
    return max(lst.windowed(2).maxOf { abs(it[0] - it[1]) }, abs(lst.first()-lst.last()))
}
