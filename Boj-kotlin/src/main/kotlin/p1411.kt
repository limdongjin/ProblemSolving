package main.kotlin.p1411

fun main() = with(System.`in`.bufferedReader()){
    test()
    val n = readLine().toInt()
    val words = List(n) { readLine() }

    println(solve(n, words))
}

fun solve(n: Int, words: List<String>): Int {
    val candiates = sequence {
        for (i in words.indices) for (j in i + 1 until words.size)
            yield(words[i] to words[j])
    }

    return candiates.count(::isSimilarPair)
}

fun isSimilarPair(pair: Pair<String, String>): Boolean {
    return pair
        .takeIf { pair.first.length == pair.second.length }
        ?.let { it.first.zip(it.second) }
        ?.let {
            val m1 = mutableMapOf<Char, Char>()
            val m2 = mutableMapOf<Char, Char>()

            it.forEach { (ach, bch) ->
                when {
                    !m1.contains(ach) && !m2.contains(bch) -> {
                        m1[ach] = bch
                        m2[bch] = ach
                    }
                    m1[ach] != bch -> return false
                }
            }
            true
        }
        ?: false
}

fun test(){
    require(
        solve(
            n=5,
            words = listOf(
                "aa",
                "ab",
                "bb",
                "cc",
                "cd"
            )
        ) == 4
    )
}