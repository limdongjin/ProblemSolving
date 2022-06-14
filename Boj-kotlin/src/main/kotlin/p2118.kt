package main.kotlin

import kotlin.math.max
import kotlin.math.min

fun main(){
    val n = readln().toInt()
    val board = Array (n) {
        readln().toInt()
    } + 0

    println(solve(n, board))
}

fun solve(n: Int, board: Array<Int>): Int {
    val s = board.sum()
    var low = 0
    var high = 0
    var ret = 0
    var now = board[low]

    while (high in low until n) {
        val minNow = min(now, s-now)
        ret = max(ret, minNow)

        if (now == minNow) {
            high++
            now += board[high]
        } else {
            now -= board[low]
            low++
        }
    }

    return ret
}