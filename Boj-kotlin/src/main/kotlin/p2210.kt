package main.kotlin.p2210

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val board = List(5) {
        readLine().split(" ").map(String::toInt)
    }

    println(solve(board))
}

fun solve(board: List<List<Int>>): Int {
    val allCases = listOf(0, 1, 2, 3)
        .let { listOf(it, it, it, it, it) }
        .let { nLists ->
            nCartesianProduct(nLists)
        }
    // require(allCases.size == 1024)

    val yxList = nCartesianProduct(listOf(board.indices, board[0].indices))
    val results = yxList.fold(setOf<String>()){ acc, (y, x) ->
        acc + allCases
            .asSequence()
            .map { oneCase -> simulate(board, oneCase, y to x) }
            .filterNotNull()
            .toSet()
    }

    return results.size
}

fun simulate(board: List<List<Int>>, oneCase: List<Int>, initialPos: Pair<Int, Int>): String? {
    var curY = initialPos.first
    var curX = initialPos.second
    val ret = StringBuilder("${board[curY][curX]}")

    oneCase.forEach {
        curY += d[it].first
        curX += d[it].second
        if(curY !in board.indices) return null
        if(curX !in board[0].indices) return null

        ret.append(board[curY][curX])
    }

    return ret.toString()
}

fun <T> nCartesianProduct(nLists: Collection<Iterable<T>>): Set<List<T>> = with(nLists) {
    return if (isEmpty()) emptySet()
    else drop(1).fold(first().map(::listOf)) { acc, iterable ->
        acc.flatMap { list -> iterable.map(list::plus) }
    }.toSet()
}

val d = listOf(
    -1 to 0,
    0 to 1,
    1 to 0,
    0 to -1
)