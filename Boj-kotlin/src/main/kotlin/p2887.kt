package main.kotlin.p2887

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue

@ExperimentalStdlibApi
fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine().toInt()

    val points: MutableList<Pair<Int, Triple<Int, Int, Int>>> = MutableList(n) { i ->
        readLine()!!.split(" ")
            .map(String::toInt)
            .run {
                Pair(i, Triple(this[0], this[1], this[2]))
            }
    }
    val q = PriorityQueue<Triple<Int, Int, Int>>(compareBy { it.third })
    points.sortBy { it.second.first }
    for(i in 0 until n-1){
        q.add(Triple(points[i].first, points[i+1].first, points[i+1].second.first-points[i].second.first))
    }

    points.sortBy { it.second.second }
    for(i in 0 until n-1){
        q.add(Triple(points[i].first, points[i+1].first, points[i+1].second.second-points[i].second.second))
    }

    points.sortBy { it.second.third }
    for(i in 0 until n-1){
        q.add(Triple(points[i].first, points[i+1].first, points[i+1].second.third-points[i].second.third))
    }

    var ans = 0
    val u = UnionFind(n)

    while (q.isNotEmpty()){
        val (a, b, cost) = q.poll()
        if(u.union(a, b)) ans += cost
    }

    println(ans)
}

@ExperimentalStdlibApi
class UnionFind(val n: Int) {
    var p = IntArray(n) { it }

    @ExperimentalStdlibApi
    val find2 = DeepRecursiveFunction<Int, Int> { x ->
        if(p[x] == x) return@DeepRecursiveFunction x
        p[x] = callRecursive(p[x])
        return@DeepRecursiveFunction p[x]
    }
//
//    @ExperimentalStdlibApi
//    val union2 = DeepRecursiveFunction<Pair<Int, Int>, Boolean> { (x, y) ->
//        val a = find2.callRecursive(x)
//        val b = find2.callRecursive(y)
//
//        if ((a == b)) return@DeepRecursiveFunction false
//
//        p[b] = a
//        return@DeepRecursiveFunction true
//    }
    @ExperimentalStdlibApi
    fun union(x: Int, y: Int): Boolean {
        val a = find2(x)
        val b = find2(y)

        if ((a == b)) return false

        p[b] = a
        return true
    }
}