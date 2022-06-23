package main.kotlin.p4179

import java.util.LinkedList
import java.util.Queue

val dirs = listOf(
    1 to 0,
    0 to 1,
    -1 to 0,
    0 to -1
)

fun main() = with(System.`in`.bufferedReader()){
    val (n, m) = readLine().split(" ").map(String::toInt)
    val board = Array(n) { readLine().toCharArray() }

    val ans = solve(n, m, board)
    if(ans == -1){
        println("IMPOSSIBLE")
    }else{
        println(ans)
    }
}

fun solve(n: Int, m: Int, board: Array<CharArray>): Int {
    val visitJ = Array(n) { Array(m){ -1 } }
    val visitF = Array(n) { Array(m){ -1 } }
    val qJ: Queue<Pair<Int, Int>> = LinkedList()
    val qF: Queue<Pair<Int, Int>> = LinkedList()

    for(y in board.indices){
        for(x in board[0].indices){
            when(board[y][x]){
                'F' -> {
                    qF.offer(y to x)
                    visitF[y][x] = 0
                }
                'J' -> {
                    qJ.offer(y to x)
                    visitJ[y][x] = 0
                }
            }
        }
    }

    while (qF.isNotEmpty()){
        val f = qF.poll()
        dirs.forEach { (dy, dx) ->
            val ny = (f.first + dy).takeIf { it in board.indices } ?: return@forEach
            val nx = (f.second + dx).takeIf { it in board[0].indices } ?: return@forEach
            if(visitF[ny][nx] >= 0 || board[ny][nx] == '#') return@forEach

            visitF[ny][nx] = visitF[f.first][f.second] + 1
            qF.offer(ny to nx)
        }
    }

    while (qJ.isNotEmpty()){
        val j = qJ.poll()
        dirs.forEach { (dy, dx) ->
            val ny = (j.first + dy)
            val nx = (j.second + dx)
            if(ny < 0 || ny >= n || nx < 0 || nx >= m){
                return visitJ[j.first][j.second]+1
            }
            if(visitJ[ny][nx] >= 0 || board[ny][nx] == '#') return@forEach
            if(visitF[ny][nx] != -1 && visitF[ny][nx] <= visitJ[j.first][j.second] + 1) return@forEach

            visitJ[ny][nx] = visitJ[j.first][j.second] + 1
            qJ.offer(ny to nx)
        }
    }

    return -1
}

