package main.kotlin.utils.matrix

typealias Board<T> = List<List<T>>
typealias MutableBoard<T> = Array<Array<T>>

typealias RotatedFunc<T> = (List<List<T>>) -> List<List<T>>

infix fun IntRange.cproduct(r2: IntRange) =
    sequence<Pair<Int, Int>> {
        for(k1 in this@cproduct) for(k2 in r2) yield(k1 to k2)
    }

// 시계 방향 90도 회전
fun <T> rotated90(board: Board<T>): Board<T> {
    val n = board.size; val m = board[0].size

    // inverseOfF :: (y, x) -> (-x, y)
    // [  y   x ]
    // |  0   1 |
    // | -1   0 |

    return (0 until m).map { y ->
        (0 until n).map { x -> board[n-1-x][y] } // trans[y][x] = original[n-1-x][y]
    }
}

// 시계 방향 90도 회전
inline fun <reified T> rotate90UsingTransform(lst: List<List<T>>): List<List<T>> {
    val n = lst.size; val m = lst[0].size

    // f :: (y, x) -> (x, -y)
    // [ y   x  ]
    // | 0  -1  |
    // | 1   0  |

    val rotateTransform: (Pos) -> Pos =
        { pos ->  Pos(pos.x to n-1-pos.y) } // trans[x][n-1-y] = original[y][x]

    return lst.transformed(newN=m, newM=n, transformNewYX = rotateTransform)
}
@JvmInline
value class Pos(val pair: Pair<Int, Int>){
    val y: Int
        get() = pair.first

    val x: Int
        get() = pair.second
}

//@JvmInline
//value class Board2<T>(val v: List<List<T>>)

fun <T> Board<T>.yxs() = sequence<Pos> {
    for(y in this@yxs.indices) for(x in this@yxs[y].indices) yield(Pos(y to x))
}

inline fun <reified T> Board<T>.transformed(
    newN: Int,
    newM: Int,
    crossinline transformNewYX: (Pos) -> Pos, // (y, x) -> (ny, nx)
): Board<T> {
//    TreeSe
    return this.yxs() // equivalent : for(y in this.indices) for(x in this[0].indices)
        // [ Pos,... ]
        .map { it to this[it.y][it.x] }
        // [ (Pos T), (Pos T), ...]
        .map { (pos, t) -> transformNewYX(pos) to t }
        // [ (NewPos T), (NewPos T), ... ]
        .let {
            val transformed: MutableBoard<T> = Array(newN) { Array<T>(newM){ this[0].first() } }
            it.forEach { (newPos, t) ->
                transformed[newPos.y][newPos.x] = t
            }

            transformed.map(Array<T>::toList)
        }
        // transformed: Board


//     val transformed: MutableBoard<T> = Array(newN) { Array<T>(newM){ this[0].first() } }
//     this.yxs()
//         .forEach { pos ->
//             val newPos = transformNewYX(pos)
//             transformed[newPos.y][newPos.x] = this[pos.y][pos.x]
//         }
//
//    return transformed.map { it.toList() }
}

val inPlaceRotate90UsingTranspose = object {
    fun <T> Array<Array<T>>.swap2D(a: Pair<Int, Int>, b: Pair<Int, Int>) =
        this[a.first][a.second]
            .also { this[a.first][a.second] = this[b.first][b.second] }
            .let { this[b.first][b.second] = it }

    fun <T> rotate90(arr: Array<Array<T>>){
        require(arr.size == arr[0].size)
        val n = arr.size

        // transpose
        for(y in 0 until n) for(x in y until n)
            arr.swap2D(y to x, x to y)

        // reverse each rows
        arr.onEach(Array<T>::reverse)
    }
}

val rotated90UsingWindowed = object {
    fun <T> rotate90(lst: List<List<T>>): List<List<T>> {
        val n = lst.size; val m = lst[0].size
        return (lst[0].indices cproduct lst.indices)
            .map { (y, x) -> lst[n-1-x][y] }
            .windowed(n, step = n)
            .toList()
    }
}

val rotated90UsingForLoop = object {
    // 런타임에 Generic T 에 접근하려면 inline fun <reified T> 를 붙여줘야한다...
    inline fun <reified T> rotated90(lst: List<List<T>>): List<List<T>> {
        val n = lst.size; val m = lst[0].size
        val newLst: Array<Array<T>> = Array(n){ Array(m){ lst[0].first() } }

        for(y in lst.indices) for(x in lst[y].indices){
            newLst[y][x] = lst[n-1-x][y]
        }

        return newLst.map(Array<T>::toList).toList()
    }
    // Generic 을 안쓰면 그나마 낫다.
    fun rotated90Int(lst: List<List<Int>>): List<List<Int>> {
        val n = lst.size; val m = lst[0].size
        val newLst: Array<Array<Int>> = Array(n){ Array(m){ 0 } }

        for(y in lst.indices) for(x in lst[y].indices){
            newLst[y][x] = lst[n-1-x][y]
        }

        return newLst.map(Array<Int>::toList).toList()
    }
}

fun <T> rotate90UsingForLoop(): RotatedFunc<T> {

    return ::rotated90
}

fun main(){
    test()
}
fun test(){
    val lst = listOf(
        listOf(1, 2, 3),
        listOf(4, 5, 6),
    )

    val actual = rotated90(lst)
    println(actual)
    check(actual == listOf(
        listOf(4, 1),
        listOf(5, 2),
        listOf(6, 3)
    ))
}