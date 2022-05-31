package main.kotlin.p20191

fun main() = with(System.`in`.bufferedReader()){
    test()
    val s = readLine()
    val t = readLine()

    println(solve(s, t))
}

fun solve(s: String, t: String): Int{
    val alphaT = List(26){ ArrayList<Int>() }
        .apply {
            for(i in t.indices)
                this[t[i] - 'a'].add(i)
        }

    var ccnt = 0
    var idx = 0
    for(i in 0 until 26){
        if(alphaT.isNotEmpty()){
            ccnt++
            idx = i
        }
    }
    if(ccnt == 1 && t[idx] == s[idx]) return (s.length+t.length-1)/t.length

    var cnt = 1
    var pos = -1
    var before = -1
    for(i in s.indices){
        val target = s[i] - 'a'
        if(alphaT[target].isEmpty()) return -1

        var left = 0
        var right = alphaT[target].size
        while(left < right){
            val mid = (left+right)/2
            if(before < alphaT[target][mid]) right = mid
            else left = mid+1
        }
        pos = left
        if(pos == alphaT[target].size){
            cnt++
            pos = 0
        }
        before = alphaT[target][pos]
    }

    return cnt
}

fun test(){
    require(solve("caa", "ac") == 3)
    require(solve("cab", "acca") == -1)
}