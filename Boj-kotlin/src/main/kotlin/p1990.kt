package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.sqrt

inline private fun is_pal(str: String): Boolean {
     for(v in (0 until str.length/2)){
         if(str[v] != str[str.length - v - 1])
             return false
     }
    return true
}

private fun solve(a: Int, b: Int): Unit {
    if(a > 9989899){
        println(-1)
        return
    }
    val newB = b.takeIf { b < 9989899 } ?: 9989899

    val is_prime = BooleanArray(newB+1) {true}
    is_prime[0] = false
    is_prime[1] = false

    val end = sqrt(is_prime.size.toDouble()).toInt()+1
    for(i in 2 until end)
        if(is_prime[i]) for(j in i*i until is_prime.size step i)
            is_prime[j] = false

    val st = StringBuilder()
    for(i in a..newB)
        if(is_prime[i]){
            val strI = i.toString()
            if(is_pal(strI)) st.appendLine(strI)
        }

    st.appendLine("-1")
    println(st.toString())

}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (a, b) = readLine().split(' ').map { it.toInt() }

    solve(a, b)
}
