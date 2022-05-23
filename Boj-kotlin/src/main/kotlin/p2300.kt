package main.kotlin.p2300

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.abs
import kotlin.math.max
import kotlin.math.min

// x, y
typealias Pos = Pair<Int, Int>
const val INF = 987654321

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val buildings = List<Pos>(n) {
        readLine().split(" ").map(String::toInt)
            .run { this[0] to abs(this[1]) } // 음수 y값은 양수로
    }

    println(solve(n, buildings))
}

fun solve(n: Int, buildings: List<Pos>): Int {
    val sorted = buildings.sortedBy { it.first }

    // dp[kExclusive] = (0 until kExclusive) 범위의 건물이 모두 포함 되도록 설치 하기 위한, 최소 비용
    val dp = IntArray(n+1) { INF }
        .apply {
            this[0] = 0
            this[1] = sorted[0].second * 2
        }

    for(rightExclusive in 2..n){
        // maxHeight: (left..rightExclusive) 범위의 건물 높이 중 최대 높이
        var maxHeight = sorted[rightExclusive-1].second

        val range = (rightExclusive-1 downTo 0)
        dp[rightExclusive] = range.minOf { left ->
            maxHeight = max(maxHeight, sorted[left].second)
            dp[left] + calcComWidth(sorted[left], sorted[range.first], maxHeight)
        }
        // Equivalent to:
        //   dp[rightExclusive] = min( dp[left] + max(diffXBetween, maxHeightBetween))
        //      , For All left in (0..rightExclusive-1)
    }

    return dp[n]
}

/**
* Returns: left 번째 건물 부터 right 번째 건물 까지 포함하는 기지국의 통신폭
*/
fun calcComWidth(leftB: Pos, rightB: Pos, maxHeightBetween: Int): Int =
    max(maxHeightBetween * 2, rightB.first - leftB.first) // max(최대 높이, x 축 거리)
