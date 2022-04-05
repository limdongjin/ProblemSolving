package main.kotlin.p2531

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

// 2531 회전 초밥

fun solve(n: Int, d: Int, k: Int, c: Int, belt: List<Int>): Int {

    fun MutableMap<Int, Int>.inc(key: Int) = merge(key, 1, Int::plus)
    fun MutableMap<Int, Int>.decOrRemove(key: Int) {
        this[key] = this[key]!! - 1
        if(this[key] == 0) this.remove(key)
    }

    val window = object {
        var left = 0
        var right = k-1
    }

    // 현재 window 에서 먹을 수 있는, (초밥_id, 개수) Map
    val eaten = mutableMapOf<Int, Int>()
        .apply {
            // 초기상태: [0, k-1] 범위
            belt.subList(window.left, window.right+1)
                .forEach { this.inc(it) }
        }

    // 계산
    val calc: (MutableMap<Int, Int>) -> Int =
        { it.count() + if (it.contains(c)) 0 else 1 }

    // ans: 먹을 수 있는 최대 개수
    var ans = 0

    do {
        ans = max(ans, calc(eaten))

        with(window) {
            // REMOVE 왼쪽 초밥
            eaten.decOrRemove(belt[left++])

            // ADD 오른쪽 초밥
            eaten.inc(belt[(++right)%belt.size])
        }
    } while (window.left < belt.size)

    return ans
}

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    // n: 접시의 수
    // d: 초밥 가짓수
    // k: 연속해서 먹는 접시의 수
    // c: 쿠폰 번호
    val (n, d, k, c) = readLine().split(" ").map(String::toInt)
    val belt = List(n){ readLine().toInt() }

    println(solve(n, d, k, c, belt))
}