package main.kotlin.p16964

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.LinkedList

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine().toInt()
    val edges = List(n-1) {
        readLine().split(" ").map(String::toInt).run {
            this[0] to this[1]
        }
    }
    val visitOrder = readLine()
                        .split(" ")
                        .map(String::toInt) + 0

    println(solve(n, edges, visitOrder))
}

class Graph(n: Int, edges: List<Pair<Int, Int>>){
    val adj = mutableMapOf<Int, MutableList<Int>>()
        .apply {
            for (edge in edges) {
                val lis = this.getOrPut(edge.first) { arrayListOf() }
                lis.add(edge.second)

                val lis2 = this.getOrPut(edge.second) { arrayListOf() }
                lis2.add(edge.first)
            }
        }
    val visited = Array(n+1){false}
    val parent = Array(n+1){ 0 }
    val childN = Array(n+1){ 0 }
}

fun solve(n: Int, edges: List<Pair<Int, Int>>, visitOrder: List<Int>): Int {
    val graph = Graph(n, edges)
    dfs(graph, 1, 0)

    if(visitOrder[0] != 1) return 0
    val curPath = LinkedList<Int>()
    curPath.offerLast(1)

    for(i in 1 until  n){
        var x = visitOrder[i]
        var topIdx = 0
        while (curPath.isNotEmpty()){
            topIdx = curPath.last()
            if(graph.childN[topIdx] > 0) break
            curPath.pollLast()
        }
        if(curPath.isEmpty()) return 0
        if(graph.parent[x] == topIdx){
            graph.childN[topIdx] -= 1
            curPath.offerLast(x)
        }
        else return 0
    }

    return 1
}

fun dfs(graph: Graph, x: Int, prev: Int){
    if(graph.visited[x]) return
    graph.visited[x] = true
    graph.parent[x] = prev
    graph.childN[prev] += 1

    graph.adj[x]!!.forEach { nextNode ->
        dfs(graph, nextNode, x)
    }
}
//
//fun solve_fail(n: Int, edges: List<Pair<Int, Int>>, visitOrder: List<Int>): Int {
//    val graph = mutableMapOf<Int, MutableSet<Int>>()
//        .apply {
//            for (edge in edges) {
//                val lis = this.getOrPut(edge.first) { mutableSetOf() }
//                lis.add(edge.second)
//
//                val lis2 = this.getOrPut(edge.second) { mutableSetOf() }
//                lis2.add(edge.first)
//            }
//        }
////    val adj = Array(n) { Array(n) { false } }
////        .apply {
////            edges.forEach { edge ->
////                this[edge.first][edge.second] = true
////                this[edge.second][edge.first] = true
////            }
////        }
//
////    println(graph)
//    val curVisited = Array(n) { false }.apply { this[0] = true }
//    val isAllChildVisit: (Int) -> Boolean = { graph[it]!!.all { v-> curVisited[v] } }
//
//    var curIdx = 0
//    for(vIdx in 1 until n){
//        val willVisit = visitOrder[vIdx]
//        val curV = visitOrder[curIdx]
//
//        // check curV -> visitOrder[vIdx] : 바로 이동할 수 있는지
//        if(graph[curV]!!.contains(willVisit) && !curVisited[willVisit]){
////            println("ok1")
//            curIdx = vIdx
//            curVisited[willVisit] = true
//            continue
//        }
//
//        // check : willVisit 을 방문할 수 없음에도 불구하고 방문하지않은 다른 노드가 남았다면, 실패.
//        if(!isAllChildVisit(curV)) return 0
//
//
//        // go to parent
//        var flag = false
//        for(i in curIdx-1  downTo 0){
//            val parent = visitOrder[i]
//
//            // if graph[parent] has visitOrder[vIdx]
//            if(graph[parent]!!.contains(willVisit)){
//                curIdx = vIdx
//                flag = true
//                break
//            }
//
//            // if graph[parent] is Not Empty but not has vIdx
//            if(!isAllChildVisit(parent)) return 0
//
//            if(i == 0) return 0
//        }
//
//        if(!flag) return 0
//
//        curVisited[willVisit] = true
//    }
//
//    return 1
//}