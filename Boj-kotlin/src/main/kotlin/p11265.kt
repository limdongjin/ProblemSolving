package main.kotlin.p11265

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    run { // init
        nm
        adjMat
        reqs
    }

    reqs.forEach { (a, b, c) ->
        println(when(solve(a, b, c)){
            true -> "Enjoy other party"
            else -> "Stay here"
        })
    }
}

fun solve(a: Int, b: Int, c: Int): Boolean {
    when {
        adjMat[a][b] <= c -> return true
        distCache[a][b] <= c -> return true
        distCache[a][b] != INF -> return false
    }

    dijkstra(a)

    return distCache[a][b] <= c
}

fun dijkstra(src: Int) {
    val dist = distCache[src]

    val pq = PriorityQueue<Pair<Int, Int>>(compareBy { it.first })
        .apply { offer(dist[src] to src) }

    while(pq.isNotEmpty()){
        val (cost, here) = pq.poll()
        if(dist[here] < cost) continue

        repeat(nm.first){ there ->
            val w = adjMat[here][there].takeIf { it != INF } ?: return@repeat
            val nextDist = cost + w
            if(dist[there] > nextDist){
                dist[there] = nextDist
                pq.offer(dist[there] to there)
            }
        }
    }

}

const val INF = 1234567890

val nm: Pair<Int, Int> by lazy {
    readLine()!!.split(" ").map(String::toInt)
        .let { it[0] to it[1] }
}

val adjMat: List<List<Int>> by lazy {
    List(nm.first) {
        readLine()!!.split(" ").map(String::toInt)
            .map { it.takeIf { it != 0 } ?: INF }
    }
}

val distCache: Array<Array<Int>> by lazy {
    Array(nm.first) { src ->
        Array(nm.first) { INF }.apply {
            this[src] = 0
        }
    }
}
val reqs: List<Triple<Int, Int, Int>> by lazy {
    List(nm.second) {
        readLine()!!.split(" ").map(String::toInt)
            .let { Triple(it[0]-1, it[1]-1, it[2]) }
    }
}