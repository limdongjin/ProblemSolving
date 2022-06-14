package main.kotlin.p14629

import kotlin.math.abs
import kotlin.math.min

fun main(){
    val n = readln().toLong()
    println(solve(n))
}

fun solve(n: Long): Long {
    if(n >= 9_876_543_210L){
        return 9_876_543_210L
    }
    val nStr = n.toString().takeUnless { it.toSet().size == it.length } ?: return n
    var ret = 999L
    val l = nStr.length
    val used = BooleanArray(10)
    val perm = CharArray(10)
    var diffMin = 9876543210L

    fun go(idx: Int){
        if(idx == l){
            var num = 0L
            for(i in 0 until l){
                num *= 10L

                num += Character.getNumericValue(perm[i]).toLong()
            }

            if(diffMin > abs(num-n)){
                diffMin = abs(num - n)
                ret = num
            }
            return
        }

        for(i in 0..9){
            if(used[i]) continue
            used[i] = true
            perm[idx] = ('0'+i)
            go(idx+1)
            used[i] = false
        }
    }
    go(0)

    return ret
}