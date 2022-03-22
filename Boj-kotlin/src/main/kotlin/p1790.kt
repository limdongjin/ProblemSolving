package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.pow

private fun myPow(n: Int, k: Int): Int{
    var ret = 1
    repeat(k){
        ret *= n
    }
    return ret
}

private fun solve(n: Int, k: Int): Int {
     val seq = generateSequence(9) {it*10}
        .mapIndexed { index, v ->  v*(index+1) }
    val dig = (1..8).firstOrNull { k < seq.take(it).sum() }
    println(seq.take(8).sum())
    if(k == seq.take(8).sum()){
        return if(n >= 100000000 - 1) 9
        else -1
    }
    if(k > seq.take(8).sum() + 9) return -1

    if(dig == null){
        println("deb")
        val tmp = seq.take(8).sum()
        return if(n == 100000000){
            when (k) {
                tmp+1 -> 1
                else -> 0
            }
        } else -1
    }

    val kk = k - seq.take(dig-1).sum()

    if(kk == 0) return 9
    println("deb2")
    println(dig)
    println(kk)
    println(myPow(10, dig-1))
    println((10.0.pow(dig - 1).toInt() + (kk / dig) - 1 + (kk % dig)))
    println(myPow(10, dig-1) + (kk / dig) - 1 + (kk % dig))
    return (10.0.pow(dig - 1).toInt() + (kk / dig) - 1 + (kk % dig))
        .takeIf { it <= n }
        ?.run {
            return Character.getNumericValue(this.toString()[(kk - 1) % dig])
        }
        ?: -1
}
private fun solve2(n: Int, k: Int): Int{
    var finalNum: Long = 0
    var tmp = k.toLong()
    var cntLength: Long = 1
    var cntNum: Long = 9

    while (tmp > cntLength * cntNum) {
        tmp = tmp - cntLength * cntNum
        finalNum = finalNum + cntNum
        cntLength++
        cntNum *= 10
    }

    finalNum = finalNum + 1 + (tmp - 1) / cntLength
    if (finalNum > n) {
        return -1
    } else {
        return Character.getNumericValue(finalNum.toString()[((tmp - 1) % cntLength).toInt()])
    }
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    solve(1, 1)
    println(solve(100-1, 190-1))
    println(solve2(100-1, 190-1))
    println(solve(100000000, 788888889))
    println(solve2(100000000, 788888889))
    println(solve(100000000-1, 788888889-1))
    println(solve2(100000000-1, 788888889-1))


    return@with
    var n = -1
    var k = -1
    (100000000 downTo 1)
        .forEach { nn: Int ->
            (1000000000 downTo 1)
                .forEach { kk: Int ->
                    val s1 = solve(nn, kk)
                    val s2 = solve2(nn, kk)
                    println("$nn $kk $s1 $s2")
                    if(s1 != s2){
                        println("not equal.., nn=$nn kk=$kk sol1=$s1 sol2=$s2")
                        n = nn
                        k = kk
                        return@forEach
                    }
                }
        }

    println("ok")
    println("$n $k")
}