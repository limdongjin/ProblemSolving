package main.kotlin.p17472

val dirs = listOf(1 to 0, -1 to 0, 0 to 1, 0 to -1)
data class Pos(val y: Int, val x: Int)
data class Edge(val v: Int, val u: Int, val cost: Int): Comparable<Edge>{
    override operator fun compareTo(other: Edge): Int =
        compareValuesBy(this, other, Edge::cost)
}
class Graph(val V: Int, val edges: List<Edge>)
class DisjointSet(val V: Int){
    val p = IntArray(V) { it }
    
    fun find(v: Int): Int = 
        if(p[v] == v) v
        else find(p[v]).also { ret -> p[v] = ret }

    fun union(v: Int, u: Int) {
        val pov = find(v)
        val pou = find(u)

        p[pov] = pou
    }
}

fun main() = with(System.`in`.bufferedReader()){
    fun readInts() = readLine().split(" ").map(String::toInt)

    val (n, m) = readInts()
    val board = Array(n) { readInts().toTypedArray() }

    val ans = solve(n,m,board)

    println(ans)
}

fun solve(n: Int, m: Int, board: Array<Array<Int>>): Int {
    // 1. board labeling (0=바다, 1: unlabeled land, 2~k+1 = labeled land)
    val nOfVertex = labelingAll(board)

    require(nOfVertex in 2..6)
//    require(board.all { row -> row.all { it == 0 || it >= 2 } })

    val edges: List<Edge> = findEdges(board)

    // 2. G.V = { 0, 1, ... }
    // 3. G.E = { Edge(0 <-> 1), Edge(0 <-> 2), ... Edge(k <->k+1) }
    val graph = Graph(V=nOfVertex, edges)

    // 4. Find Minimum Spanning Tree.
    return kruskalMST(graph)
        .map(Edge::cost)
        .toList()
        .takeIf { it.size == graph.V - 1 } // is only one MST?
        ?.sum()
        ?: -1
}

fun kruskalMST(graph: Graph): Sequence<Edge> =
    DisjointSet(graph.V).let { S ->
        graph.edges.sorted()
            .asSequence()
            .filter { (v, u, _) -> S.find(v) != S.find(u) }
            .onEach { (v, u, _) -> S.union(v, u) }
            .take(graph.V-1)
    }

fun <T> Array<Array<T>>.yxs(): Sequence<Pos> =
    sequence {
        for(y in this@yxs.indices) for(x in this@yxs[y].indices) yield(Pos(y=y, x=x))
    }

fun findEdges(board: Array<Array<Int>>): List<Edge> {
    val candidates = mutableListOf<Pair<Set<Int>, Int>>()

    board.yxs()
        .filter { board[it.y][it.x] >= 2 }
        .forEach { (y, x) -> 
            val myColor = board[y][x]
            
            dirs.forEach { (dy, dx) ->
                var diff = 1
                var otherColor = -1
                while(y+dy*diff in board.indices && x+dx*diff in board[0].indices){
                    require(otherColor == -1)

                    val cell = board[y+dy*diff][x+dx*diff] 
                    when(cell){
                        myColor -> break
                        0 -> diff++
                        else -> { otherColor = cell; break }
                    }
                }

                diff--
                if(otherColor != -1 && diff > 1)
                    candidates.add(setOf(myColor, otherColor) to diff)
            }
        }

    // require(candidates.all { (S, cost) -> S.first() != S.last() && cost >= 2 })

    return candidates // [ Pair(set(v, u), cost), ...]
        .groupBy(keySelector = { it.first }, valueTransform = { it.second }) // Map { set(v, u): [ cost1, cost2,..] }
        .mapValues { (_, value) -> value.minOrNull()!! } // Map { set(v, u): cost, .... }
        .map { (key, value) -> Edge(v=key.first()-2, u=key.last()-2, cost=value) } // [ Edge1, Edge2, ... ]
}

fun labelingAll(board: Array<Array<Int>>): Int {
    var nextColor = 2
    
    board.yxs()
        .filter { (y, x) -> board[y][x] == 1 }
        .forEach { (y, x) -> labeling(board, Pos(y, x), nextColor); nextColor++ }
    
    return nextColor - 2
}

fun labeling(board: Array<Array<Int>>, pos: Pos, color: Int) {
    require(color >= 2)

    val q = ArrayDeque<Pos>().apply { addLast(pos) }
    board[pos.y][pos.x] = color

    while(q.isNotEmpty()){
        val (y, x) = q.removeFirst()
        dirs.forEach { (dy, dx) ->
            val ny = (y+dy).takeIf { it in board.indices } ?: return@forEach
            val nx = (x+dx).takeIf { it in board[0].indices } ?: return@forEach
            if(board[ny][nx] != 1) return@forEach // 0 or Labelled island
            
            board[ny][nx] = color
            q.addLast(Pos(y=ny, x=nx))
        }
    }
}
