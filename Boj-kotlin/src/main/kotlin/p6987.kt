package main.kotlin.p6987

import java.io.BufferedReader
import java.io.InputStreamReader

val match = Array(6) { Array(3) { 0 } }
val expected = Array(6) { Array(3) { 0 } }
//val gamePredicate = { // 병목점
//    (0 until 6).all { y ->
//        (0 until 3).all { x -> match[y][x] == expected[y][x] }
//    }
//}
val team1 = arrayOf(0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4)
val team2 = arrayOf(1, 2, 3, 4, 5, 2, 3, 4, 5, 3, 4, 5, 4, 5, 5 )
val ans = Array(4) { 0 }

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    repeat(4){ t ->
        val inp = readLine().split(" ").map(String::toInt)
        var i = 0
        for(y in 0 until 6 ) for(x in 0 until  3)
            match[y][x] = inp[i++]

        dfs(t, 0)
    }

    print(ans.joinToString(" "))
}

fun dfs(t: Int, round: Int) {
    if(round == 15){
        if(ans[t] != 0) return
        for(y in 0 until 6) for(x in 0 until 3)
            if(match[y][x] != expected[y][x])
                return

        ans[t] = 1
        return
    }

    val t1 = team1[round]
    val t2 = team2[round]

    expected[t1][0]++
    expected[t2][2]++
    dfs(t, round + 1)
    expected[t1][0]--
    expected[t2][2]--

    expected[t1][1]++
    expected[t2][1]++
    dfs(t, round + 1)
    expected[t1][1]--
    expected[t2][1]--

    expected[t1][2]++
    expected[t2][0]++
    dfs(t, round + 1)
    expected[t1][2]--
    expected[t2][0]--
}
