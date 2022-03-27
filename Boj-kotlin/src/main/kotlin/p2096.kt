package main.kotlin.p2096

import kotlin.math.max
import kotlin.math.min

fun solve(board: List<List<Int>>): Pair<Int, Int>{
    // maxDp[y][x] :  (y, x) 에서 끝났을때, 얻은 최대 점수
    // minDp[y][x] :  (y, x) 에서 끝났을때, 얻은 최소 점수

    val n = board.size
    val maxDp = Array(n){Array(3){-1}}.apply {
        (0 until 3).forEach { this[0][it] = board[0][it] }
    }

    val minDp = Array(n){Array(3){-1}}.apply {
        (0 until 3).forEach { this[0][it] = board[0][it] }
    }

    for(y in 1 until n){
        maxDp[y][0] = max(maxDp[y-1][0], maxDp[y-1][1]) + board[y][0]
        maxDp[y][1] = maxDp[y-1].maxOrNull()!! + board[y][1]
        maxDp[y][2] = max(maxDp[y-1][1], maxDp[y-1][2]) + board[y][2]

        minDp[y][0] = min(minDp[y-1][0], minDp[y-1][1]) + board[y][0]
        minDp[y][1] = minDp[y-1].minOrNull()!! + board[y][1]
        minDp[y][2] = min(minDp[y-1][1], minDp[y-1][2]) + board[y][2]
    }

    return maxDp[n-1].maxOrNull()!! to minDp[n-1].minOrNull()!!
}

fun main(){
    val n = readln().toInt()
    val board = List(n) {
        readln().split(" ").map(String::toInt)
    }

    val (maxScore, minScore) = solve(board)
    println("$maxScore $minScore")
}