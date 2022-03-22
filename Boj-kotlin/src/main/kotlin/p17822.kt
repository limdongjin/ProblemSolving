package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader



private enum class Direction(
    val dx: Int,
    val dy: Int
) {
    UP(-1, 0),
    RIGHT(0, 1),
    DOWN(1, 0),
    LEFT(0, -1);

    companion object {
        val values = Direction.values()
    }
}



private fun main(){
    for(d in Direction.values()){
        println(d.dy to d.dx)
    }
}


private fun IntArray.getSafeIndex(index: Int): Int {
    return (index%size).run {
        when{
            this < 0 -> size + this
            else -> this%size
        }
    }
}

private fun solve(board: Array<IntArray>, xdkList: Array<IntArray>): Int{
    val (n, m) = board.size to board[0].size

    val boardDir = Array(n+1){0}
    for((xi, di, ki) in xdkList){

        // 회전
        for(y in xi..n step xi) {
            boardDir[y-1] = boardDir[y-1].plus(when (di) {
                0 -> ki
                else -> -ki
            })
            if(boardDir[y-1] >= 0) boardDir[y-1] %= m
            else boardDir[y-1] = -((-boardDir[y-1])%m)
        }

        val deletedList = mutableSetOf<Pair<Int, Int>>()
        // 같은 행 끼리 검사
        for (y in 0 until n) for (x in 1 until  m){
            if(board[y][x] != 0 && board[y][x] == board[y][x-1]) {
                deletedList.add(y to x)
                deletedList.add(y to x-1)
            }
        }
        // 1열과 m열 비교
        for(y in 0 until  n)
            if(board[y][0] != 0 && board[y][0] == board[y][m-1]){
                deletedList.add(y to 0)
                deletedList.add(y to m-1)
            }


        // 인접한 열 검사
        for(x in 0 until m) for(y in 0 until n-1){
            val diff = (boardDir[y] - boardDir[y+1])%(m)

            val index2 = board[y+1].getSafeIndex(x+diff)

            if(board[y][x] != 0 && board[y][x] == board[y+1][index2]){
                deletedList.add(y to x)
                deletedList.add(y+1 to index2)
            }
        }

        // 인접하면서 수가 같은 것이 없는 경우.
        if(deletedList.isEmpty()){
            val average = board.sumOf { row -> row.sum().toDouble() }
                                .div(board.sumOf { it.count { cell -> cell != 0 } }.toDouble())

            for(y in 0 until  n) for(x in 0 until m)
                board[y][x] += when {
                    board[y][x] == 0 -> 0
                    board[y][x].toDouble() > average -> -1
                    board[y][x].toDouble() < average -> 1
                    else -> 0
                }

            continue
        }

        // 수를 지워주자.
        for ((y, x) in deletedList)
            board[y][x] = 0
    }

    return board.sumOf { it.sum() }
}
/*
private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (n, m, t) = readLine()!!.split(" ").map { it.toInt() }
    val board = Array(n){ IntArray(m){0}}

    (0 until n).forEach { y ->
        readLine()!!.split(" ")
            .map { it.toInt() }
            .forEachIndexed { x, v ->
                board[y][x] = v
            }
    }

    val xdkList = (1..t).map {
        readLine()!!.split(" ").map { it.toInt() }.toIntArray()
    }.toTypedArray()

    println(solve(board, xdkList))
}
*/