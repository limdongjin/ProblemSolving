package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.LinkedList

import java.util.Queue
import kotlin.math.abs
import kotlin.math.min

private val moveDir = listOf(
    1 to 0,
    -1 to 0,
    0 to -1,
    0 to 1,
)

private fun labeling(pos: Pair<Int, Int>, id: Int, board: Array<Array<Int>>, edges: ArrayList<Pair<Int, Int>>){
    val q: Queue<Pair<Int, Int>> = LinkedList()
    q.offer(pos)
    while (!q.isEmpty()){
        var edge = false
        val (y, x) = q.poll()
        board[y][x] = id
        for((dy, dx) in moveDir){
            val ny = y+dy
            val nx = x+dx
            if(ny !in board.indices || nx !in board.indices)
                continue
            if(board[ny][nx] < 0){
                board[ny][nx] = id
                q.offer(ny to nx)
            }else if(board[ny][nx] == 0) edge = true
        }
        if(edge) edges.add(y to x)
    }
}

private fun calcAns(board: Array<Array<Int>>, edges: ArrayList<Pair<Int, Int>>): Int {
    var ans = 987654321

    for(i in edges.indices) for(j in i+1 until edges.size){
        val (y, x) = edges[i]
        val (ny, nx) = edges[j]
        if(board[y][x]>0 && board[ny][nx]>0 && board[y][x] != board[ny][nx])
            ans = min(ans, abs(y-ny) + abs(x-nx)-1)
    }

    return ans
}

private fun solve(board: Array<Array<Int>>): Int{
    val edges = ArrayList<Pair<Int, Int>>()

    for(y in board.indices) for(x in board.indices)
        if(board[y][x] != 0)
            board[y][x] = -1

    var lab = 1
    for(y in board.indices) for(x in board.indices)
        if(board[y][x] < 0)
            labeling(y to x, lab++, board, edges)

    return calcAns(board, edges)

}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine().toInt()
    val board = (1..n).map {
        readLine().split(" ").map { it.toInt() }.toTypedArray()
    }.toTypedArray()

    println(solve(board))
}