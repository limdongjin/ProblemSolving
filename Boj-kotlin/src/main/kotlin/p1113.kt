package main.kotlin.p1113

val dirs = listOf(
    -1 to 0,
    1 to 0,
    0 to 1,
    0 to -1
)

typealias PosPredicate = (Pair<Int, Int>) -> Boolean

fun main() = with(System.`in`.bufferedReader()){
//    test()
    val (n, m) = readLine().split(" ").map(String::toInt)
    val board = List(n){ readLine().map(Character::getNumericValue) }

    println(solve(n, m, board))
}

fun solve(n: Int, m: Int, board: List<List<Int>>): Int {
    val visited = Array(board.size) { BooleanArray(board[0].size) }

    val isVisited: PosPredicate = { visited[it.first][it.second] }
    val inRange: PosPredicate = { it.first in board.indices && it.second in board[0].indices }
    val q = ArrayDeque<Pair<Int, Int>>()

    fun go(h: Int): Int {
        val isHeightLessThanH: PosPredicate = { board[it.first][it.second] < h }
        var cnt = 1
        var flag = true

        while (q.isNotEmpty()){
            val qsize = q.size
            repeat(qsize){
                val (y, x) = q.removeFirst()
                dirs.forEach { (dy, dx) ->
                    val nPos = (y+dy to x+dx).takeIf(inRange) ?: run { flag = false; return@forEach }

                    nPos.takeUnless(isVisited)
                        ?.takeIf(isHeightLessThanH)
                        ?.let {
                            q.addLast(it)
                            visited[it.first][it.second] = true
                            cnt++
                        }
                }
            }
        }

        return when {
            !flag -> 0
            else -> cnt
        }
    }


    val maxH = board.maxOf { it.maxOrNull() ?: 9 }
    var ans = 0

    for (h in 2..maxH) {
        visited.clear()

        // 첫행,첫열,막행,막열 제외
        for (y in 1 until n - 1) for (x in 1 until m - 1) {
            val pos = (y to x)
                .takeUnless(isVisited)
                ?.takeIf { board[it.first][it.second] < h }
                ?: continue
            visited[pos.first][pos.second] = true
            q.addLast(pos)

            ans += go(h)
        }
    }

    return ans
}

fun Array<BooleanArray>.clear(){
    this.forEach { it.fill(false) }
}

fun test(){
    require(
        solve(n=3, m=5, board = listOf(
            listOf(1,6,6,6,1),
            listOf(6,1,1,1,6),
            listOf(1,6,6,6,1)
        )) == 15
    )
}

