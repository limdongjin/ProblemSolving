package main.kotlin

fun main(){
    val n = readln().toInt()
    val s = readln()

    solve(n, s)
}

fun solve(n: Int, s: String) {
    var idx = s.indexOfFirst { it == '*' }
    var subStr1 = s.substring(0 until idx)
    var subStr2 = s.substring(idx+1 until s.length)
    repeat(n){
        val cmp = readln()
        if(subStr1.length + subStr2.length > cmp.length)
            println("NE")
        else if(cmp.startsWith(subStr1)){
            val e = cmp.substring(cmp.length - subStr2.length)
            if(e == subStr2) println("DA")
            else println("NE")
        } else println("NE")
    }
}