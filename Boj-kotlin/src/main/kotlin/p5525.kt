package main.kotlin.p5525

fun main() = with(System.`in`.bufferedReader()){
//    test()
    val n = readLine().toInt()
    val m = readLine().toInt()
    val s = readLine()

    println(solve(n, m, s))
}

fun solve(n: Int, m: Int, s: String): Int {
    var i = 1
    var ans = 0
    var ioiCnt = 0

    while(i < m-1){
        when(s.subSequence(i-1..i+1)) {
            "IOI" -> { ioiCnt++; i += 2 }
            else -> { ioiCnt = 0; i++ }
        }
        if(ioiCnt == n){ ans++; ioiCnt-- }
    }

    return ans
}
//
//fun test(){
//    require(solve(1, 13, "OOIOIOIOIIOII") == 4)
//    require(solve(2, 13, "OOIOIOIOIIOII") == 2)
//}