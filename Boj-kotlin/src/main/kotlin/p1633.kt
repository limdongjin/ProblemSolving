package main.kotlin.p1633

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val players = ArrayList<Pair<Int, Int>>() // white, black

    while(true){
        try {
            val wb = readLine()?.split(" ")?.map(String::toInt) ?: break
            players.add(wb[0] to wb[1])
        }catch(e: NumberFormatException) {
            break
        }
    }

    println(Solver(players).solve())
}

class Solver(private val players: ArrayList<Pair<Int, Int>>) {
    // dp[player][white][black]
    val n = players.size
    val dp = Array(n) { Array(16) { Array(16){ -1 } } }

    fun solve(): Int {
        return dfs(0, 0, 0)
    }

    fun dfs(idx: Int, w: Int, b: Int): Int{
        when {
            w == 15 && b == 15 -> return 0
            idx == n -> return -1000000000
            dp[idx][w][b] != -1 -> return dp[idx][w][b]
        }

        var ret = dfs(idx+1, w, b)
        if(w < 15) // WHITE
            ret = max(ret, dfs(idx+1, w+1, b) + players[idx].first)
        if(b < 15) // BLACK
            ret = max(ret, dfs(idx+1, w, b+1) + players[idx].second)
        dp[idx][w][b] = ret

        return dp[idx][w][b]
    }
}
