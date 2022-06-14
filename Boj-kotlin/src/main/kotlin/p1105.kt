package main.kotlin.p1105

fun main() {
//    test()
    val (l, r) = readLine()!!.split(" ")
    println(solve(l, r))
}

fun solve(l: String, r: String): Int = when {
    l.length != r.length -> 0
    else -> l.commonPrefixWith(r).count { it == '8' }
}

// 구현1 (AC)
//fun _solve(l: String, r: String): Int {
//    if(l.length != r.length) return 0
//    var cnt = 0
//    for(i in l.indices){
//        when {
//            l[i] != r[i] -> break
//            l[i] == '8' -> cnt++
//        }
//    }
//
//    return cnt
//}
//
//fun test(){
//    require(solve("1", "10") == 0)
//    require(solve("88", "88") == 2)
//    require(solve("800", "899") == 1)
//    require(solve("8808", "8880") == 2)
//}
