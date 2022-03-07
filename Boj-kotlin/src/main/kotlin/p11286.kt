package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.PriorityQueue
import kotlin.math.absoluteValue

private fun solve(n: Int, inputs: List<Int>): List<Int> {
    val negPq = PriorityQueue<Int>(Comparator.reverseOrder())
    val posPq = PriorityQueue<Int>()
    val output = mutableListOf<Int>()

    for (inp in inputs) when {
        inp > 0 -> posPq.offer(inp)
        inp < 0 -> negPq.offer(inp)
        negPq.isEmpty() and posPq.isEmpty() -> output.add(0)
        negPq.isEmpty() -> output.add(posPq.poll())
        posPq.isEmpty() -> output.add(negPq.poll())
        negPq.peek().absoluteValue > posPq.peek().absoluteValue -> output.add(posPq.poll())
        else -> output.add(negPq.poll())
    }

    return output
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()

    val inputs = (1..n).map { readLine().toInt() }.toList()
    println(solve(n, inputs).joinToString("\n"))
}