package main.kotlin.utils.combinations

import main.kotlin.utils.factorial.factorial
import main.kotlin.utils.permutations.nPr
import main.kotlin.utils.permutations.nextPermutation

import kotlin.time.ExperimentalTime
import kotlin.time.measureTimedValue

// Combinations(조합) nCr = (nPr)/(r!)
fun nCr(n: Int, r: Int): Long = nPr(n, r) / factorial(r)

// CombinationsWithRepetition(중복 조합) nHr = {n+r-1}C{r}
fun nHr(n: Int, r: Int): Long = nCr(n = n+r-1, r = r)

// 조합 구현
fun IntArray.combinations(r: Int): Sequence<IntArray> =
    combinations(r, output = IntArray(r), start = 0, depth = 0)

// 중복 조합 구현
fun IntArray.combinationsWithRepetition(r: Int): Sequence<IntArray> = combinations(r, output = IntArray(r), start = 0, depth = 0, repetition = true)

// depth-1 개의 수를 이미 선택한 output 배열이 주어졌을때, (output[0]..output[depth-1] 은 이미 채워졌다는 것)
// @return [Sequence] of depth 번째 수 ~ r 번째 수를 선택하는 조합
private fun IntArray.combinations(r: Int,
                          output: IntArray,
                          start: Int,   // thisL 에서 고르기 시작할 인덱스 :: each element E of thisL for range(start until n):
                          depth: Int,    // output[depth] = E // depth 번째 뽑은 수는 E 이다.
                          repetition: Boolean = false
): Sequence<IntArray> = sequence {
    // 함수 리턴 타입을 명시적으로 지정해줘야 yieldAll(recursiveCall) 할 수 있음.
    // Type checking has run into a recursive problem. Easiest workaround: specify types of your declarations explicitly

    // require(output[0]~output[depth-1] 는 이미 채워져 있다.)
    require(depth <= r)
    if(depth == r) yield(output).also { return@sequence } // terminal.

    val thisL = this@combinations; val n = thisL.size

    for (idx in start until n) {
        output[depth] = thisL[idx] // depth 번째 선택을 결정한다. :: output[depth] = thisL[selectedIdx]
        yieldAll(combinations(     // sequence for [depth+1(~r) 번째 선택]
            r           = r,
            output      = output,
            start       = if(repetition) idx else idx + 1,
            depth       = depth + 1,
            repetition  = repetition
        ))
    }
}

// 다소 느림
fun IntArray.combinationsUsingNextPerm(r: Int): Sequence<IntArray> {
    fun IntArray.fillFromElementsBy(elements: IntArray, selected: Array<Boolean>) {
        var cur = 0
        for(i in selected.indices) if(selected[i]) this[cur++] = elements[i]
    }

    val n = size
    val output = IntArray(r)
    val lstReversed = reversedArray()

    val selected = Array<Boolean>(n){false}.apply {
        fill(element = true, fromIndex = n-r, toIndex = n) // true 를 r 개 놓는다.
    }

    require(output.size == r)
    return sequence {
        do {
            output.fillFromElementsBy(elements = lstReversed, selected)
            yield(output)
        } while(nextPermutation(selected))
    }
}

////////////////////////////////////
fun testCombination(lst: List<Int>, r: Int, actual: List<List<Int>>) {
    val n = lst.size

    // nCr = (nPr / (r!))
    val expectedSize: Long = nPr(n, r) / factorial(r)

    check(actual.all { it.size == r }) { "check all selected `r` elements" }
    check(actual.size.toLong() == expectedSize) { "check nCr" }

//    check(actual.toSet().size == actual.size) { "check distinct" } // 메모리 소모 큰 테스트
    check(actual.all { it.toSet().size == r }){ "check distinct2" }
    check(actual.all { lst.containsAll(it) }) { "check containsAll" }
}

fun testCombination(lst: IntArray, r: Int, actual: ArrayList<IntArray>) {
    val n = lst.size

    // nCr = (nPr / (r!))
    val expectedSize: Long = nPr(n, r) / factorial(r)

    check(actual.all { it.size == r }) { "check all selected `r` elements" }
    check(actual.size.toLong() == expectedSize) { "check nCr" }

    check(actual.toList().toSet().size == actual.toList().size) { "check distinct" } // 메모리 소모 큰 테스트
    check(actual.all { it.toList().toSet().size == r }){ "check distinct2" }
    check(actual.all { lst.toList().containsAll(it.toList()) }) { "check containsAll" }

    println("testCombination success")
}

