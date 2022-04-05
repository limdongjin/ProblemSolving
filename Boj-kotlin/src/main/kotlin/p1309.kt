package main.kotlin

fun main(){
    val n = readln().toInt()

    var prev0 = 1
    var prev1 = 1
    var prev2 = 1
    repeat(n-1){
        val c0 = (prev0+prev1+prev2)%9901
        val c1 = (prev0+prev2)%9901
        val c2 = (prev0+prev1)%9901

        prev0 = c0
        prev1 = c1
        prev2 = c2
    }

    println((prev0+prev1+prev2)%9901)
}