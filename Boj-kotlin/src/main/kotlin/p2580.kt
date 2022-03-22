package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.system.exitProcess

private class Infos {
    val board: Array<IntArray>
    val row = Array(10) { BooleanArray(10) { false } }
    val col = Array(10) { BooleanArray(10) { false } }
    val square = Array(10) { BooleanArray(10) { false } }

    init {
        board = (1..9)
            .map { readLine()!!.toCharArray().map { it - '0' }.toIntArray() }
            .toTypedArray()
        initOthers()
    }

    private fun initOthers() {
        for (y in board.indices) for (x in board[0].indices) if (board[y][x] != 0) {
            row[y][board[y][x]] = true
            col[x][board[y][x]] = true
            square[(y / 3) * 3 + (x / 3)][board[y][x]] = true
        }
    }

}


private fun dfs(cnt: Int, infos: Infos): Unit = with(infos){
    val x = cnt / 9
    val y = cnt % 9

    if(cnt == 81) {
        for(yy in board.indices)
            println(board[yy].joinToString(""))
        exitProcess(0)
    }

    if(board[x][y] == 0){
        for(i in (1..9)){
            if(!row[x][i] && !col[y][i] && !square[(x/3)*3+(y/3)][i]){
                row[x][i] = true
                col[y][i] = true
                square[(x/3)*3 + (y/3)][i] = true
                board[x][y] = i
                dfs(cnt+1, infos)
                board[x][y] = 0
                row[x][i] = false
                col[y][i] = false
                square[(x/3)*3 + (y/3)][i] = false
            }
        }
    }else dfs(cnt+1, infos)

    return
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val infos = Infos()

    dfs(0, infos)

}