package main.kotlin.utils.permutations

import kotlin.time.ExperimentalTime
import kotlin.time.measureTimedValue
import kotlin.math.pow
import main.kotlin.utils.factorial.factorial

// 순열 nPr = (n!)/(n-r)! = (n)*({n-1}P{r-1})
// 순열: n 개 중 r 개를 중복 없이 고르고 나열
tailrec fun nPr(n: Int, r: Int, acc: Long = 1L): Long = if(r == 0) acc else nPr(n-1, r-1, n*acc)

// 중복 순열 {n}\Pi{r} = n^r
// 중복 순열: n 개 중 r 개를 중복을 허용하여 고르고 나열
fun nPIr(n: Int, r: Int): Long = n.toDouble().pow(r).toLong()

// nextPermutation 구현
fun <T: Comparable<T>> nextPermutation(arr: Array<T>): Boolean {
    fun <T> Array<T>.swap(i: Int, j: Int) = this[i].also { this[i] = this[j] }.let { this[j] = it }

    // Find the largest index k such that a[k] < a[k+1].
    val k = (arr.lastIndex-1 downTo 0)
        .firstOrNull { arr[it] < arr[it+1] } // lastOrNull 는 반복문 끝까지 돌기때문에 비효율적이다.
        ?: return false

    // Find the largest index i such that a[k] < a[i]
    val i = (arr.lastIndex downTo k+1).first { arr[k] < arr[it] }

    arr.swap(i, k)
    arr.reverse(k+1, arr.size)

    return true
}

// 순열 구현 using sequence + recursive
fun IntArray.permutations(r: Int = size): Sequence<IntArray> =
    permutations(r = r, depth = 0, output = IntArray(r), visited = BooleanArray(size))

// 중복 순열 구현 using sequence + recursive
fun IntArray.permutationsWithRepetition(r: Int = size): Sequence<IntArray> =
    permutations(r = r, depth = 0, output = IntArray(r), visited = BooleanArray(size), repetition = true)

private fun IntArray.permutations(r: Int,
                                  depth: Int,
                                  output: IntArray,
                                  visited: BooleanArray,
                                  repetition: Boolean = false
): Sequence<IntArray> = sequence {
    check(depth <= r) { "depth 는 r 보다 작거나 같아야한다." }
    if(depth == r) {
        check(repetition || output.toSet().size == r) { "순열의 경우, 중복하여 선택할 수 없다." }

        yield(output)
        return@sequence
    }

    val thisL = this@permutations
    for(idx in thisL.indices) if(!visited[idx] || repetition) { // 중복 순열은 방문 여부 무시 가능
        output[depth] = thisL[idx]

        visited[idx] = true
        yieldAll(thisL.permutations(
            r           = r,
            depth       = depth+1,
            output      = output,
            visited     = visited,
            repetition  = repetition
        ))
        visited[idx] = false
    }
}

// 순열 구현 using pattern-matching
fun <T: Comparable<T>> permutationsUsingPatternMatching(el: List<T>): List<List<T>> = permutationsUsingPatternMatching(el, sub = el, fin = listOf())
private fun <T: Comparable<T>> permutationsUsingPatternMatching(el: List<T>,
                                                                sub: List<T>, // 아직 고르지않은 요소들
                                                                fin: List<T> // 고른 요소들
): List<List<T>> =
    when(sub.size){
        0 -> listOf(fin)
        else -> sub.flatMap { x -> permutationsUsingPatternMatching(el, sub - x, fin + x) }
    }

fun permutationsUsingNextPerm(lst: List<Int>): List<List<Int>>{
    val ret = mutableListOf<List<Int>>()
    val arr = lst.toTypedArray()

    do {
        ret.add(arr.toList())
    } while (nextPermutation(arr))

    return ret
}

////////////// test //////////////////////
fun main(){
    testFactorial(::factorial)
    testNPR(::nPr)
    testNPIR(::nPIr)

    testPermutation(IntArray::permutations)

    testPermutation2(::permutationsUsingPatternMatching)
    testPermutation2(::permutationsUsingNextPerm)

    testPermutationWithRepetition(IntArray::permutationsWithRepetition)
}

@OptIn(ExperimentalTime::class)
fun testPermutation(permutationFunc: IntArray.(Int) -> Sequence<IntArray>){
    val arr = intArrayOf(1,21,3,4,5,61)
    val n = arr.size // 6
    val r = 3

    measureTimedValue {
        arr.sortedArray().permutationFunc(r)
            .map(IntArray::toList)
            .toList()
    }
    .let { (actual, duration) ->
        println("duration=$duration")

        check(actual.size.toLong() == nPr(n, r))
        check(actual.distinct() == actual)
        check(actual.all { it: List<Int> -> it.toSet().size == r })
    }

    println("$permutationFunc test success")
}

@OptIn(ExperimentalTime::class)
fun testPermutation2(permutationFunc: (List<Int>) -> List<List<Int>>){
    val arr = listOf(1,21,3,4,5,61)
    val n = arr.size // 6

    measureTimedValue {
        permutationFunc(arr.sorted())
    }
    .let { (actual, duration) ->
        println("duration=$duration")
        check(actual.size.toLong() == factorial(n))
        check(actual.distinct() == actual)
        check(actual.all { it: List<Int> -> it.toSet().size == n })
    }

    println("$permutationFunc test success")
}

fun testPermutationWithRepetition(permutationsRepFunc: IntArray.(Int) -> Sequence<IntArray>){
    val arr = intArrayOf(1,21,3,4,5,61)
    val n = arr.size // 6
    val r = 3
    val actual = arr.permutationsRepFunc(r).map { it.toList() }.toList()

    check(actual.size.toLong() == nPIr(n, r))
    check(actual.distinct() == actual)
    check(actual.all { it.size == r })

    println("$permutationsRepFunc test success")
}

fun testNPIR(nPIrFunc: (Int, Int) -> Long){
    check(nPIrFunc(1, 1) == 1L)
    check(nPIrFunc(213, 0) == 1L)
    check(nPIrFunc(5, 4) == 625L)
    check(nPIrFunc(5, 2) == 25L)

    println("$nPIrFunc test success")
}

fun testFactorial(factorialFunc: (Int) -> Long){
    check(factorialFunc(5) == 120L)
    check(factorialFunc(1) == 1L)
    check(factorialFunc(0) == 1L)

    println("$factorialFunc test success")
}

fun testNPR(nPrFunc: (Int, Int) -> Long){
    check(nPrFunc(1, 1) == 1L)
    check(nPrFunc(23, 0) == 1L)
    check(nPrFunc(5, 4) == 120L)
    check(nPrFunc(5, 4) == 5*nPrFunc(4, 3))

    println("$nPrFunc test success")
}
