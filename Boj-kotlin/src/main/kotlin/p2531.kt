package main.kotlin.p2531

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

// 2531 회전 초밥

fun solve(n: Int, d: Int, k: Int, c: Int, belt: List<Int>): Int {

    // 현재 위치에서 먹을 수 있는, (초밥_id, 개수) Map
    val eatenMap = mutableMapOf<Int, Int>()

    fun MutableMap<Int, Int>.inc(key: Int) = merge(key, 1, Int::plus)
    fun MutableMap<Int, Int>.decOrRemove(key: Int) {
        this[key] = this[key]!! - 1
        if(this[key] == 0) this.remove(key)
    }
    
    // 현재 위치에서 먹을 수 있는, 초밥의 가짓수의 최댓값
    fun calculate(m: MutableMap<Int, Int>, coupon: Int = c) =
        (m.count() + if (m.contains(coupon)) 0 else 1)

    // INIT: (0 ~ k-1) 위치 
    var right = k-1
    (0..right).forEach { eatenMap.inc(belt[it]) }

    // ans: 먹을 수 있는 최대 개수
    var ans = calculate(eatenMap)

    // REMOVE 왼쪽음식
    eatenMap.decOrRemove(belt[0])
    
    for(left in 1 until belt.size){
        // ADD 오른쪽 음식
        right += 1
        eatenMap.inc(belt[right%belt.size])
        
        ans = max(ans, calculate(eatenMap))

        // REMOVE 왼쪽음식
        eatenMap.decOrRemove(belt[left])
    }

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