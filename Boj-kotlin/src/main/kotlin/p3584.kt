package main.kotlin.p3584

fun main() = with(System.`in`.bufferedReader()) {
    repeat(readLine()!!.toInt()) {
        val n = readLine().toInt()
        val edges = List(n - 1) { readLine().split(" ").map(String::toInt).let { it[0] to it[1] } }
        val (a, b) = readLine().split(" ").map(String::toInt)

        println(solve(n, edges, a, b))
    }
}

fun solve(n: Int, edges: List<Pair<Int, Int>>, a: Int, b: Int): Int {
    // parents[b] = a
    val p = IntArray(n+1) { 0 }.apply {
        edges.forEach { (parent, child) ->
            this[child] = parent
        }
    }

    var curA = a; var curB = b
    val visited = BooleanArray(n+1)

    while(p[curA] != 0 || p[curB] != 0){
        if(curA != 0) visited[curA] = true
        if(curB != 0) visited[curB] = true

        when {
            p[curA] == p[curB] -> return p[curA]
            visited[p[curA]] -> return p[curA]
            visited[p[curB]] -> return p[curB]
        }

        curA = p[curA]
        curB = p[curB]
    }

    require(false)
    return -1
}
