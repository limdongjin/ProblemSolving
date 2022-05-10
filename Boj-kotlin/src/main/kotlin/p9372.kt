package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val t = readLine().toInt()

    repeat(t) {
        val (n, m) = readLine().split(" ").map(String::toInt)
        repeat(m) { readLine() }
        println(n-1)
    }

}