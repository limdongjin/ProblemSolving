package main.kotlin.p1613

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

const val INF = 1234567890
fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (n, k) = readLine().split(" ").map(String::toInt)
    val pairs = List(k) { readLine().split(" ").map(String::toInt).let { it[0] - 1 to it[1] - 1 } }
    val s = readLine().toInt()
    val questions = List(s) { readLine().split(" ").map(String::toInt).let { it[0] - 1 to it[1] - 1 } }

    val dist by lazy { solve(pairs, n) }

    questions.forEach {
        val ans = when {
            dist[it.first][it.second] != INF -> -1
            dist[it.second][it.first] != INF -> 1
            else -> 0
        }

        println(ans)
    }
}

fun solve(pairs: List<Pair<Int, Int>>, n: Int): Array<Array<Int>> {
    val adj = Array(n){Array(n){INF}}
        .apply {
            pairs.forEach { this[it.first][it.second] = 1 }
        }

    val dist = Array(n) { src ->
        Array(n) { INF }.apply {
            this[src] = 0
        }
    }

    repeat(n){
        dijkstra(it, adj, dist[it])
    }

    return dist
}

fun dijkstra(src: Int, adj: Array<Array<Int>>, dist: Array<Int>) {
    val pq = PriorityQueue<Pair<Int, Int>>(compareBy { it.first })
        .apply { offer(dist[src] to src) }

    while(pq.isNotEmpty()){
        val (cost, here) = pq.poll()
        if(dist[here] < cost) continue

        repeat(dist.size){ there ->
            val w = adj[here][there].takeIf { it != INF } ?: return@repeat
            val nextDist = cost + w
            if(dist[there] > nextDist){
                dist[there] = nextDist
                pq.offer(dist[there] to there)
            }
        }
    }
}