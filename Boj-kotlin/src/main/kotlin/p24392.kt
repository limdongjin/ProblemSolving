package main.kotlin.p24392

fun main() = with(System.`in`.bufferedReader()){
    // test()
    val (n, m) = readLine().split(" ").map(String::toInt)
    val board = Array(n) { readLine().split(" ").map(String::toByte).toByteArray() }

    println(solve(n, m, board))
}

fun solve(n: Int, m: Int, board: Array<ByteArray>): Long {
    // dp[y][x] : (y, x) 좌표에 도착하는 경우의 수
    // dp[y][x] = (dp[y+1][x-1] + dp[y+1][x] + dp[y+1][x+1])*board[y][x]
    // 만약 일반 유리라면 board 값 0이 곱해지므로 dp 값도 0이 된다.
    if(m == 1) return if(board.all { it[0] == 1.toByte() }) 1L else 0L

    val R = 1_000_000_007L
    val startY = n-1; val endX = m-1
    val dp = Array(n) { LongArray(m) }
        .apply {
            for(x in board[startY].indices) this[startY][x] = board[startY][x].toLong()
        }

    for(y in startY-1  downTo 0){
        dp[y][0] = ((dp[y+1][0] + dp[y+1][1])*board[y][0])%R
        dp[y][endX] = ((dp[y+1][endX-1] + dp[y+1][endX])*board[y][endX])%R

        for(x in 1 until endX){
            dp[y][x] = ((dp[y+1][x-1] + dp[y+1][x] + dp[y+1][x+1])*board[y][x])%R
        }
    }
    
    return (dp[0].sum())%R
}

fun test(){
    require(solve(n = 4, m = 4, board = arrayOf(
        byteArrayOf(1, 1, 1, 1),
        byteArrayOf(1, 0, 0, 1),
        byteArrayOf(1, 0, 0, 1),
        byteArrayOf(1, 1, 1, 1),
    )) == 8L)
    require(solve(n = 1, m= 1, board = arrayOf(
        byteArrayOf(1)
    )) == 1L)
    require(solve(n = 1, m= 1, board = arrayOf(
        byteArrayOf(0)
    )) == 0L)
    require(solve(n = 1, m= 3, board = arrayOf(
        byteArrayOf(1, 0, 1)
    )) == 2L)
    require(solve(n = 3, m= 1, board = arrayOf(
        byteArrayOf(1),
        byteArrayOf(0),
        byteArrayOf(1)
    )) == 0L)
    require(solve(n = 3, m= 1, board = arrayOf(
        byteArrayOf(1),
        byteArrayOf(1),
        byteArrayOf(1)
    )) == 1L)
}