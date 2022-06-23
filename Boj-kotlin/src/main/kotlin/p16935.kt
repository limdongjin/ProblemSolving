package main.kotlin.p16935


fun main() = with(System.`in`.bufferedReader()){
    test()
    val (n, m, r) = readLine().split(" ").map(String::toInt)
    val board = Array(n) { readLine().split(" ").map(String::toInt).toTypedArray() }
    val operations = readLine().split(" ").map(String::toInt)

    solve(n, m, r, board, operations)
}

fun solve(n: Int, m: Int, r: Int, board: Array<Array<Int>>, operations: List<Int>){
    var curBoard = Array(n){ Array(m){ 0 } }.apply {
        for(y in board.indices) for(x in board[0].indices)
            this[y][x] = board[y][x]
    }

    operations.forEach { op ->
        when(op){
            1 -> curBoard = curBoard.transform1234(newN=curBoard.size, newM=curBoard[0].size) { curBoard.size-it.first-1 to it.second }
            2 -> curBoard = curBoard.transform1234(newN=curBoard.size, newM=curBoard[0].size) { it.first to curBoard[0].size-it.second-1 }
            3 -> curBoard = curBoard.transform1234(newN=curBoard[0].size, newM=curBoard.size) { it.second to curBoard.size-1-it.first }
            4 -> curBoard = curBoard.transform1234(newN=curBoard[0].size, newM=curBoard.size) { curBoard[0].size-1-it.second to it.first }
            5 -> curBoard = curBoard.transform5()
            6 -> curBoard = curBoard.transform6()
        }
    }

    curBoard.forEach {
        println(it.joinToString(" "))
    }
}

fun Array<Array<Int>>.transform1234(newN: Int, newM: Int, transformNewYX: (Pair<Int, Int>) -> Pair<Int, Int>): Array<Array<Int>> {
    val transformed = Array(newN) { y -> Array<Int>(newM){ 0 } }
    for(y in this.indices) for(x in this[0].indices){
        transformNewYX(y to x).also { (ny, nx) ->
            transformed[ny][nx] = this[y][x]
        }
    }

    return transformed
}

fun Array<Array<Int>>.transform5(): Array<Array<Int>> {
    val n = this.size; val m = this[0].size
    val transformed = Array(this.size) { y -> Array<Int>(this[0].size){ 0 } }
    val nMid = this.size/2
    val mMid = this[0].size/2

    for(y in 0 until nMid) for(x in 0 until mMid)
        transformed[y][mMid+x] = this[y][x]

    for(y in 0 until nMid) for(x in mMid until this[0].size)
        transformed[nMid+y][x] = this[y][x]

    for(y in nMid  until this.size) {
        for((c, x) in (mMid until this[0].size).withIndex()){
            transformed[y][c] = this[y][x]
        }
    }

    for((row, y) in (nMid until this.size).withIndex()){
        for(x in 0 until mMid)
            transformed[row][x] = this[y][x]
    }

    return transformed
}

fun Array<Array<Int>>.transform6(): Array<Array<Int>> {
    val n = this.size; val m = this[0].size
    val transformed = Array(this.size) { y -> Array<Int>(this[0].size){ 0 } }
    val nMid = this.size/2
    val mMid = this[0].size/2

    for(y in 0 until nMid) for(x in 0 until mMid)
        transformed[nMid+y][x] = this[y][x]

    for(y in nMid until n) for(x in 0 until mMid)
        transformed[y][mMid+x] = this[y][x]

    var row = 0
    for(y in nMid until n) {
        for(x in mMid until m)
            transformed[row][x] = this[y][x]

        row++
    }

    for(y in 0 until nMid){
        var c = 0
        for(x in mMid until m){
            transformed[y][c] = this[y][x]
            c++
        }
    }

    return transformed
}

fun test(){
    var transformed
    = arrayOf(
        arrayOf(1, 2),
        arrayOf(3, 4)
    ).transform1234(2, 2) { pos -> 2 - pos.first - 1 to pos.second }

    require(transformed.contentDeepEquals(
            arrayOf(
                arrayOf(3, 4),
                arrayOf(1, 2)
            )
    ))

    /*
     1 2
     3 4

     n = 높이, m=너비
     (y, x) -> (y', x')

     1번 연산 (상하) // (y', x') = (n-y-1, x), n'=n, m'=m
     3 4
     1 2

     2번(좌우) // (y', x') = (y, m-x-1), n'=n, m'=m
     2 1
     4 3

     3번(오른쪽으로 90회전) // (y', x') = (x, n-1-y), n'=m, m'=n
     // (n-1, 0) -> (0, 0)
     // (0, x=0) -> (0, n-1-0)
     // (0, x=1) -> (1, n-1-0)
     // (1, x=1) -> (1, n-1-1) = (1, 0)
     3 1
     4 2

     4번(왼쪽 90회전)     // (y', x') = (m-1-x ,y),  m'=n, n'=m
     // (y=0, 0) -> (1, 0)
     // (y=0, 1) -> (0, 0)
     2 4
     1 3

    5번(1그룹 -> 2그룹, .....)
    // n/2,
    // m/2

     */

}


