package main.kotlin.p2140

import java.io.BufferedReader
import java.io.InputStreamReader

val directions = listOf(
    -1 to 0,
    -1 to 1,
    0 to 1,
    1 to 1,
    1 to 0,
    1 to -1,
    0 to -1,
    -1 to -1
)

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine().toInt()
    val board = Array(n){ readLine().toCharArray().toTypedArray() }

    println(solve(board))
}

fun solve(board: Array<Array<Char>>): Int{
    val n = board.size
    var ret = 0
    for(y in 1..n-2) for(x in 1..n-2) {
        var flag = true
        directions.forEach { (dy, dx) ->
            val ny = y + dy; val nx = x + dx
            if(board[ny][nx] == '0'){
                board[y][x] = ' '
                flag = false
            }
        }
        if(flag) directions.forEach { (dy, dx) ->
            val ny = y + dy; val nx = x + dx
            if(board[ny][nx] in '1'..'3') board[ny][nx]--
        }
    }

    for(y in 1..n-2) for(x in 1..n-2)
        if(board[y][x] == '#')
            ret++

    return ret
}
