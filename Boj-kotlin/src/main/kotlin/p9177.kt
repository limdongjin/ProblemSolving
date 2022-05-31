package main.kotlin.p9177

fun main() = with(System.`in`.bufferedReader()){
    val n = readLine().toInt()
    repeat(n){
        val (s1, s2, s3) = readLine()!!.split(" ")
        val ans = if(solve(s1, s2, s3)) "yes" else "no"
        println("Data set ${it+1}: $ans")
    }
}

fun solve(s1: String, s2: String, s3: String): Boolean {
    val q = ArrayDeque<Pair<Int, Int>>()
    val visited = Array(s1.length+1){ BooleanArray(s2.length+1) }
    q.addLast(0 to 0)
    visited[0][0] = true

    val predicateS1CharSelect: (Pair<Int, Int>) -> Boolean = { p ->
        p.first in s1.indices && s1[p.first] == s3[p.first+p.second] && !visited[p.first+1][p.second]
    }
    val predicateS2CharSelect: (Pair<Int, Int>) -> Boolean = { p ->
        p.second in s2.indices && s2[p.second] == s3[p.first+p.second] && !visited[p.first][p.second+1]
    }
    val predicateSuccess: (Pair<Int, Int>) -> Boolean = { p ->
        p.first + p.second == s3.length
    }

    while(q.isNotEmpty()){
        val p = q.removeFirst()

        if (predicateSuccess(p)) return true
        if (predicateS1CharSelect(p)){
            val selected = p.first+1 to p.second
            visited[selected.first][selected.second] = true
            q.addLast(selected)
        }
        if (predicateS2CharSelect(p)){
            val selected = p.first to p.second+1
            visited[selected.first][selected.second] = true
            q.addLast(selected)
        }
    }

    return false
}
