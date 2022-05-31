package main.kotlin.p1939

fun main() {
    val (n, m) = readln().split(" ").map(String::toInt)
    val bridges = List(m) {
        readln().split(" ").let { t ->
            Triple(t[0].toInt()-1, t[1].toInt()-1, t[2].toInt())
        }
    }

    val (start, end) = readln().split(" ").map(String::toInt).let {
        it[0] - 1 to it[1] - 1
    }

    println(solve(n, m, bridges, start, end))
}

fun solve(n: Int, m: Int, bridges: List<Triple<Int, Int, Int>>, start: Int, end: Int): Int {
    val graph = List(n+1) { ArrayList<Pair<Int, Int>>() }
        .apply {
            bridges.forEach {
                this[it.first].add(it.second to it.third)
                this[it.second].add(it.first to it.third)
            }
        }

    val q = ArrayDeque<Int>()

    fun bfs(w: Int): Boolean {
        q.clear()
        val visited = BooleanArray(n+1)

        visited[start] = true
        q.addLast(start)

        while (q.isNotEmpty()){
            val pos = q.removeFirst()
            if(pos == end) return true
            graph[pos].forEach { (to, ww) ->
                if(!visited[to] && ww >= w){
                    visited[to] = true
                    q.addLast(to)
                }
            }
        }
        return false
    }

    var ans = -1
    var low = 1
    var high = 1000000000

    while (low <= high){
        val mid = (low+high) / 2
        if(bfs(mid)){
            ans = mid
            low = mid + 1
        }else{
            high = mid - 1
        }
    }

    return ans
}


fun test(){
    require(
        solve(n=3, m=3, bridges = listOf(
            Triple(0, 1, 2),
            Triple(2, 0, 3),
            Triple(1, 2, 2))
            , start = 0, end = 2) == 3
    )


}

