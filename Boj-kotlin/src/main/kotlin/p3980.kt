package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

// 선발 명단

private fun solve(stats: List<List<Int>>): Int{
    var ret = 0

    val positionPlayers = (0..10)
        .map { positionId ->
            (0..10)
                .filter { stats[it][positionId] != 0 }
        }

    val nCartesianProduct = nCartesianProduct(positionPlayers)

    for(case1 in nCartesianProduct){
        // require(case1.size == 11)
        ret = max(ret, case1.withIndex().sumOf { (index, pos) ->
            stats[pos][index]
        })
    }

    return ret
}

private fun nCartesianProduct(lists: List<List<Int>>): List<Set<Int>>{
    var ret = lists[0].map { setOf(it) }

    for((index, list1) in lists.slice(1 until lists.size).withIndex()){
        ret = list1.flatMap { ret.map { set1 -> set1.plus(it) } }.filter { it.size == index + 2 }
            .map { it }
    }

    return ret
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val tc = readLine()!!.toInt()
    repeat(tc){
        val stats = (1..11).map {
            readLine().split(" ").map { it.toInt() }
        }

        println(solve(stats))
    }
}