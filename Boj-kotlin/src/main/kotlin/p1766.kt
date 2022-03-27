package main.kotlin.p1766

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue

// 1766 문제집

class Graph(n: Int) {
    class Node(val num: Int) {
        var unsolvedParentNum = 0
        val children = mutableListOf<Node>()
    }

    val nodes: List<Node> = (0 until n).map{ Node(it) }
}


fun solve(n: Int, problemPairs: List<Pair<Int, Int>>): List<Int>{
    val graph = Graph(n).apply {
        problemPairs.forEach {
            nodes[it.first].children
                           .add(nodes[it.second])
            nodes[it.second].unsolvedParentNum += 1
        }
    }

    // Each node : (unsolved 상태의)부모가 없는 노드
    val candidates = PriorityQueue<Graph.Node>(compareBy { it.num })
        .apply {
            graph.nodes
                .filter { it.unsolvedParentNum == 0 }
                .forEach(::offer)
        }

    val solvedProblems = mutableListOf<Int>()

    while(candidates.isNotEmpty())
        candidates.poll()
            .run {
                solvedProblems.add(num)

                // children: 제거된 노드의 자식들
                children.forEach { child ->
                        child.unsolvedParentNum-- // 해당 노드의 부모 숫자를 줄인다.
                        if(child.unsolvedParentNum == 0)
                            candidates.offer(child) // child 노드의 부모가 없다면,
                                                    // candidates 에 child 추가
                }
            }

    return solvedProblems.map(Int::inc)
}


fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val (n, m) = readLine().split(" ").map(String::toInt)
    val problemPairs = List(m){
        readLine().split(" ").run { get(0).toInt()-1 to get(1).toInt()-1 }
    }

    val ans = solve(n, problemPairs)
    println(ans.joinToString(" "))
}