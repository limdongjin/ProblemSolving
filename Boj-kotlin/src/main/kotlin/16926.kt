package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.min

// 배열 돌리기 1

private fun Array<IntArray>.print2D(){
    this.forEach { println(it.joinToString(" ")) }
}

private fun findStartingIndex(rotate: Int, mm: Int, nn: Int): Pair<Int, Int>{
    var cnt = 0
    var ansY = 0
    var ansX = 0
    while(cnt < rotate) {
        when (cnt) {
            in 0..mm - 2 -> ansX++
            in mm - 1..mm - 3 + nn -> ansY++
            in mm + nn - 2..2 * mm + nn - 4 -> ansX--
            in 2 * mm + nn - 3..2 * mm + 2 * nn - 4 -> ansY--
        }
        cnt++
    }
    val ret = ansY to ansX

    return ret
}

private fun solve(board: List<List<Int>>, r: Int){
    val (n, m) = board.size to board[0].size
    val ansBoard = board.map {
        it.toIntArray()
    }.toTypedArray()
    val minNM = min(n, m)
    // N*M -> (N-2)*(M-2) -> ....
    for(level in 0 until (minNM/2)){
        val nn = n-2*level
        val mm = m-2*level

        // 이 level 의 총 길이
        val levelLeng = 2*nn+2*mm-4
        val rr = r % (levelLeng)


        // find index
        val firstPos = findStartingIndex(rotate = rr, mm = mm, nn = nn)

        // move and fill
        var cnt = 0
        var curY = level+firstPos.first
        var curX = level+firstPos.second
        var ansY = level
        var ansX = level

        while(cnt < levelLeng) {
            ansBoard[ansY][ansX] = board[curY][curX]

            if (curY == level && curX != level+mm-1) {
                curX++ // 위
            }else if(curX == level+mm-1 && curY != level+nn-1){
                curY++ // 오른쪽
            }else if(curY == level+nn-1 && curX != level){
                curX--  // 아래
            }else if(curX == level){
                curY--  // 왼쪽
            }
//            else{
//                throw Exception("error")
//            }

            when (cnt) {
                in 0..mm-2 -> ansX++
                in mm-1..mm-3+nn -> ansY++
                in mm+nn-2..2*mm+nn-4 -> ansX--
                in 2*mm+nn-3..2*mm+2*nn-4 -> ansY--
            }

            cnt++
        }

    }

    ansBoard.print2D()

    return
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (n, m, r) = readLine()!!.split(" ").map { it.toInt() }
    val board = (1..n).map {
        readLine()!!.split(" ").map { it.toInt() }
    }

    solve(board, r)
}
