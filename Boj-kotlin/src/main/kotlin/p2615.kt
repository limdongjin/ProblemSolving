package main.kotlin.p2615

import java.io.BufferedReader
import java.io.InputStreamReader

val board = Array(21) { IntArray(21) }
val cache = Array(21) { Array(21) { IntArray(4) } }
val dy = intArrayOf(0, 1, 1, 1)
val dx = intArrayOf(1, 1, 0, -1)


fun main(args: Array<String>) = with(BufferedReader(InputStreamReader(System.`in`))) {
    for (i in 1..19) {
        val str = readLine().split(" ").map { it.toInt() }
        for (j in 1..19) {
            board[i][j] = str[j - 1]
        }
    }

    println(solve())
}

fun solve(): String {
    for (y in 1..19)  for (x in 1..19) {
        if(board[x][y] == 0) continue

        // 현재 위치 (x, y) 에서 방향 d 로  이동. 다른말이 나올때 까지
        for (d in 0..3) if (cache[x][y][d] == 0 && go(x, y, d, board[x][y]) == 5) {
            return "${board[x][y]}\n$x $y"
        }
    }

    return "0"
}


fun go(x: Int, y: Int, dir: Int, color: Int): Int {
    val nx = x + dx[dir]
    val ny = y + dy[dir]

    if (board[nx][ny] == color) // 같은 색이므로 이동
        return go(nx, ny, dir, color) + 1.also { cache[nx][ny][dir] = it }
    else return 1 // 다른색이므로 1 리턴 (이동 종료)
}