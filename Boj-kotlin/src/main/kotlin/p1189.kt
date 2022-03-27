package main.kotlin.p1189

private var directions = listOf( //u, r, d, l
    -1 to 0,
    0 to 1,
    1 to 0,
    0 to -1
)

// 1189 컴백홈
fun go(board: Array<Array<Int>>, pos: Pair<Int, Int>, kk: Int): Int{
    if(kk == 1)
        return if(pos == Pair(0, board[0].size-1)) 1 else 0

    val nextPredicate: (Pair<Int, Int>) -> Boolean =
        { it.first in board.indices && it.second in board[0].indices
                && board[it.first][it.second] == 0 }

    var ret = 0
    for((dy, dx) in directions){
        val nextPos = Pair(pos.first + dy, pos.second + dx)
            .takeIf(nextPredicate) ?: continue

        board[nextPos.first][nextPos.second] = 1
        ret += go(board, nextPos, kk-1)
        board[nextPos.first][nextPos.second] = 0
    }
    return ret
}

fun solve(board: Array<Array<Int>>, k: Int): Int{
    board[board.size-1][0] = 1
    return go(board, board.size-1 to 0, k)
}

fun main(){
    val (r, _, k) =  readLine()!!.split(" ").map(String::toInt)
    val board = Array(r){
        readLine()!!.toCharArray().map { if(it == '.') 0 else -1 }.toTypedArray()
    }

    println(solve(board, k))
}