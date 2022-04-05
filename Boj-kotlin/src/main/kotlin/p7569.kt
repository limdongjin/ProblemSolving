package main.kotlin.p7569

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.LinkedList
import kotlin.math.max

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (m, n, h) = readLine().split(" ").map(String::toInt)
    val box = Array(h){ Array(n) {
            readLine().split(" ").map(String::toInt).toTypedArray()
        }
    }

    solve(box)
}

fun solve(box: Array<Array<Array<Int>>>){
    val q = LinkedList<Triple<Int, Int, Int>>()
    val H = box.size
    val N = box[0].size
    val M = box[0][0].size

    for(m in 0 until  M) for(n in 0 until N) for(h in 0 until H) if(box[h][n][m] == 1){
        q.addLast(Triple(h, n, m))
    }
    while (q.isNotEmpty()){
        val (h, n, m) = q.pollFirst()
        if (m > 0 && box[h][n][m-1] == 0) { // 앞
            q.addLast(Triple(h, n, m-1))
            box[h][n][m-1] = box[h][n][m] + 1
        }
        if (m < M-1 && box[h][n][m+1] == 0) { // 뒤
            q.addLast(Triple(h, n, m+1))
            box[h][n][m+1] = box[h][n][m] + 1
        }
        if (n > 0 && box[h][n-1][m] == 0) { // 왼
            q.addLast(Triple(h, n-1, m))
            box[h][n-1][m] = box[h][n][m] + 1
        }
        if (n < N-1 && box[h][n+1][m] == 0) { // 오
            q.addLast(Triple(h, n+1, m))
            box[h][n+1][m] = box[h][n][m] + 1
        }
        if (h > 0 && box[h-1][n][m] == 0) { // 위
            q.addLast(Triple(h-1, n, m))
            box[h-1][n][m] = box[h][n][m] + 1
        }
        if (h < H-1 && box[h+1][n][m] == 0) { // 아래
            q.addLast(Triple(h+1, n, m))
            box[h+1][n][m] = box[h][n][m] + 1
        }
    }

    var flag = true
    var minusCount = N*M*H
    for(hh in box){
        for(rr in hh){
            if(0 in rr) flag = false
            minusCount -= rr.count { it == -1 }
        }
    }

    if(flag && minusCount >= 0){
        var minDay = 1
        for(hh in box){
            for(rr in hh){
                minDay = max(minDay, rr.maxOrNull()!!)
            }
        }
        println(minDay-1)
    }else{
        println(-1)
    }
}
