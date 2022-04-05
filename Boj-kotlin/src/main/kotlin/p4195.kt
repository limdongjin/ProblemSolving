package main.kotlin.p4195

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

// 4195 친구 네트워크

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val t = readLine().toInt()
    repeat(t){
        val f = readLine().toInt()
        val rels = List(f){ readLine().split(" ").let { it[0] to it[1] } }
        solve(rels)
    }

}

class FindUnion(initSize: Int) {
    val size = Array(initSize){ 1 }
    private val parent = Array(initSize){ it }

    fun find(x: Int): Int {
        if(parent[x] == x) return x
        parent[x] = find(parent[x])
        return parent[x]
    }

    fun union(s1: Int, s2: Int){
        var a = find(s1)
        var b = find(s2)
        if(a != b){
            if(size[a] < size[b]) a.also { a = b }.also { b = it } // swap
            size[a] += size[b]
            parent[b] = a
        }
    }
}

fun solve(rels: List<Pair<String, String>>){
    val findUnion = FindUnion(rels.size*2)

    val id = mutableMapOf<String, Int>()
    var nextId = 0

    rels.forEach { (p1, p2) ->
        val a = id.getOrPut(p1) { nextId++ }
        val b = id.getOrPut(p2) { nextId++ }

        with(findUnion){
            union(a, b)
            println(max(size[find(a)], size[find(b)]))
        }
    }

}

