package main.kotlin.p2078

fun main() {
    val (a, b) = readln().split(" ").map(String::toInt)

    solve(a, b)
        .also { println("${it.first} ${it.second}") }
}

fun solve(a: Int, b: Int): Pair<Int, Int> {
    val cnt = object {
        var left = 0
        var right = 0
    }

    val cur = object {
        var a = a
        var b = b
    }

    while (cur.a != 1 || cur.b != 1) when(cur.a > cur.b) { // is Left
        true -> {
            cnt.left++
            cur.a = cur.a - cur.b
        }
        false -> {
            cnt.right++
            cur.b = cur.b - cur.a
        }
    }

    return cnt.left to cnt.right
}