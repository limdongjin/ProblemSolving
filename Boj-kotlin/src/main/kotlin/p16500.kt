package main.kotlin.p16500

import java.io.BufferedReader
import java.io.InputStreamReader
typealias Predicate = () -> Boolean

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val s = readLine()!!
    val n = readLine()!!.toInt()
    val arr = Array(n) { readLine()!! }

    print(solve(s, n, arr))
}

private fun solve(s: String, n: Int, arr: Array<String>): Int {
    val checkArr = Array(s.length+1) { false }
    checkArr[0] = true

    for(i in s.indices){
        val prefixL = i + 1
        for(j in 0 until n){
            val predicate1: Predicate = { prefixL >= arr[j].length }
            val predicate2: Predicate = { s.substring(i-arr[j].length +1, i+1) == arr[j] }
            val predicate3: Predicate = { checkArr[prefixL-arr[j].length] }
            if(predicate1() && predicate2() && predicate3()){
                checkArr[prefixL] = true
                break
            }
        }
    }

    return if(checkArr[s.length]) 1 else 0
}
