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
        val minTriple: Array<Long> = arrayOf(get(0), get(1), get(2))
        var minAbsSum = abs(minTriple.sum())
        fun updateAns(f: Long, s: Long, t: Long) {
            minTriple.apply { set(0, f); set(1, s); set(2, t) }
            minAbsSum = abs(minTriple.sum())
        }

        topLoop@ for (i in 0..n-3) {
            var l = i+1; var r = n-1

            while (l < r){
                val s = get(i)+get(l)+get(r)
                if(abs(s) < minAbsSum) updateAns(get(i), get(l), get(r))
                if(minAbsSum == 0L) break@topLoop

                when(s < 0L){ true -> l++; false -> r-- }
            }
        }

        return@run minTriple
    }
    .let { Triple(it[0], it[1], it[2])  }
}
