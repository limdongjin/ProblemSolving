package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

private var moveDirs = listOf(
    0 to 1,
    0 to -1,
    1 to 0,
    -1 to 0
)

private fun solve(board: Array<IntArray>){
    val ansBoard = Array(board.size) { IntArray(board[0].size) {0} }

     // Example of board
     // 1001
     // 0101
     // 1010

    // labels = { 라벨1: 영역크기, 라벨2: 영역크기, ... }
    val labels = labeling(board)
    // new state of board after labelling(board)
    // 1221
    // 3121
    // 1415

    for(y in board.indices) for(x in board[0].indices)
    {
        // board[y][x] 벽 부시기 진행

        // 벽이 아니므로, 스킵
        if(board[y][x] != 1) continue

        val s = mutableSetOf<Int>()
        for((dy, dx) in moveDirs){
            val ny = y+dy
            val nx = x+dx

            if(ny !in board.indices || nx !in board[0].indices) // 범위 체크
                continue
            if(board[ny][nx] == 1 || s.contains(board[ny][nx])) // 새로운 벽은 스킵한다.
                continue

            // board[ny][nx] : 새로 발견한 빈칸 영역

            s.add(board[ny][nx])
            ansBoard[y][x] += labels[board[ny][nx]]!! // 현재 벽의 정답 값을 업데이트
        }
        ansBoard[y][x] = ansBoard[y][x] + 1
        ansBoard[y][x] = ansBoard[y][x] % 10
    }

    // print answer board
    for(y in board.indices)
        println(ansBoard[y].joinToString(""))

    return
}

// 빈칸 라벨링
// 함수 실행후 결과: 연결된 영역끼리는 서로 같은 라벨 값(>=2)을 갖는다.
// 리턴: { 라벨1: 영역크기, 라벨2: 영역크기, ... }
private fun labeling(board: Array<IntArray>): Map<Int, Int>{
    var id = 2
    val labels = mutableMapOf<Int, Int>()

    for(y in board.indices) for(x in board[0].indices)
        if(board[y][x] == 0)
            labelingId(y to x, id, board)
                .also { labels[id++] = it }

    return labels.toMap()
}

// 구현: BFS
// 함수 실행후 결과: pos(좌표) 와 연결된 영역에, 모두 id 값을 넣음.
// 리턴: id 라벨 영역의 크기를 리턴함.
private fun labelingId(pos: Pair<Int, Int>, id: Int, board: Array<IntArray>): Int{
    val q: Queue<Pair<Int, Int>> = LinkedList()
    q.offer(pos)

    var areaSize = 0
    while (!q.isEmpty()){
        val (y, x) = q.poll()
        board[y][x] = id
        areaSize++

        for((dy, dx) in moveDirs){
            val ny = y+dy
            val nx = x+dx
            if(ny !in board.indices || nx !in board[0].indices || board[ny][nx] != 0)
                continue

            board[ny][nx] = id
            q.offer(ny to nx)
        }
    }

    return areaSize
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (n, _) = readLine().split(' ').map {it.toInt()}
    val board = (1..n).map {
        readLine().toCharArray().map { it.code - '0'.code }.toIntArray()
    }.toTypedArray()

    solve(board)
}