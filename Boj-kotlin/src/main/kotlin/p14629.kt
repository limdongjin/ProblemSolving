package main.kotlin.p14629

import kotlin.math.abs
import kotlin.math.min

fun main(){
//    println(permute(nums = intArrayOf(2,1,3,5,6)))
    // test()
    val n = readln().toLong()
    println(solve2(n))
}

fun solve2(n: Long): Long {
    if(n >= 9_876_543_210L) return 9_876_543_210L
    val l = n.toString().takeUnless { it.toSet().size == it.length }?.length ?: return n

    val combs = combinations(lst= ('0'..'9').toList(), r=l)
    var m = 9876543210L
    var p = 9876543210L
    combs.forEach {  comb ->
        val perms = permutations(comb)
        perms.forEach {
            if(abs(n-it) < m){
                m = abs(n-it)
                p = it
            }else if(abs(n-it) == m && it < p){
                p = it
            }
        }
    }

    return p

//   TLE...Memory Over // 9CL * L!
//    return combinations(lst= (0L..9L).toList(), r=l)
//        .flatMap(::permutations)
//        .minWithOrNull(compareFunc())!!
}

fun <T> combinations(lst: List<T>, r: Int): Sequence<List<T>> = sequence {
    val selected = Array<Boolean>(lst.size) { false }.apply {
        fill(true, lst.size-r, lst.size)
    }

    do {
        yield(lst.filterIndexed { i, _ -> selected[i] })
    } while(nextPermutation(selected))
}

fun permutations(lst: List<Char>) = sequence {
    val arr = lst.toTypedArray()
    do {
        yield(arr.joinToString("").toLong())
    }while (nextPermutation(arr))
}
fun <T: Comparable<T>> nextPermutation(arr: Array<T>): Boolean {
    // a[k] < a[k+1]
    val k = (0 until arr.size-1).lastOrNull { arr[it] < arr[it+1] } ?: return false

    // a[k] < a[i]
    val i = (k+1 until arr.size).last { arr[k] < arr[it] }

    // swap
    arr.swap(k, i)

    // reverse [k+1..]
    arr.reverse(k+1, arr.size)

    return true
}
fun <T> Array<T>.swap(i: Int, j: Int) = this[i].also { this[i] = this[j] }.let { this[j] = it }
/////////////////////////////////////////////////////////
fun test(){
    for(i in 1921831L..9999999999L){
        val ret1 = solve(i)
        val ret2 = solve2(i)
        println("$i 's ans1: $ret1")
        println("$i 's ans2: $ret2")

        require(ret1 == ret2)
    }
}
/////////////////////////////////////////////////////////
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