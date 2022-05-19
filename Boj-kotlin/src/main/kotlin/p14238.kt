package main.kotlin.p14238
import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val s = readLine()
    println(Solver(s).solve())
}

class Solver(val s: String) {
    val n = s.length
    val aCnt = s.count { it == 'A' }
    val bCnt = s.count { it == 'B' }
    val cCnt = s.count { it == 'C' }
    val ans = Array(n) { ' ' }

    // dp[a][b][c][pprev][prev]
    val dp = Array(n+1) {
        Array(n+1) {
            Array(n+1) { Array(3){ Array(3) { false } } }
        }
    }

    fun solve(): String {
        val success = go(a =0, b =0, c =0, prev =0, pprev =0)

        return when(success) {
            true -> ans.joinToString("")
            false -> "-1"
        }
    }

    fun go(a: Int, b:Int, c: Int, prev: Int, pprev: Int): Boolean {
        when {
            a == aCnt && b == bCnt && c == cCnt -> return true
            dp[a][b][c][pprev][prev] -> return false
        }

        dp[a][b][c][pprev][prev] = true
        if(a+1 <= aCnt){
            ans[a + b + c] = 'A'
            if(go(a+1, b, c, prev=0, pprev=prev)) return true
        }
        if(b+1 <= bCnt){
            ans[a+b+c] = 'B'
            if(prev != 1 && go(a, b+1, c, prev=1, pprev=prev)) return true
        }
        if(c+1 <= cCnt) {
            ans[a+b+c] = 'C'
            if(pprev != 2 && prev != 2 && go(a, b, c+1, prev=2, pprev=prev)) return true
        }
        return false
    }
}
