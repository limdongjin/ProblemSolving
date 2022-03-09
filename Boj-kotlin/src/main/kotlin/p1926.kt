package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.LinkedList

private val moveDir = listOf(
    0 to 1,
    0 to -1,
    1 to 0,
    -1 to 0
)

private fun bfs(board: Array<Array<Int>>,
                pos: Pair<Int, Int>, id: Int): Int {
    // 빈칸이거나 이미 라벨링된 그림이면, return
    if (board[pos.first][pos.second] != 0) return id

    board[pos.first][pos.second] = id
    val q = LinkedList<Pair<Int, Int>>().apply { offer(pos) }

    while(!q.isEmpty()) with(q.poll()) {
        moveDir
            .asSequence()
            .map { (dy, dx) -> first+dy to second+dx } // => (nextY, nextX)
            .filter { (y, x) -> y in board.indices && x in board[0].indices } // is valid range?
            .filter { (y, x) -> board[y][x] == 0 } // Is unlabeled pic?
            .forEach {
                q.offer(it)
                board[it.first][it.second] = id // labelling
            }
    }

    return id+1 // next label id
}

private fun solve(board: Array<Array<Int>>){
    // 1 이 있는 좌표를 저장
    val positions = board.flatMapIndexed { y, row ->
        row
            .filter{ cell -> cell == 1 }
            .map { x -> y to x }
    }

    // 데이터 정규화
    for (y in board.indices) for(x in board.indices)
        board[y][x] -= 1
    // => 빈칸: -1 || 그림: 0

    // 라벨링
    var id = 1 // id: 그림 라벨
    positions.forEach { id = bfs(board, it, id) }

    // 그림의 개수, 가장 넓은 그림의 넓이를 구한다.
    board
        .flatten()
        .asSequence()
        .filter { it > 0 }
        .groupingBy { it }.eachCount() // ex, {1: 4, 2: 2, 3: 9, 4: 1}
        .also {
            println(it.size) // 그림의 개수 : key 의 개수
            println(it.maxOfOrNull { p -> p.value }?:0) // 가장 넓은 그림의 넓이 : max value
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