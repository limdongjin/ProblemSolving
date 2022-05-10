package main.kotlin.p2230

import kotlin.math.abs
import kotlin.math.max
import kotlin.math.min

fun main() {
    val (n, m) = readln().split(" ").map(String::toLong)
    val nums = List<Long>(n.toInt()) { readln().toLong() }

    println(solve(nums, m))
}

fun solve(nums: List<Long>, m: Long): Long {
    if(m == 0L) return 0L
    if(nums.size == 2) return abs(nums[0] - nums[1])

    val sortedA = nums.sorted()

    val w = object {
        var left = 0
        var right = 1
    }

    var ans = Long.MAX_VALUE

    while (w.right < sortedA.size){
        when(val diff = abs(sortedA[w.right] - sortedA[w.left])) {
            m -> return m
            in 0 until m -> w.right++
            else -> {
                ans = min(ans, diff)
                if(w.left + 1 == w.right) w.right++
                w.left++
            }
        }
    }

    return ans
}