package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.LinkedList

val dy = listOf(0, 0, 1, -1)
val dx = listOf(1, -1, 0, 0)
val isInRange = { v: Int, end: Int -> (0 <= v) and (v < end) }

private fun bfs(board: List<MutableList<Int>>,
                pos: Pair<Int, Int>, id: Int): Int {
    when(board[pos.first][pos.second]){
        0 -> board[pos.first][pos.second] = id
        -1 -> return id
        else -> return id
    }

    val q = LinkedList<Pair<Int, Int>>().apply { offer(pos) }

    while(q.isEmpty().not()) with(q.poll()){
        (dy zip dx)
            .asSequence()
            .map { d -> (first + d.first) to (second + d.second) }
            .filter {
                isInRange(it.first, board.size) and
                        isInRange(it.second, board[0].size)
            }
            .filter { board[it.first][it.second] == 0 }
            .forEach {
                q.offer(it.first to it.second)
                board[it.first][it.second] = id
            }
    }

    return id+1
}

private fun solve(board: Array<Array<Int>>){
    val positions = board.indices.asSequence().flatMap {
        board[it].indices.map { c -> it to c }
    }.filter { (y, x) -> board[y][x] == 1 }.toList()

    val board2 = board.map {
            row -> row.map { it - 1 }.toMutableList()
    }

    var id = 1
    positions.forEach { id = bfs(board2, it, id) }

    board2
        .asSequence()
        .flatten()
        .filter { it != -1 && it != 0 }
        .groupingBy { it }.eachCount()
        .also {
            println(it.size)
            println(it.maxOfOrNull { p -> p.value }?:0)
        }
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (h, _) = readInts()
    val board = (1..h).map { readInts() }.toTypedArray()
    solve(board)
}

private fun BufferedReader.readInts(): Array<Int> {
    return readLine().split(" ").map {it.toInt()}.toTypedArray()
}