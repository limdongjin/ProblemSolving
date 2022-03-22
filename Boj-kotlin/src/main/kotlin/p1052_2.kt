package main.kotlin

import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*

private inline fun IntArray.myindexOfFirst(start: Int, predicate: (Int) -> Boolean): Int {
    for (index in (start until this.size)) {
        if (predicate(this[index])) {
            return index
        }
    }
    return -1
}

private fun solve(n: Int, k: Int): Int{
    if(n <= k) return 0
    if(n.countOneBits() == 1) return 0

    var curN = n
    var curK = k

    while(curN > 0 && curK > 1 && curN > curK){
        curN -= curN.takeHighestOneBit()
        curK--
    }
    if(curN <= curK) return 0
    if(curN.countOneBits() == 1) return 0

    return curN.takeHighestOneBit().shl(1) - curN
}

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (n, k) = readLine().split(' ').map {it.toInt()}
    println(solve(n, k))

    val examples = hashMapOf<Pair<Int, Int>, Int>(
        (3 to 1) to 1,
        (1000000 to 1) to 48576, // 10^6
        (1000000 to 5) to 15808,
        (1000000 to 6) to 448,
        (13 to 2) to 3,
        (10 to 5) to 0,
        (17 to 1) to 15,
        (9 to 1) to 7,
        (2 to 1) to 0,
        (4 to 2) to 0,
        (6 to 3) to 0,
        (7 to 1) to 1,
        (9 to 1) to 7,
        (10 to 1) to 6,
        (3 to 5) to 0,
        (16 to 1) to 0,
        (1 to 1) to 0,
        (4 to 1) to 0,
        (8 to 1) to 0,
        (77 to 8) to 0,
        (100 to 1) to 28,
        (100 to 2) to 28,
        (100 to 3) to 0,
        (100 to 4) to 0,
    )

    examples.forEach {
        (inpu, expected) ->
            solve(inpu.first, inpu.second)
                .also { if(it != expected) println("$inpu not eq $it")  }

    }

    // 15,868 = 2^15-(1000000-2^19-2^18-2^17-2^16)
}