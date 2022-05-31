package main.kotlin.p1985

import java.io.BufferedReader
import java.io.InputStreamReader

private const val friends = "friends"
private const val nothing = "nothing"
private const val almost = "almost friends"

fun main() //= with(System.`in`.bufferedReader()){
    = with(BufferedReader(InputStreamReader(System.`in`))){
//    test()
    val pairs = List(3){
        readLine().split(" ").let { it[0] to it[1] }
    }
    pairs.forEach {
        println(solve(it.first, it.second))
    }
}

fun solve(s1: String, s2: String): String {
    val minusPlusPredicate = { s: CharArray, i: Int -> s[i] > '0' && s[i+1] < '9' }
    val plusMinusPredicate = { s: CharArray, i: Int -> s[i] < '9' && s[i+1] > '0' }
    val friendsPredicate: (CharArray, CharArray) -> Boolean = { x, y -> x.toSet() == y.toSet() }
    val minusPlusOperation = { s: CharArray, i: Int -> s[i]--; s[i+1]++ }
    val plusMinusOperation = { s: CharArray, i: Int -> s[i]++; s[i+1]-- }

    val s1Chars = s1.toCharArray()
    val s2Chars = s2.toCharArray()

    if(friendsPredicate(s1Chars, s2Chars))
        return friends

    for(idx1 in 0..s1.length-2){
        if(minusPlusPredicate(s1Chars, idx1)){
            minusPlusOperation(s1Chars, idx1)
            if(friendsPredicate(s1Chars, s2Chars) && s1Chars[0] != '0') return almost
            plusMinusOperation(s1Chars, idx1)
        }

        if(plusMinusPredicate(s1Chars, idx1)){
            plusMinusOperation(s1Chars, idx1)
            if(friendsPredicate(s1Chars, s2Chars)) return almost
            minusPlusOperation(s1Chars, idx1)
        }
    }

    for(idx2 in 0..s2.length-2){
        if(minusPlusPredicate(s2Chars, idx2)){
            minusPlusOperation(s2Chars, idx2)
            if(friendsPredicate(s1Chars, s2Chars) && s2Chars[0] != '0') return almost
            plusMinusOperation(s2Chars, idx2)
        }

        if(plusMinusPredicate(s2Chars, idx2)){
            plusMinusOperation(s2Chars, idx2)
            if(friendsPredicate(s1Chars, s2Chars)) return almost
            minusPlusOperation(s2Chars, idx2)
        }
    }

    return nothing
}

private fun test(){
    require(solve("123" ,"32331313323213") == friends)
    require(solve("137", "470") == nothing)
    require(solve("123", "2223042") == almost)
}