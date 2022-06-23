package main.kotlin.p24513

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.LinkedList
import java.util.Queue
import java.util.StringTokenizer

typealias Pos = Pair<Int, Int>
val dirs = listOf(
    1 to 0,
    -1 to 0,
    0 to 1,
    0 to -1
)

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    var st = StringTokenizer(br.readLine())

    val (n, m) = st.nextToken().toInt() to st.nextToken().toInt()
    val board = Array(n) { IntArray(m) { 0 } }
    var onePos = -1 to -1; var twoPos = -1 to -1
    repeat(n) { y ->
        st = StringTokenizer(br.readLine())
        for(x in 0 until m){
            board[y][x] = st.nextToken().toInt()
            if(board[y][x] == 1){
                onePos = y to x
            }else if(board[y][x] == 2){
                twoPos = y to x
            }
        }
    }

    val (one, two, three) = solve(n, m, board, onePos, twoPos)
    println("$one $two $three")
}

fun solve(n: Int, m: Int, board: Array<IntArray>, onePos: Pos, twoPos: Pos): Triple<Int, Int, Int> {
    val visitedTime = Array(n){ IntArray(m){ 0 } }
    val q: Queue<Pair<Pos, Int>> = LinkedList<Pair<Pos, Int>>().apply {
        offer(Pair(onePos, 1))
        offer(Pair(twoPos, 1))
    }
    while (q.isNotEmpty()){
        val (pos, t) = q.poll()
        val curCell = board[pos.first][pos.second]
        if(curCell != 1 && curCell != 2) continue
        dirs.forEach { (dy, dx) ->
            val ny = (pos.first + dy).takeIf { it in 0 until n } ?: return@forEach
            val nx = (pos.second + dx).takeIf { it in 0 until m } ?: return@forEach

            if(board[ny][nx] == 0){
                board[ny][nx] = curCell
                visitedTime[ny][nx] = t
                q.offer(Pair(ny to nx, t+1))
            }else if(visitedTime[ny][nx] == t && board[ny][nx] != curCell){
                board[ny][nx] = 3
            }
        }
    }

    val ans = run {
        var one = 0; var two = 0; var three = 0
        for(y in board.indices) for(x in board[0].indices){
            when(board[y][x]){
                1 -> one++
                2 -> two++
                3-> three++
            }
        }

        Triple(one, two, three)
    }

    return ans
}
