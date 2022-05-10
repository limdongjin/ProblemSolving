package main.kotlin.p2887

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue

// custom class 사용하면 메모리 초과.... 오버헤드 발생하는듯
// 근데 Pair, Triple 도 class 인데..
//class Point(val id: Int, val x: Int, val y: Int, val z: Int)
//class Edge(val from: Int, val to: Int, val cost: Int)

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

class UnionFind(val n: Int) {
    var p = IntArray(n) { it }

    fun find(x: Int): Int {
        if(p[x] == x) return x
        p[x] = find(p[x])
        return p[x]
    }

    fun union(x: Int, y: Int): Boolean {
        val a = find(x)
        val b = find(y)

        if ((a == b)) return false

        p[b] = a
        return true
    }
}