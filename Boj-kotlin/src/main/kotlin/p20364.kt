package main.kotlin.p20364

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, q) = readLine()!!.split(" ").map(String::toInt)
    val wants = List(q) { readLine()!!.toInt() }

    val ans = solve(n, q, wants).joinToString("\n")

    println(ans)
}

fun solve(n: Int, q: Int, wants: List<Int>): List<Int> {
    val visited = BooleanArray(n+1)
    val results = ArrayList<Int>(q)

    wants.forEach { land ->
        val res = checkGo(land, visited)
        if(res == 0) visited[land] = true

        results.add(res)
    }

    return results
}

/**
Returns 0 if possible, or 처음 마주치는 점유된 땅 번호 if impossible
*/
fun checkGo(land: Int, visited: BooleanArray): Int =
    generateSequence(land) { x -> (x / 2).takeIf { it != 0 } }
        .filter { visited[it] }
        .minOfOrNull { it } ?: 0