@OptIn(ExperimentalTime::class)
fun main(){
//    run {
//        val arr = intArrayOf(1,2,3,4,5,6)
//        val r = 3
//        arr.combinationsRecursive(r=3)
//            .also { actual -> testCombination(arr, r, actual) }
//            .map(IntArray::toList)
//            .also(::println)
//    }
//    TODO()

    val lst = (1..500).toList()
    val arr = lst.toIntArray()
    val r = 3

    println("==using recursiveSeq==")
    measureTimedValue {
        arr.combinations(r)
            .map { it.toList() }
            .toList()
    }.let { (actual, duration) ->
        testCombination(lst = lst, r, actual).also { println("test success") }
        println("duration=$duration")
    }
    println()

//    println("==using nextPerm==")
//    measureTimedValue {
//        arr.combinationsUsingNextPerm(r)
//            .map { it.toList() }
//            .toList()
//    }.let { (actual, duration) ->
//        testCombination(lst = lst, r, actual).also { println("test success") }
//        println("duration=$duration")
//    }
//    println()

    println("==combinationWithRep==")
    val arr2 = intArrayOf(11, 21, 31, 41, 5)
    val nn = arr2.size
    val rr = 3
    arr2.combinationsWithRepetition(rr)
        .onEach { println(it.toList()) }
        .count().let { cnt -> check(cnt.toLong() == nHr(nn, rr)); println(cnt) }
}

//
//fun IntArray.tail() = sliceArray(1..lastIndex)
//fun List<Int>.tail() = subList(1, size)
//// 빠름
//fun IntArray.combinations(r: Int): Sequence<IntArray> = sequence {
//    val n = size.takeIf { it >= r } ?: return@sequence
//    val combIndices = (0 until r).toList().toIntArray()
//    val output = IntArray(r)
//    val updateOutput: () -> Unit = {
//        (0 until r).forEach { output[it] = this@combinations[combIndices[it]] }
//    }
//
//    do {
//        updateOutput()
//        yield(output)
//        // yield(combIndices.map { this@combinations[it] })
//
//        val i = (r-1 downTo 0)
//            .firstOrNull { combIndices[it] != it+n-r }
//            ?: break
//        combIndices[i] += 1
//        (i+1 until r).forEach { combIndices[it] = combIndices[it-1] + 1 }
//    }while (true)
//}

//// 느림
//fun <T> List<T>.tail() = drop(1) // .subList(1, size)
//fun combinations(arr: List<Int>, r: Int): List<List<Int>> =
//    when {
//        (r < 1 || arr.isEmpty()) -> listOf(emptyList())
//        (r == arr.size) -> listOf(arr)
//        // lst[1:] 에서 r 개 선택 OR lst[1:]에서 r-1개 선택
//        else -> arr.tail().let { tail ->
//            combinations(tail, r) +
//                    combinations(tail, r-1).map { comb: List<Int> -> comb.plus(arr.first()) }
//        }
//    }
//fun IntArray.combinationsRecursive(r: Int): ArrayList<IntArray> {
//    val ans = ArrayList<IntArray>()
//    this.combinationsRecursive(
//        r=r,
//        ans = ans,
//        curComb = IntArray(r),
//        start = 0,
//        curDepth = 0
//    )
//    return ans
//}
//private fun IntArray.combinationsRecursive(r: Int,
//                                   ans: ArrayList<IntArray>,
//                                   curComb: IntArray,
//                                   start: Int,
//                                   curDepth: Int) {
//    if(curDepth == r){
//        ans.add(curComb.copyOf())
//        return
//    }
//
//    for(idx in start..lastIndex){
//        curComb[curDepth] = this[idx]
//        this.combinationsRecursive(
//            r=r,
//            ans=ans,
//            curComb=curComb,
//            start=idx+1,
//            curDepth=curDepth+1
//        )
//    }
//}
//fun combinationsUsingRecursive(lst: List<Int>,
//                          r: Int,
//                          ans: ArrayList<Array<Int>>,
//                          curComb: Array<Int> = lst.slice(0 until r).toTypedArray(),
//                          curIdx: Int = 0,
//                          curDepth: Int = 0) {
//    if(curDepth == r){
//        ans.add(curComb.copyOf())
//        return
//    }
//
//    for(i in curIdx until lst.size){
//        curComb[curDepth] = lst[i]
//        combinationsUsingRecursive(
//            lst = lst,
//            r = r,
//            ans = ans,
//            curComb = curComb,
//            curIdx = i + 1,
//            curDepth = curDepth + 1
//        )
//    }
//}

//fun <T> List<T>.tail() = drop(1) // subList(1, size)
//fun <T: Comparable<T>> combinations(lst: List<T>, r: Int): List<List<T>> =
//    when {
//        (r < 1 || lst.isEmpty()) -> listOf(listOf())
//        (r == lst.size) -> listOf(lst)
//        // lst[1:] 에서 r 개 선택 OR lst[1:]에서 r-1개 선택
//        else -> lst.tail().let { tail ->
//            combinations(tail, r) + combinations(tail, r-1).map { comb: List<T> -> comb.plusElement(lst.first()) }
//        }
////        else -> combinations(lst.tail(), r) + combinations(lst.tail(), r-1).map { comb: List<T> -> comb.plusElement(lst.first()) }
//    }
