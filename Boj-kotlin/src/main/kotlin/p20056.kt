package main.kotlin.p20056

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

private data class Ball(var m: Int, var s: Int, var d: Int)
private val directions = listOf(
    -1 to 0,
    -1 to 1,
    0 to 1,
    1 to 1,
    1 to 0,
    1 to -1,
    0 to -1,
    -1 to -1
)

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, m, k) = readLine().split(" ").map(String::toInt)
    val fireballsInput = List(m) { readLine().split(" ").map(String::toInt) }

    println(solve(n, m, k, fireballsInput))
}

fun solve(n: Int, m: Int, k: Int, fireBallsInput: List<List<Int>>): Int {
    val board = Array <Array<Queue<Ball>>> (n){ Array(n) { LinkedList() } }
        .apply {
            fireBallsInput.forEach { (r, c, m, s, d) ->
                this[r-1][c-1].offer(Ball(m=m, s=s, d=d))
            }
        }
    val sizeBoard = Array(n) { y ->
        Array(n) { x ->
            board[y][x].size
        }
    }
    val updatesSizeBoard = {
        for (y in board.indices) for (x in board[y].indices) {
            sizeBoard[y][x] = board[y][x].size
        }
    }
    val moves = {
        for (y in board.indices) for (x in board[y].indices) {
            repeat(sizeBoard[y][x]) {
                val ball = board[y][x].poll()
                val (ny, nx) = calcNextPosition(y to x, ball, n = board.size)
                board[ny][nx].offer(ball)
            }
        }
        updatesSizeBoard()
    }

    val afterMoves = {
        for(y in sizeBoard.indices) for(x in sizeBoard[y].indices) {
            if(sizeBoard[y][x] < 2) continue

            val balls = List(sizeBoard[y][x]) { board[y][x].poll() }
            val newM = balls.sumOf(Ball::m) / 5
            val newS = balls.sumOf(Ball::s) / sizeBoard[y][x]
            val dirFlag = balls.all { it.d % 2 == 0 } || balls.all { it.d % 2 == 1 }

            when {
                newM == 0 -> {}
                dirFlag -> {
                    board[y][x].offer(Ball(newM, newS, 0))
                    board[y][x].offer(Ball(newM, newS, 2))
                    board[y][x].offer(Ball(newM, newS, 4))
                    board[y][x].offer(Ball(newM, newS, 6))
                }
                else -> {
                    board[y][x].offer(Ball(newM, newS, 1))
                    board[y][x].offer(Ball(newM, newS, 3))
                    board[y][x].offer(Ball(newM, newS, 5))
                    board[y][x].offer(Ball(newM, newS, 7))
                }
            }
            sizeBoard[y][x] = board[y][x].size
        }
    }

    repeat(k) {
        moves()
        afterMoves()
    }

    return board.sumOf { row ->
        row.sumOf { q -> q.sumOf(Ball::m) }
    }
}

private fun calcNextPosition(curPos: Pair<Int, Int>, ball: Ball, n: Int): Pair<Int, Int> {
    val position: (Int) -> Int = {
        when (it < 0) {
            true -> (it % n + n) % n
            else -> it % n
        }
    }

    val ny = position(curPos.first + ball.s * directions[ball.d].first)
    val nx = position(curPos.second + ball.s * directions[ball.d].second)

    return ny to nx
}