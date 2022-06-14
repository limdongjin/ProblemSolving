package main.kotlin.p5052

fun main() = with(System.`in`.bufferedReader()){
    val t = readLine().toInt()

    repeat(t){
        val n = readLine().toInt()
        val phones = Array(n) { readLine() }

        println(when(solve(n, phones)){
            true -> "YES"
            else -> "NO"
        })
    }
}

fun solve(n: Int, phones: Array<String>): Boolean {
    phones.sort()
    for(k in 0 until phones.size-1){
        val curL = phones[k].length
        val nextL = phones[k+1].length
        if(curL >= nextL) continue
        if(phones[k+1].substring(0, curL) == phones[k]) return false
    }
    return true
}
