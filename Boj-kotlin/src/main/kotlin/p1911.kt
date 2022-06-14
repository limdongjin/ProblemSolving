package main.kotlin.p1911

fun main() = with(System.`in`.bufferedReader()){
    val (n, l) = readLine().split(" ").map(String::toInt)
    val infos = List(n){ readLine().split(" ").let { it[0].toInt() to it[1].toInt() } }

    println(solve(n, l, infos))
}

fun solve(n: Int, l: Int, infos: List<Pair<Int, Int>>): Int{
    var cur = 0
    var ret = 0

    infos
        .sortedBy { it.first }
        .forEach {
            if(cur >= it.second - 1) return@forEach
            var begin = it.first
            val end = it.second

            when {
                cur >= it.first -> begin = cur + 1
                else -> cur = begin - 1
            }

            val diff = end - begin
            val num = when(diff%l == 0 && diff != 0){
                true -> diff / l
                else -> diff / l + 1
            }
            cur += l*num
            ret += num
        }

    return ret
}