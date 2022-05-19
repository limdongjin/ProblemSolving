package main.kotlin.p11048

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.Arrays

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, m) = readLine().split(" ").map(String::toInt)
    val board = Array(n) {
        readLine().split(" ").map(String::toInt).toTypedArray()
    }

    println(Solver(board, n, m).solve())
}

class Solver(val board: Array<Array<Int>>, val n: Int, val m: Int){
    // dp[y][x][direction]
    val dp = Array(n){ Array(m) { Array(3){ -1 } } }
    val end = n-1 to m-1

    fun solve(): Int {
        dirs.forEachIndexed { i, (dy, dx) ->
            dp[0][0][i] = go(0+dy to 0+dx, i) + board[0][0]
        }

        return dp[0][0].maxOrNull()!!
    }

    fun go(pos: Pair<Int, Int>, dir: Int): Int = with(pos){
        if(first !in board.indices || second !in board[0].indices)
            return 0
        if(pos == end)
            return board[first][second]

        dirs.forEachIndexed { i, (dy, dx) ->
            if(dp[first][second][i] == -1) {
                dp[first][second][i] = board[first][second]
                dp[first][second][i] += go(first + dy to second + dx, i)
            }
        }

        return dp[first][second].maxOrNull()!!
    }

    companion object {
        val dirs = listOf(
            1 to 0, // up
            0 to 1, // right
            1 to 1// diag
        )
    }

}