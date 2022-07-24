package main.kotlin.p23743

import java.io.BufferedReader

data class Edge(var u: Int, var v: Int, var cost: Int): Comparable<Edge> {
    override fun compareTo(other: Edge): Int = compareValuesBy(this, other) { it.cost }
}
class Graph(val V: Int, val edges: List<Edge>){

    companion object {
        fun buildGraph(block: () -> Graph): Graph = block()
    }
}

class DisjointSet(val V: Int){
    val p = IntArray(V) { it } // make-set

    fun find(v: Int): Int =
        if(p[v] == v) v
        else find(p[v]).also { ret -> p[v] = ret }
    fun union(u: Int, v: Int){
        val pu = find(u)
        val pv = find(v)

        p[pu] = pv
    }
}

fun kruskalMST(graph: Graph): Sequence<Edge> =
    DisjointSet(graph.V).let { S ->
        graph.edges.sorted() // 1. sort edges
            .asSequence()
            .filter { (start, end, _) -> println("F"); S.find(start) != S.find(end) } // 2. filter
            .onEach { (start, end, _) -> println("U"); S.union(start, end) } // 3. union
            .take(graph.V-1)
    }

fun BufferedReader.readInts() = readLine()!!.split(" ").map(String::toInt)
fun main() = with(System.`in`.bufferedReader()){
    val graph = Graph.buildGraph {
        val (n, m) = readInts() //readLine().split(" ").map(String::toInt)
        val edges: List<Edge> = run {
            val warpEdges = List(m) {
                readInts().let { Edge(u=it[0], v=it[1], cost=it[2]) }
            }

            // Note that.
            // Emergency Exit: v[0]
            // Rooms: v[1] ~ v[n]
            val emergencyEdges = readInts()
                .takeIf { it.size == n }!!
                .mapIndexed { i, time -> Edge(0, i+1, time) }

            warpEdges + emergencyEdges
        }

        Graph(V=n+1, edges=edges)
    }

    val ans = kruskalMST(graph).sumOf(Edge::cost)

    println(ans)
}

//fun <P1, P2, R> ((P1, P2) -> R).curried(): (P1) -> (P2) -> R =
//    { p1: P1 -> { p2: P2 -> this(p1, p2) } }
//fun <P1, P2, P3, R> ((P1, P2, P3) -> R).curried(): (P1) -> (P2) -> (P3) -> R =
//    { p1: P1 -> { p2: P2 -> { p3: P3 ->  this(p1, p2, p3) } } }

//fun solve(n: Int, m: Int, edges: List<Edge>): Int {
////    val p = IntArray(200111).apply {
////        for(i in 0..n) this@apply[i] = i
////    }
////    val find = ::find.curried()(p)
////    val union = ::union.curried()(p)`
//    return FindUnion(n).run {
//        edges
//            .sorted() // 1. Sort edges
//            .asSequence()
//            .filter { (start, end, _) -> println("F"); find(start) != find(end) } // 2. filter
//            .onEach { (start, end, _) -> println("U"); union(start, end) } // 3. union
//            .take(n-1)
//            .sumOf { println("S"); it.cost } // 4. sum of costs
//    }
//
//    FindUnion(n).run {
//        val ans = 0
//        edges.sorted()
//            .forEach { (start, end, cost) ->
//                if(find(start) != find(end)){
//
//                    union(start, end)
//                }
//            }
//    }
//
//
//    return FindUnion(n).run {
//        edges.sortedBy(Edge::cost)
//            .asSequence()
//            .filter { edge -> find(edge.start) != find(edge.end) && union(edge.start, edge.end).let { true } }
//            .sumOf(Edge::cost)
//    }
//}

//fun find(p: IntArray, x: Int): Int {
//    if(p[x] == x) return x
//    p[x] = find(p, p[x])
//    return p[x]
//}
//
//fun union(p: IntArray, x: Int, y: Int){
//    val find = (::find.curried())(p)
//    val px = find(x)
//    val py = find(y)
//
//    p[px] = py
//}
