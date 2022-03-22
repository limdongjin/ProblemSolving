package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader

private fun solve(board: List<List<Int>>, positions: List<List<Int>>): Unit {
    val h = board.size
    val w = board[0].size

    // make sumBoard
    val sumBoard = Array(h+1){Array(w+1){0}}
    for(y in 0 until h) for (x in 0 until w)
        sumBoard[y+1][x+1] = board[y][x]

    for(y in 1..h) {
        var rowSum = 0
        for (x in 1..w) {
            sumBoard[y][x] += sumBoard[y - 1][x] + rowSum
            rowSum += board[y-1][x-1]
        }
    }

    // solve
    val st = StringBuilder()

    for (pos in positions) {
        val start = pos[0] to pos[1]
        val end = pos[2] to pos[3]

        sumBoard[end.first][end.second]
            .minus(sumBoard[start.first-1][end.second])
            .minus(sumBoard[end.first][start.second-1])
            .plus(sumBoard[start.first-1][start.second-1])
            .also {
                st.appendLine(it)
            }
    }

    println(st.toString())
}


private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (n, _) = readLine().split(' ').map { it.toInt() }
    val board = (1..n).map {
        readLine().split(' ').map { it.toInt() }
    }

    val positions = (1..readLine().toInt()).map {
            readLine().split(' ').map { it.toInt() }
    }

    solve(board, positions)
}