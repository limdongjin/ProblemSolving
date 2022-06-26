package main.kotlin.p2473

import kotlin.math.abs

fun main() = with(System.`in`.bufferedReader()){
    fun readLongs() = readLine().split(" ").map(String::toLong)
    val n = readLine().toInt()
    val nums = readLongs()

    solve(n, nums).run { println("$first $second $third") }
}

fun solve(n: Int, nums: List<Long>): Triple<Long, Long, Long> {
    return nums.sorted().run {
        val ansTriple = longArrayOf(get(0), get(1), get(2))
        var ansAbsSum = abs(ansTriple.sum())

        topLoop@ for (i in 0..n-3) {
            var l = i+1; var r = n-1

            while (l < r){
                val candidate = longArrayOf(get(i), get(l), get(r))
                val s = candidate.sum()

                if(abs(s) < ansAbsSum) candidate.copyInto(ansTriple).also { ansAbsSum = abs(it.sum()) }
                if(ansAbsSum == 0L) break@topLoop

                when(s < 0L){ true -> l++; false -> r-- }
            }
        }

        return@run ansTriple
    }
    .let { Triple(it[0], it[1], it[2])  }
}
