package main.kotlin.p9207
import kotlin.math.max

val dirs = listOf(
  1 to 0,
  -1 to 0,
  0 to 1,
  0 to -1
)

fun main() = with(System.`in`.bufferedReader()){
  val n = readLine().toInt()

  repeat(n){
    val board = Array(5){ readLine().toCharArray() }
    solve(board).also { println("${it.first} ${it.second}") }
    if(it < n-1) readLine()
  }
}

fun solve(board: Array<CharArray>): Pair<Int, Int> {
  // 핀의 개수
  var pin_cnt = board.sumOf { row -> row.filter {it == 'o'}.count() }

  // 움직인 횟수
  var move_cnt = 0

  fun go(k: Int){

    for(y in board.indices) for(x in board[0].indices){

      if(board[y][x] != 'o') continue
      dirs.forEach { (dy, dx) ->
        // next 
        val ny = (y+dy).takeIf { it in board.indices } ?: return@forEach
        val nx = (x+dx).takeIf { it in board[0].indices } ?: return@forEach
        if(board[ny][nx] != 'o') return@forEach
        
        // next_next
        val nny = (ny+dy).takeIf { it in board.indices } ?: return@forEach
        val nnx = (nx+dx).takeIf { it in board[0].indices } ?: return@forEach
        if(board[nny][nnx] != '.') return@forEach

        // 현재 칸(y, x)이 PIN 이면서,
        // 다음 칸(ny, nx)도 PIN 이면서,
        // 다음다음 칸(nny, nnx)가 구멍이라면,

        board[y][x] = '.'
        board[ny][nx] = '.'
        board[nny][nnx] = 'o'
        go(k+1) // go: 핀 이동
        board[y][x] = 'o' 
        board[ny][nx] = 'o'
        board[nny][nnx] = '.'
      }
    }
    move_cnt = max(move_cnt, k) // 이동 횟수 업데이트
  }

  go(0)
  
  return pin_cnt-move_cnt to move_cnt
}
