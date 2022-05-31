package main.kotlin.p16948

import java.util.Queue
import kotlin.math.max
import kotlin.math.min

const val INF = 987654321
val dirs = listOf( // dr, dc
    -2 to -1,
    -2 to 1,
    0 to -2,
    0 to 2,
    2 to -1,
    2 to 1
)

fun main() = with(System.`in`.bufferedReader()){
//    test()
    val n = readLine().toInt()
    val (r1, c1, r2, c2) = readLine().split(" ").map(String::toInt)

    println(solve(n, r1, c1, r2, c2))
}

fun solve(n: Int, r1: Int, c1: Int, r2: Int, c2: Int): Int{
    val rangePredicate = { v:Int -> v in 0 until n }
    val gameSuccessPredicate = { r: Int, c: Int -> r == r2 && c == c2 }
    val visited = Array(n){ Array(n){ false } }

    val q = ArrayDeque<Triple<Int, Int, Int>>()
    q.addLast(Triple(r1, c1, 0))
    visited[r1][c1] = true

    while (q.isNotEmpty()){
        val (r, c, cnt) = q.removeFirst()
        dirs.forEach { (dr, dc) ->
            val nr = (r+dr).takeIf(rangePredicate) ?: return@forEach
            val nc = (c+dc).takeIf(rangePredicate) ?: return@forEach
            if(visited[nr][nc]) return@forEach
            if(gameSuccessPredicate(nr, nc)) return cnt+1

            visited[nr][nc] = true
            q.addLast(Triple(nr, nc, cnt+1))
        }
    }

    return -1
}

fun test(){
    require(solve(7,6,6,0,1) == 4)
    require(solve(6,5,1,0,5) == -1)
    require(solve(7,0,3,4,3) == 2)
}
