package main.kotlin.p16957

val INF = 987654321
val dirs = listOf(
    0 to 1,
    1 to 1,
    1 to 0,
    1 to -1,
    0 to -1,
    -1 to -1,
    -1 to 0,
    -1 to 1,
    0 to 0
)

data class MutablePair(var y: Int, var x: Int)

fun main() = with(System.`in`.bufferedReader()){
    val (r, c) = readLine().split(" ").map(String::toInt)
    val board = Array(r){ readLine().split(" ").map(String::toInt).toTypedArray() }


    solve(r, c, board)
}

fun solve(r: Int, c: Int, board: Array<Array<Int>>) {
    val b = IntArray(300000)
    val p = IntArray(300000)

    fun find(x: Int): Int {
        if(x == p[x]) return x
        p[x] = find(p[x])
        return p[x]
    }

    for(y in board.indices) for(x in board[0].indices)
    {
        val minDir = dirs.minByOrNull { (dy, dx) ->
            val ny = (y + dy).takeIf { it in board.indices } ?: return@minByOrNull INF
            val nx = (x + dx).takeIf { it in board[0].indices } ?: return@minByOrNull INF

            board[ny][nx]
        }!!

        p[y*c + x] = (y+minDir.first)*c + (x+minDir.second)
    }

    for(y in board.indices) for(x in board[0].indices)
    {
        ++b[find(y*c+x)]
    }

    for(y in board.indices) {
        for(x in board[0].indices)
        {
            print("${b[y*c+x]} ")
        }
        println()
    }
    return
}
