package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.min

private fun bellmanFord(adj: List<MutableList<Pair<Int, Int>>>, src: Int): Array<Int>{
    fun relax(upper: Array<Int>): Boolean {
        var updated = false
        for(here in adj.indices) for(i in adj[here].indices){
            val (there, cost) = adj[here][i]
            if (upper[there] > upper[here] + cost){
                upper[there] = upper[here] + cost
                updated = true
            }
        }
        return updated
    }

    var updated = false
    val upper = Array(adj.size) { 987654321 }
    // val upper = Array(adj.size) { Integer.MAX_VALUE }
    //    오버플로우 발생 => 틀린 답을 발생시킴

    upper[src] = 0

    repeat(adj.size) {
        relax(upper)
            .also { ret: Boolean ->
                updated = ret
                if(!updated) return@repeat
            }
    }

    // V 번째 순회에도 완화가 성공했다면, 음수 사이클이 있다.
    return when(updated){
        true -> emptyArray()
        else -> upper
    }
}

private fun solve(n: Int, roadsInfo: Array<Array<Int>>, holesInfo: Array<Array<Int>>): String {
    val adj = buildList<MutableList<Pair<Int, Int>>>(n) {
        repeat(n) {
            add(mutableListOf())
        }

        roadsInfo.forEach {
            this[it[0]-1].add(it[1]-1 to it[2])
            this[it[1]-1].add(it[0]-1 to it[2])
        }
        holesInfo.forEach { this[it[0]-1].add(it[1]-1 to -it[2]) }
    }

    bellmanFord(adj, 0)
        .also {
            return when(it.isEmpty()){
                true -> "YES"
                else -> "NO"
            }
        }
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val tc = readLine().toInt()

    repeat(tc) {
        val (n, m, w) = readInts()
        val roadsInfo = (1..m).map { readInts() }.toTypedArray()
        val holeInfo = (1..w).map { readInts() }.toTypedArray()

        solve(n, roadsInfo, holeInfo)
            .also { println(it) }
    }
}

private fun BufferedReader.readInts(): Array<Int> =
    readLine()
        .split(" ")
        .map { it.toInt() }.toTypedArray()
