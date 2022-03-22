package main.kotlin.p1865

import java.io.BufferedReader
import java.io.InputStreamReader

private fun bellmanFord(adj: List<MutableList<Pair<Int, Int>>>, src: Int): Array<Int>{
    fun relaxEdges(dist: Array<Int>): Boolean {
        var updated = false
        for(v1 in adj.indices) for((v2, weight) in adj[v1])
            if (dist[v2] > dist[v1] + weight) {
                dist[v2] = dist[v1] + weight
                updated = true
            }
        return updated
    }

    val dist = Array(adj.size) { 987654321 }.apply { this[src] = 0 }

    repeat(adj.size-1) { relaxEdges(dist) }

    return when(relaxEdges(dist)){
        true -> emptyArray() // 음수 사이클 존재하면 비어있는 배열 리턴
        else -> dist
    }
}

private fun solve(n: Int, roadsInfo: Array<Array<Int>>, holesInfo: Array<Array<Int>>): String {
    // 인접 리스트 생성 :: adj[from][i] = (to, w)
    val adj = buildList<MutableList<Pair<Int, Int>>>(n) {
        repeat(n) {
            add(mutableListOf())
        }

        roadsInfo.forEach {
            this[it[0]-1].add(it[1]-1 to it[2])
            this[it[1]-1].add(it[0]-1 to it[2])
        }
        holesInfo.forEach { this[it[0]-1].add(it[1]-1 to -it[2]) } // 웜홀은 음수 가중치
    }

    // 벨만포드
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

        println(solve(n, roadsInfo, holeInfo))
    }
}

private fun BufferedReader.readInts(): Array<Int> =
    readLine()
        .split(" ")
        .map { it.toInt() }.toTypedArray()