package main.kotlin.utils.unionFind

fun kruskalMST(graph: Graph): Sequence<Edge> =
    DisjointSet(graph.V).let { S ->
        graph.edges.sorted()
            .asSequence()
            .filter { (u, v, _) -> S.find(u) != S.find(v) }
            .onEach { (u, v, _) -> S.union(u, v) }
            .take(graph.V-1)
    }

data class Edge(val u: Int, val v: Int, val cost: Int): Comparable<Edge> {
    override fun compareTo(other: Edge): Int =
        compareValuesBy(this, other, Edge::cost)
}
class Graph(val V: Int, val edges: List<Edge>)
class DisjointSet(val V: Int){
    val p = IntArray(V) { it }
//    val rank = IntArray(V)

    fun find(v: Int): Int =
        if(p[v] == v) v
        else find(p[v]).also { ret -> p[v] = ret }

    fun union(u: Int, v: Int) {
        val pu = find(u)
        val pv = find(v)

//        when {
//            rank[pu] < rank[pv] -> { p[pu] = pv; return }
//            rank[pu] == rank[pv] -> rank[pu]++
//        }

        p[pv] = pu
    }
}