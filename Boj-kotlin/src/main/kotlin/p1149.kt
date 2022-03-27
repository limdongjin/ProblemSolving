package main.kotlin.p1149

import kotlin.math.min

enum class Color(val id: Int){
    R(0), G(1), B(2), NOTHING(-1)
}

fun solve(costs: List<List<Int>>): Int {
    val n = costs.size
    val dp = Array(n){ Array(3){-1}}.apply {
        this[0][Color.R.id] = costs[0][Color.R.id]
        this[0][Color.G.id] = costs[0][Color.G.id]
        this[0][Color.B.id] = costs[0][Color.B.id]
    }

    fun go(i: Int, color: Color): Int = when(dp[i][color.id]) {
        Color.NOTHING.id -> {
            val (other1, other2) = Color.values().filter { color != it }
            dp[i][color.id] = min(go(i - 1, other1), go(i - 1, other2)) + costs[i][color.id]
            dp[i][color.id]
        }
        else -> dp[i][color.id]
    }

    return minOf(go(n-1, Color.R), go(n-1, Color.G), go(n-1, Color.B))
}


fun main(){
    val n = readln().toInt()
    val costs = List(n) {
        readln().split(" ").map(String::toInt)
    }

    println(solve(costs))
}