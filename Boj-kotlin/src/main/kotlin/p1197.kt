package main.kotlin.p1197

data class Edge(val u: Int, val v: Int, val cost: Int): Comparable<Edge> {
    override fun compareTo(other: Edge): Int =
        compareValuesBy(this, other, Edge::cost)
}
class Graph(val V: Int, val edges: List<Edge>)
class DisjointSet(val V: Int){
    val p = IntArray(V) { it }
    val rank = IntArray(V)

    fun find(v: Int): Int =
        if(p[v] == v) v
        else find(p[v]).also { ret -> p[v] = ret }

    fun union(u: Int, v: Int) {
        val pu = find(u)
        val pv = find(v)

        when {
            rank[pu] < rank[pv] -> { p[pu] = pv; return }
            rank[pu] == rank[pv] -> rank[pu]++
        }

        p[pv] = pu
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    fun readInts() = readLine().split(" ").map(String::toInt)
    val (v, e) = readInts()
    val edgesInfo = List(e) { readInts() }

    val ans = solve(v, e, edgesInfo)

    println(ans)
}

fun solve(v: Int, e: Int, edgesInfo: List<List<Int>>): Long {
    val graph = Graph(V=v, edges = edgesInfo.map { (u, v, cost) -> Edge(u-1, v-1, cost) })

    return kruskalMST(graph).sumOf { edge -> edge.cost.toLong() }
}

fun kruskalMST(graph: Graph): Sequence<Edge> =
    DisjointSet(graph.V).let { S ->
        graph.edges.sorted()
            .asSequence()
            .filter { (u, v, _) -> S.find(u) != S.find(v) }
            .onEach { (u, v, _) -> S.union(u, v) }
            .take(graph.V-1)
    }