package main.kotlin.p1988

import kotlin.math.max

fun main() = with(System.`in`.bufferedReader()){
    val (n, b) = readLine()!!.split(" ").map(String::toInt)

    val nums = List(n){ readLine()!!.toLong() }

    println(solve(nums, n, b))
}
// TODO 다시 풀어보기
// https://gall.dcinside.com/mgallery/board/view/?id=ps&no=5888
fun solve(nums: List<Long>, n: Int, b: Int): Long {
    val accSum = LongArray(n+1){ 0 }
    for(i in 1..n){
        accSum[i] = accSum[i-1] + nums[i-1]
    }
    val dp1 = LongArray(n+1){ 0 }
    val dp2 = LongArray(n+1){ 0 }
    for(i in 1 until n) {
        dp1[i] = accSum[i+1] - accSum[i]
    }

    for(i in 3..b){
        var lastMax = 0L
        dp2[i-1] = accSum[i]-accSum[1]
        for(j in i until n){
            lastMax = max(lastMax, dp1[j-2])
            dp2[j] = max(dp1[j-1]+accSum[j+1]-accSum[j], lastMax)
        }
        for(j in 0 until n) dp1[j] = dp2[j]
    }
    val ans = dp1.maxOrNull() ?: 0L

    return ans
}
