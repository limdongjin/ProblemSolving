package main.kotlin.p1303

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.LinkedList
import java.util.Queue

private val dirs = listOf(
    -1 to 0,
    0 to 1,
    1 to 0,
    0 to -1
)

fun solve(board: Array<Array<Char>>): String {
    val n = board.size
    val m = board[0].size
    val whiteOrBlack = mutableMapOf('W' to 0, 'B' to 0)

    val visited = Array(n) { Array(m) { false } }

    for(y in board.indices) for(x in board[0].indices) if(!visited[y][x]) {
        val number = bfs(pos = y to x, board = board, visited = visited)

        whiteOrBlack[board[y][x]] = whiteOrBlack[board[y][x]]!! + number*number
    }

    return "${whiteOrBlack['W']} ${whiteOrBlack['B']}"
}

fun bfs(pos: Pair<Int, Int>, board: Array<Array<Char>>, visited: Array<Array<Boolean>>): Int {
    var ans = 1
    val queue: Queue<Pair<Int, Int>> = LinkedList()
    val rangePredicate: (Pair<Int, Int>) -> Boolean = { it.first in board.indices && it.second in board[0].indices }
    val visitPredicate: (Pair<Int, Int>) -> Boolean = { visited[it.first][it.second] }
    val colorPredicate: (Pair<Int, Int>) -> Boolean = { board[it.first][it.second] == board[pos.first][pos.second] }

    queue.offer(pos.first to pos.second)
    visited[pos.first][pos.second] = true

    while (queue.isNotEmpty()){
        val (y, x) = queue.poll()

        dirs.forEach { (dy, dx) ->
            val newPos = (y+dy to x+dx).takeIf(rangePredicate) ?: return@forEach
            if(!visitPredicate(newPos) && colorPredicate(newPos)) {
                visited[newPos.first][newPos.second] = true
                queue.offer(newPos)
                ans++
            }
        }
    }

    return ans
}

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (_, n) = readLine().split(" ").map(String::toInt)
    val board = Array(n) { readLine().toCharArray().toTypedArray() }

    println(solve(board))
}