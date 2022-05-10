package main.kotlin.p3019
// 3019 테트리스

import java.io.BufferedReader
import java.io.InputStreamReader

private typealias Block = List<Pair<Int, Int>>
private typealias Pos = Pair<Int, Int>

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val (c, p) = readLine()!!.split(" ").map(String::toInt)
    val heights = readLine()!!.split(" ").map(String::toInt)

    println(Solver(c, p, heights).solve())
}

class Solver(val c: Int, val p: Int, val heights: List<Int>) {
    val board = Array(111){ Array(c){ false } }
        .apply {
            heights.forEachIndexed { col, height ->
                repeat(height) { y -> this[y][col] = true }
            }
        }

    private val blocks: List<Block> = getRotatedBlocks(blockTypes[p-1])

    fun solve(): Int {
        var ans = 0

        for (col in 0 until c)
            blocks.forEach { block ->
                val bottomLeft = Pos(heights[col], col)

                // col 열의 한칸 위에 block 을 놓는다. 즉, bottomLeft 위치에 블록의 왼쪽아래 부분을 놓는다.
                // 그릴 수 없는 위치라면, continue
                // unDrawable if (범위초과 or 이미 채워진 칸)
                draw(bottomLeft, block)
                    .takeIf { drawable -> drawable } ?: return@forEach

                // 게임 규칙 체크
                if(predicateForGame(this.board)) ans++

                // 복구
                unDraw(bottomLeft, block)
            }

        return ans
    }

    private fun draw(bottomLeft :Pos, block: Block): Boolean {
        val (y, x) = bottomLeft
        val tmpBlock = mutableListOf<Pos>() // rollback 을 위한 tmp
        val rollback: () -> Boolean = { unDraw(bottomLeft, tmpBlock); false }

        block.forEach { (dy, dx) ->
            // IF 범위 초과, THEN rollback
            val ny = (y + dy).takeIf { it >= 0 } ?: return rollback()
            val nx = (x + dx).takeIf { it in 0 until c } ?: return rollback()

            // IF 이미 채워진 칸, THEN rollback()
            if(board[ny][nx]) return rollback()

            board[ny][nx] = true
            tmpBlock.add(dy to dx)
        }

        return true
    }

    private fun unDraw(bottomLeft: Pos, block: Block) {
        val (y, x) = bottomLeft

        block.forEach { (dy, dx) ->
            val ny = (y + dy)
            val nx = (x + dx)

            board[ny][nx] = false
        }
    }

    companion object {
        private fun predicateForGame(board: Array<Array<Boolean>>): Boolean {
            val c = board[0].size

            for (x in 0 until c) {
                var y = 0
                var value = board[y][x]

                // value(=board[0][x]) 값과 다른 값이 나올때 까지 y++
                while (y in board.indices && board[y][x] == value){ y++ }

                // case 비어있는 열 또는 가득찬 열
                if(y !in board.indices) continue

                value = !value

                while (y in board.indices)
                    if(board[y++][x] != value) return false
            }

            return true
        }

        private fun getRotatedBlocks(block: Block) =
            List(4) { rotate90(block, it) }
                .map(::blockNormalize)
                .distinctBy { it.toSet() }

        private fun rotate90(block: Block, times: Int = 1): Block {  // (y', x') = (-x, y)
            var newBlock = block.toList()
            repeat(times) { newBlock = newBlock.map { pos -> -pos.second to pos.first } }
            return newBlock
        }

        // 블록의 맨 아래에 있으면서 왼쪽에 있는 칸이 (0, 0) 좌표에 놓이도록 평행이동한다.
        // 평행 이동된 블록을 반환한다.
        private fun blockNormalize(block: Block) =
            block.minWithOrNull(compareBy({ it.first }, { it.second }))!!
                 .let { (minY, minX) ->
                     block.map { it.first - minY to it.second - minX }
                 }

        private val blockTypes = listOf(
            // block 1
            listOf(
                0 to 0,
                1 to 0,
                2 to 0,
                3 to 0
            ),

            // block 2
            listOf(
                0 to 0,
                0 to 1,
                1 to 0,
                1 to 1
            ),

            // block 3
            listOf(
                0 to 0,
                0 to 1,
                1 to 1,
                1 to 2
            ),

            // block 4
            listOf(
                0 to 0,
                0 to 1,
                1 to -1,
                1 to 0
            ),

            // block 5
            listOf(
                0 to 0,
                0 to 1,
                0 to 2,
                1 to 1
            ),

            // block 6
            listOf(
                0 to 0,
                0 to 1,
                0 to 2,
                1 to 2
            ),

            // block 7
            listOf(
                0 to 0,
                1 to 0,
                0 to 1,
                0 to 2
            )
        )

    } // end companion object
} // end class Solver