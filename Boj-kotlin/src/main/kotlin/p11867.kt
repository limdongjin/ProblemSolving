package main.kotlin

fun main(){
    val (n, m) = readln().split(" ").map(String::toInt)
    println(when(n % 2 ==0 || m % 2 == 0){
        true -> "A"
        else -> "B"
    })
}