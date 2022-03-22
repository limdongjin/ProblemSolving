package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

// 계란으로 계란치기

private fun solve(eggs: List<List<Int>>): Int{
    var ans = 0
    val n = eggs.size
    val eggsStatus = eggs.map { it.toTypedArray() }.toTypedArray()

    fun recurs(cur: Int) {
        if (cur >= n) {
            ans = max(ans, eggsStatus.count { it[0] <= 0 })
            return
        }
        if(eggsStatus[cur][0] <= 0) {
            recurs(cur+1)
            return
        }
        var flag = false
        for (idx in eggsStatus.indices) {
            if (idx == cur || eggsStatus[idx][0] <= 0) continue
            eggsStatus[cur][0] -= eggsStatus[idx][1]
            eggsStatus[idx][0] -= eggsStatus[cur][1]
            flag = true
            recurs(cur + 1)
            eggsStatus[idx][0] += eggsStatus[cur][1]
            eggsStatus[cur][0] += eggsStatus[idx][1]
        }
        if (!flag) recurs(n)
    }

    recurs(0)

    return ans
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine()!!.toInt()
    val eggs = (1..n).map {
        readLine()!!.split(" ").map { it.toInt() }
    }

    println(solve(eggs))
}