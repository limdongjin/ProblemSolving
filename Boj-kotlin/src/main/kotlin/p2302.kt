package main.kotlin.p2302

fun main(){
    val n = readln().toInt()
    val m = readln().toInt()
    val vipList = List(m) { readln().toInt() }

    println(solve(n, m, vipList))
}

fun solve(n: Int, m: Int, vipList: List<Int>): Int {
    val dp = IntArray(n+1)
        .apply {
            this[0] = 1
            this[1] = 1
            this[2] = 2
        }
    for(i in 3..n)
        dp[i] = dp[i-1] + dp[i-2]

    var ret = 1
    var p = 0
    vipList.forEach { vip ->
        ret *= dp[vip-p-1]
        p = vip
    }

    return ret * dp[n-p]
}
