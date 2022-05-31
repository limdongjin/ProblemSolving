package main.kotlin.p25049

import kotlin.math.max

fun main() = with(System.`in`.bufferedReader()) {
    require(solve(n = 6, p = listOf(3, 2, 5, 1, 4, 2)) == 34L)
    require(solve(n = 7, p = listOf(-1, 2, 3, -8, 6, -2, 5)) == 19L)
    val n = readLine().toInt()
    val p = readLine().split(" ").map(String::toLong)

    println(solve(n, p))
}

fun solve(n: Int, p: List<Long>): Long {
    // leftDp[i]: 고를 수 있는 최대 구간합 in (0..i 구간)
    val leftDp = LongArray(n) { -1 }
        .apply {
            set(0, p[0])
            // cur: p[i] 를 포함한 구간 중 최대 구간합 in (0..i 구간)
            var cur = p[0]

            for(i in 1..p.lastIndex){
                // cur = max(p[i]만 포함하는 구간, 이전 구간+p[i])
                cur = max(p[i], cur + p[i])

                // leftDp[i] = max( 0~i-1 에서의 최대 구간합, p[i]를 포함하는 최대 구간합 )
                set(i, max(get(i-1), cur))
            }
        }
    // rightDp[i]: 고를 수 있는 최대 구간합 in (i..n-1)
    val rightDp = LongArray(n) { -1 }
        .apply {
            set(n-1, p[n-1])
            var cur = p[n-1]
            for(i in n-2 downTo 0){
                cur = max(p[i], cur + p[i])
                set(i, max(get(i+1), cur))
            }
        }

    return p.sum() + maxOf(leftDp
                                .zip(rightDp.slice(1 until n))
                                .maxOf { it.first + it.second },
                            leftDp[n-1],
                            0L)
}
