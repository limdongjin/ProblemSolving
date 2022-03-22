package main.kotlin.p9507

import java.io.BufferedReader
import java.io.InputStreamReader

// Generations of Tribbles

private fun makeKoongs(): Array<Long> {
    val koongs = Array(68) { 0L }.apply {
            this[0] = 1
            this[1] = 1
            this[2] = 2
            this[3] = 4
        }

    with(koongs) {
        for(i in 4..67)
            set(i, slice(i-4 until i).sum())
    }

    return koongs
}

private fun solve(numbers: List<Int>){
    val koongs = makeKoongs()

    numbers
        .joinToString("\n") { num -> koongs[num].toString() }
        .also { println(it) }
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val tc = readLine()!!.toInt()
    val numbers = (1..tc).map { readLine()!!.toInt() }

    solve(numbers)
}