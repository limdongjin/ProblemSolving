package main.kotlin.p14620

private typealias Pos = Pair<Int, Int>
val dirs = listOf(
    1 to 0,
    -1 to 0,
    0 to 1,
    0 to -1
)
const val INF = 987654321

fun main() = with(System.`in`.bufferedReader()){
    val n = readLine().toInt()
    val board = Array(n){ readLine()!!.split(" ").map(String::toInt).toIntArray() }

    println(solve(n, board))
}

fun solve(n: Int, board: Array<IntArray>): Int {
    val encode = { pos: Pos -> pos.encode(n) }
    val decode = { encoded: Int -> decode(encoded, n) }

    val getAllCombinations: () -> Sequence<Triple<Pos, Pos, Pos>> = {
        val encodedList = (0 until n * n)
            .asSequence()
            .map(decode)
            .filter { it.first != 0 && it.first != n - 1 && it.second != 0 && it.second != n - 1 }
            .map(encode)
            .toList()

        combinations(3, encodedList).asSequence()
            .map { it.map(decode) }
            .map(List<Pos>::toTriple)
    }

    val inRange: (Pos) -> Boolean = { it.first in board.indices && it.second in board[0].indices }
    val adjPositions: (Pos) -> List<Pos> = { dirs.map { (dy, dx) -> it.first+dy to it.second+dx } }

    val calcCost: (Triple<Pos, Pos, Pos>) -> Int = {
        (adjPositions(it.first) + adjPositions(it.second) + adjPositions(it.third))
            .plus(listOf(it.first, it.second, it.third))
            .asSequence()
            .filter(inRange)
            .distinctBy(encode)
            .takeIf { posList -> posList.count() == 15 }
            ?.sumOf { pos -> board[pos.first][pos.second] }
            ?: INF
    }

    return getAllCombinations().minOf(calcCost)
}


private fun Pos.encode(width: Int) = first*width + second
private fun decode(encoded: Int, width: Int) = Pos(encoded / width, encoded % width)

fun <T> List<T>.toTriple(): Triple<T, T, T> {
    require(size == 3)
    return Triple(get(0), get(1), get(2))
}

fun combinations(n: Int, lst: List<Int>): List<List<Int>> = when(n){
    0 -> listOf(emptyList())
    else -> when(lst.isNotEmpty()){
        true -> combinations(n-1, lst)
                    .map(listOf(lst[0])::plus)
                    .plus(combinations(n, lst.subList(1, lst.size)))
        false -> emptyList()
    }
}