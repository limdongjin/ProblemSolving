package main.kotlin.p3107

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val ip = readLine()!!
    println(solve(ip))
}

fun solve(ip: String): String {
    // 4 자리가 아닌 그룹은 앞에 0을 추가 한다.
    fun zeroFormatting(s: String): String {
        val added = (0 until (4 - s.length)).joinToString("") { "0" }
        return "$added$s"
    }
    // left + "::" + right

    fun restore(groups: List<String>, range: IntRange) =
        groups.slice(range).map { zeroFormatting(it) }

    val groups = ip.split(":")

    val midGroupIdx = groups.indexOf("").takeIf { it != -1 }
        ?: return restore(groups, groups.indices).joinToString(":")

    val leftIp = restore(groups, 0 until midGroupIdx)
    val startRight =
        if(midGroupIdx+1 in groups.indices && groups[midGroupIdx+1] == "")
            midGroupIdx+2
        else
            midGroupIdx+1

    val rightIp = restore(groups, startRight until groups.size)
    val midIpLength = 32 - (leftIp.size + rightIp.size)*4

    val zeroGroup = (0 until 4).joinToString("") { "0" }
    val midIp = (0 until midIpLength / 4).joinToString(":") { zeroGroup }

    val ans = leftIp + midIp + rightIp

    return ans.joinToString(":")
}