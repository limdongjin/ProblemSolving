package main.kotlin.p8911
import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.abs
import kotlin.math.max
import kotlin.math.min

// (x, y)
val dirs = listOf(
    0 to 1, // up
    1 to 0, // right
    0 to -1,// down
    -1 to 0 // left
)

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val n = readLine()!!.toInt()

    repeat(n) {
        val commands = readLine()!!
        println(solve(commands))
    }
}

data class Pos(var x: Int, var y: Int)
fun solve(commands: String): Int {
    val cur = object {
        var pos = Pos(0, 0)
        var d = 0

        val move: (Int) -> Unit = { pos.x += dirs[d].first*it; pos.y += dirs[d].second*it }
        val changeDir = { v: Int -> d = (4+d+v)%4 }
    }

    var maxPos = Pos(0, 0)
    var minPos = Pos(0, 0)

    val updateMaxOrMin: (Pos) -> Unit = {
        maxPos.x = max(it.x, maxPos.x)
        maxPos.y = max(it.y, maxPos.y)
        minPos.x = min(it.x, minPos.x)
        minPos.y = min(it.y, minPos.y)
    }

    commands.forEach {
        when(it){
            'F' -> cur.move(1)
            'B' -> cur.move(-1)
            'L' -> cur.changeDir(-1)
            'R' -> cur.changeDir(1)
        }
        updateMaxOrMin(cur.pos)
    }

    return abs((maxPos.y - minPos.y)*(maxPos.x - minPos.x))
}
