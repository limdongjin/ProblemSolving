package main.kotlin.p17374

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max
import kotlin.math.min

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val t = readLine().toInt()

    repeat(t){
        val inp = readLine().split(" ").map(String::toInt)

        var p = inp[0]
        var q = inp[1]
        var a = inp[2]
        var b = inp[3]
        var c = inp[4]
        var d = inp[5]

        var coin = (q/c)*d
        p += (coin/b)*a
        coin %= b

        val x = (p-coin)/(a+b)
        val ans = max(
            min(coin+(b*x), p-(a*x)),
            min(coin+(b*(x+1)), p-(a*(x+1)))
        )
        println(ans)
    }
}