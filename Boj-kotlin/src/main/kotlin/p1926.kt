package main.kotlin.p1926
import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.LinkedList

private typealias Point = Pair<Int, Int>

private object Extensions {
    val Point.y: Int
        get() =  first
    val Point.x: Int
        get() = second
    fun Point.getNeighbors(): Sequence<Point> =
        dirs.map { this + it }
    fun Array<Array<Int>>.checkIndex(point: Point): Boolean =
        point.y in this.indices && point.x in this[0].indices
    operator fun Array<Array<Int>>.get(point: Point): Int =
        this[point.y][point.x]
    operator fun Array<Array<Int>>.set(point: Point, value: Int) {
        this[point.y][point.x] = value
    }

    private operator fun Point.plus(other: Point): Point =
        y+other.y to x+other.x
    private val dirs = sequenceOf(// up right down left
        -1 to 0,
        0 to 1,
        1 to 0,
        0 to -1
    )
}

private fun bfs(board: Array<Array<Int>>,
                point: Point, id: Int): Int = with(Extensions) {
    // 빈칸이거나 이미 라벨링된 그림이면, return
    if(board[point] != 0) return id

    val q = LinkedList<Point>().apply { offer(point) }
    board[point] = id

    while(q.isNotEmpty())
        q.poll().getNeighbors()
            .filter { board.checkIndex(it) && board[it] == 0 }
            .forEach {
                q.offer(it)
                board[it] = id
            }

    return id+1 // next label id
}

private fun solve(board: Array<Array<Int>>) = with(Extensions) {
    // 1 이 있는 좌표를 저장
    val positions = board.indices
        .flatMap { y -> board[y].indices.map { Point(y, it) } }
        .filter { board[it.y][it.x] == 1 }

    // 데이터 정규화
    for (y in board.indices) for(x in board[y].indices)
        board[y to x] = board[y to x]-1

    // => 빈칸: -1 || 그림: 0

    // 라벨링
    var id = 1 // id: 그림 라벨
    positions.forEach { id = bfs(board, it, id) }

    // 그림의 개수, 가장 넓은 그림의 넓이를 구한다.
    board
        .flatten()
        .asSequence()
        .filter { it > 0 }
        .groupingBy { it }.eachCount() // ex, {1: 4, 2: 2, 3: 9, 4: 1}
        .run {
            println(size) // 그림의 개수 : key 의 개수
            println(maxOfOrNull { p -> p.value }?:0) // 가장 넓은 그림의 넓이 : max value
        }
}

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    fun BufferedReader.readInts(): Array<Int>
        = readLine().split(" ").map {it.toInt()}.toTypedArray()

    val (h, _) = readInts()
    val board = (1..h).map { readInts() }.toTypedArray()

    solve(board)
}