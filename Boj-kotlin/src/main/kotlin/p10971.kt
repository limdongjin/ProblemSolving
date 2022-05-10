package main.kotlin.p10971

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.LinkedList
import kotlin.math.min

class Solver(val costs: List<List<Int>>){
    private val n = costs.size
    private var visited = Array(n) { false }.apply { this[0] = true }
    var ans = Int.MAX_VALUE

    fun solve(): Int {
        go(path = LinkedList<Int>().apply { add(0) }, curCost = 0, visitCnt = 1)
        return ans
    }

    private fun go(path: LinkedList<Int>, curCost: Int, visitCnt: Int) {
        when {
            curCost >= ans -> return
            visitCnt == n -> {
                val v = costs[path.last()][path.first()]
                if(v != 0) ans = min(ans, curCost+v)
                return
            }
        }

        for(i in 1 until n){
            val v = costs[path.last()][i]
            if(visited[i] || v == 0) continue
            visited[i] = true
            path.offerLast(i)

            go(path = path, curCost = curCost+v, visitCnt+1)

            path.pollLast()
            visited[i] = false
        }
    }

}


fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine()!!.toInt()
    val costs = List(n) { readLine()!!.split(" ").map(String::toInt) }

    println(Solver(costs).solve())
}

