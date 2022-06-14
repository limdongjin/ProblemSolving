package main.kotlin.p12859

fun nextPermutations(a: Array<Int>): Boolean {
    val k = (0 until  a.size-1)
        .lastOrNull { a[it] < a[it+1] } ?: return false

    val i = (k+1 until a.size)
        .last { a[k] < a[it] }

    a[i].also { a[i] = a[k] }.also { a[k] = it }
    a.reverse(k+1, a.size)

    return true
}

fun allPermutations(a: Array<Int>): List<Array<Int>> {
    val ret = mutableListOf<Array<Int>>()

    do {
        ret.add(a.clone())
    }while (nextPermutations(a))

    return ret
}

fun solve(a: Int, b: Int, c: Int = 0): Int{
    val cache = mutableMapOf<Triple<Int, Int, Int>, Int>()
    val ddd = allPermutations(arrayOf(1, 3, 9))
    val posOrZero: (Int) -> Int = { it.takeIf { it >= 0 } ?: 0 }

    fun go(aa: Int, bb: Int, cc: Int): Int {
        if(aa == 0 && bb == 0 && cc == 0) return 0

        val cur = Triple(aa, bb, cc).takeUnless { cache.contains(it) }
                                        ?: return cache[Triple(aa, bb, cc)]!!

        cache[cur] = ddd.minOf { (da, db, dc) ->
            go(posOrZero(aa - da), posOrZero(bb - db), posOrZero(cc - dc)) + 1
        }

        return cache[cur]!!
    }

    return go(a, b, c)
}


fun main(){
    val n = readln().toInt()
    val scvList = readln().split(" ").map(String::toInt)

    println(solve(scvList.getOrElse(0){0},
        scvList.getOrElse(1){0},
        scvList.getOrElse(2){0}
    ))
}
