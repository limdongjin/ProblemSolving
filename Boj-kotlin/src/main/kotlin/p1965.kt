package main.kotlin.p1965

fun solve(boxes: List<Int>): Int{
    val n = boxes.size

    // dp[i] = i 번째 박스로 시작했을때, 최대 상자 수
    val dp = Array(n){-1}


    for(i in n-1 downTo 0)
        dp[i] = (dp.slice(i+1 until n)
            .filterIndexed { idx, _ ->  boxes[i] < boxes[i+1+idx] }
            .maxOrNull() ?: 0) + 1

    return dp.maxOrNull()!!
}

fun main(){
    readln() // n
    val boxes = readln().split(" ").map(String::toInt)

    println(solve(boxes))
}