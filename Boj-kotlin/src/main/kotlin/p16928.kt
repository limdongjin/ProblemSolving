package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader

private fun solve(jump: Array<Int>): Int {
    val dd = Array(101){-1}
    dd[1] = 0
    val q = ArrayDeque<Int>()
    q.addFirst(1)

    while(!q.isEmpty()){
        val x = q.removeLast()
        for(dx in (1..6)){
            var nx = x + dx
            if(nx > 100) continue
            if(jump[nx] != -1) nx = jump[nx]
            if(dd[nx] == -1){
                dd[nx] = dd[x] + 1
                q.addFirst(nx)
            }
        }
    }

    return dd[100]
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (n, m) = readLine().split(' ').map { it.toInt() }
    val jump = Array(101){-1}

    repeat(n+m){
        val (f, to) = readLine().split(' ').map { it.toInt() }
        jump[f] = to
    }

    println(solve(jump))
}