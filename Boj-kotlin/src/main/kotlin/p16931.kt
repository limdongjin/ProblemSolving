package main.kotlin.p16931
import kotlin.math.abs

fun main() = with(System.`in`.bufferedReader()){
//    test()
    val (n, m) = readLine().split(" ").map(String::toInt)
    val board = List(n) { readLine().split(" ").map(String::toInt) }

    println(solve(n, m, board))
}

fun solve(n: Int, m: Int, board: List<List<Int>>): Int {
    val calcSides = { lst: List<Int> -> lst.windowed(2).sumOf { abs(it[0] - it[1]) } + lst.first() + lst.last() }

    return  n*m*2 +
            board.sumOf { row -> calcSides(row) } +
            board[0].indices.sumOf { x -> calcSides(board.indices.map { board[it][x] }) }

}

fun test(){
    require(solve(3, 3, listOf(
            listOf(1, 3, 4),
            listOf(2, 2, 3),
            listOf(1, 2, 4)
        )) == 60)
    require(solve(1, 1, listOf(listOf(1))) == 6)
    require(solve(1, 1, listOf(listOf(10))) == 42)
}