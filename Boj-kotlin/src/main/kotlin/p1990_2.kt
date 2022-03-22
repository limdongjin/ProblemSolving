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
    val is_prime = Array<Boolean>(b+1) {true}
    is_prime[0] = false
    is_prime[1] = false

    val abRange = (a..b)
    val end = sqrt(is_prime.size.toDouble()).toInt()+1
    for(i in 2 until end)
        if(is_prime[i]) for(j in i*i until is_prime.size step i)
            is_prime[j] = false

    val ret = is_prime
        .asSequence()
        .mapIndexed { i, v -> i to v }
        .filter { it.first in abRange && it.second }
        .map { it.first.toString() }
        .filter { is_pal(it) }
        .joinToString(separator = "\n")

    println(ret)
    println(-1)
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (a, b) = readLine().split(' ').map { it.toInt() }

    solve(a, b)
}