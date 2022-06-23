package LCS

import kotlin.math.max

// longest common subsequence
fun lcs(x: String, y: String): Int{
    val dp = Array(x.length+1) { IntArray(y.length+1) }
    // dp[xi][yi]

    for(xi in 1..x.length) for(yi in 1..y.length){
        dp[xi][yi] = when(x[xi-1] == y[yi-1]) {
            true -> dp[xi - 1][yi - 1] + 1
            false -> max(dp[xi][yi-1], dp[xi-1][yi])
        }
    }

    return dp[x.length][y.length]
}

fun lcsWithString(x: String, y: String): Pair<Int, String> {
    val dp = Array(x.length+1) { IntArray(y.length+1) }

    for(xi in 1..x.length) for(yi in 1..y.length){
        dp[xi][yi] = when(x[xi-1] == y[yi-1]) {
            true -> dp[xi - 1][yi - 1] + 1
            false -> max(dp[xi][yi-1], dp[xi-1][yi])
        }
    }

    val ansStr: String = run {
        var xi = x.length; var yi = y.length
        val sb = ArrayDeque<Char>()

        while (xi > 0 && yi > 0){
            when(dp[xi][yi]) {
                dp[xi-1][yi] -> xi--
                dp[xi][yi-1] -> yi--
                else -> { xi--; yi--; sb.addFirst(x[xi])}
            }
        }

        sb.joinToString("")
    }

    return dp[x.length][y.length] to ansStr
}

fun main(){
    println("test start")
    test()
    println("test success")
}

fun test(){
    data class Tc(val x: String, val y: String, val expected: Any)

    val lcsTcList = listOf(
        Tc("ABCD", "AEBD", 3),
        Tc("", "ABC", 0),
        Tc("", "", 0),
        Tc("", "A", 0),
        Tc("A", "A", 1),
        Tc("A", "ABC", 1),
        Tc("ABC", "A", 1),
        Tc("ACAYKP", "CAPCAK", 4),
        Tc("KKKBCBCAAA", "KCKBCBCAKK", 7)
    )
    lcsTcList.forEach {  (x, y, expected) ->
        require(lcs(x, y) == expected)
    }

    val getLcsSeqTcList = listOf(
        Tc("ABCD", "AEBD", "ABD"),
        Tc("", "ABC", ""),
        Tc("", "", ""),
        Tc("", "A", ""),
        Tc("A", "A", "A"),
        Tc("A", "ABC", "A"),
        Tc("ABC", "A", "A"),
        Tc("ABC", "ABC", "ABC"),
        Tc("ACAYKP", "CAPCAK", "ACAK"),
        Tc("KKKBCBCAAA", "KCKBCBCAKK", "KKBCBCA")
    )
    getLcsSeqTcList.forEach { (x, y, expected) ->
        require(lcsWithString(x, y).second == expected)
    }

}