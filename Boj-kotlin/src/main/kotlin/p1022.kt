package main.kotlin.p1022
// 소용돌이 예쁘게 출력하기
import java.io.BufferedReader
import java.io.InputStreamReader

private typealias Point = Pair<Int, Int>

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val(r1, c1, r2, c2) = readLine()!!.split(" ").map{it.toInt()}
    solve(r1, c1, r2, c2)
}


private fun solve(r1: Int, c1: Int, r2: Int, c2: Int) {
    val board = makeAnsBoard(r1, c1, r2, c2)
    val maxLength = board.maxOf { it.maxOf { v -> "$v".length } }

    board.forEach { row ->
        row.joinToString(" ") { "%${maxLength}d".format(it) }
            .also { println(it) }
    }
}

private fun makeAnsBoard(r1: Int, c1: Int, r2: Int, c2: Int): Array<Array<Int>> = with(Extension) {
    val ansBoard = Array(r2-r1+1){Array(c2-c1+1){0}}
    val rangePredicate: (Point) -> Boolean = { it.y in r1..r2 && it.x in c1..c2 }
    var cnt = (r2-r1+1)*(c2-c1+1)

    var cur = Point(0, 0) // 초기 좌표
    var num = 1

    while (cnt > 0) {
        cur.takeIf(rangePredicate) // (r1, r2)~(c1, c2) 범위에 포함된다면, 저장해주자.
            ?.run {
                ansBoard[y-r1][x-c1] = num
                cnt--
            }
        cur = move.next(cur)
        num++
    }

    return ansBoard
}

private object Extension {
    val Point.y: Int
        get() = first
    val Point.x: Int
        get() = second
    operator fun Point.plus(other: Point): Point {
        return y+other.y to x+other.x
    }
}

private val move = object {
    fun next(point: Point): Point {
        val ret = nextPoint(point)
        //=> (nextY, nextX)

        // 방향 관련 정보 업데이트 로직
        i++ // 현재 방향(d)에서 현재까지, 직진한 거리 증가
        if(i == goLength){ // 방향 꺾는 상황
            i = 0
            d = (d+1)%4 // 다음 방향으로 업데이트
            flag = !flag
            if(!flag) goLength++ // 직진해야하는 거리 증가시킴.
        }

        return ret
    }

    private fun nextPoint(point: Point): Point = with(Extension) { return point + dirs[d] }

    private var i = 0 // (현재 방향에서) 현재까지 직진한 거리
    private var goLength = 1 // (현재 방향에서) 직진해야하는 거리
    private var d  = 0 // 현재 방향

    private var flag = false
    private val dirs = listOf(
        0 to 1,
        -1 to 0,
        0 to -1,
        1 to 0
    )
}


