package main.kotlin.p23743


data class Edge(var start: Int, var end: Int, var cost: Int)

fun main() = with(System.`in`.bufferedReader()){
    val (n, m) = readLine().split(" ").map(String::toInt)
    val edges = List(m){ readLine().split(" ").map(String::toInt).let { Edge(it[0], it[1], it[2]) } }.toMutableList()
    val tList = readLine().split(" ").map(String::toInt)
    for(i in 1..n){
        edges.add(Edge(0, i, tList[i-1]))
    }

    val p = IntArray(200111)
    for(i in 0..n) p[i] = i

    edges.sortBy { it.cost }

    fun find(x: Int): Int{
        if(p[x] == x){
            return x
        }
        p[x] = find(p[x])
        return p[x]
    }

    fun union(x: Int, y: Int){
        val px = find(x)
        val py = find(y)
        p[px] = py
    }

    var ans = 0L
    for(i in 0 until edges.size){
        if(find(edges[i].start) != find(edges[i].end)){
            union(edges[i].start, edges[i].end)
            ans += edges[i].cost
        }
    }

    println(ans)
}
