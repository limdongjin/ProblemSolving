package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader

private fun check_bingo(visited: Array<BooleanArray>): Boolean {
    with(visited){
        val row_bingo = count {row -> row.all { it }}
        val col_bingo = indices
            .count { colIdx ->
                indices
                    .map { this[it][colIdx] }
                    .all { it }
            }
        fun Boolean.toInt() = if (this) 1 else 0
        val diagBingo = indices.all { this[it][it] }.toInt()
            .plus(indices.all { this[it][size-it-1] }.toInt())

        return (row_bingo + col_bingo + diagBingo) >= 3

    }
}

private fun solve(board: List<List<Int>>, nums: List<Int>): Int {
    val posOfValue = board.flatMapIndexed { y, row ->
        row.mapIndexed { x, value -> Pair(value, Pair(y, x)) }
    }.toMap()
    val visited = Array(board.size){BooleanArray(board.size)}

    for ((i, v) in nums.withIndex()){
        val (y, x) = posOfValue[v]!!
        visited[y][x] = true
        if(check_bingo(visited)) return i+1
    }

    return -1
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val board = (1..5).map {
        readLine().split(" ").map { it.toInt() }
    }
    val nums = (1..5).flatMap {
        readLine().split(" ").map { it.toInt() }
    }

    println(solve(board, nums))
}