package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue

// 문제 추천 시스템 Version 1

fun PriorityQueue<Pair<Int, Int>>.validPeek(validMap: Map<Int, Int>): Pair<Int, Int>{
    do {
        val flag = with(peek()) {
            return@with (validMap[first] == 0 || validMap[first] != second)
                .takeIf { it }?.also { poll() } ?: false
        }
    }while (flag)

    return peek()
}

private fun solve(problems: List<Pair<Int, Int>>, commands: List<Pair<String, List<Int>>>) {
    // init
    val minQ = PriorityQueue<Pair<Int, Int>>(compareBy({it.second}, {it.first}))
    val maxQ = PriorityQueue<Pair<Int, Int>>(compareBy({-it.second}, {-it.first}))
    val problemsMap = mutableMapOf<Int, Int>() // num -> rank
    problems.forEach {
        minQ.offer(it)
        maxQ.offer(it)
        problemsMap[it.first] = it.second
    }

    commands.forEach { (name, target) ->
        when(name){
            "recommend" -> when(target[0]){
                                1 -> maxQ.validPeek(problemsMap)
                                else -> minQ.validPeek(problemsMap)
                            }.let { println(it.first) }
            "solved" -> problemsMap[target[0]] = 0
            "add" -> {
                problemsMap[target[0]] = target[1]
                maxQ.offer(target[0] to target[1])
                minQ.offer(target[0] to target[1])
            }
        }
    }

    return
}

//private fun solve2(problems: List<Pair<Int, Int>>, commands: List<Pair<String, List<Int>>>) {
//    Sequence
//}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine()!!.toInt()
    // (번호, 난이도)
    val problems = (1..n).map {
        readLine()!!.split(" ").let { it[0].toInt() to it[1].toInt() }
    }
    val m = readLine()!!.toInt()
    val commands = (1..m).map {
        readLine()!!.split(" ").let {
            it[0] to it.subList(1, it.size).map(String::toInt) }
    }



    solve(problems, commands)
}