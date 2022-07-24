package main.kotlin.utils

import kotlin.time.ExperimentalTime
import kotlin.time.measureTimedValue

data class Tc<T, E>(val input: T, val expected: E)

// lowerBound 구현
// @return: element 이상의 값이 처음 나오는 위치
fun <T : Comparable<T>> List<T>.lowerBound(element: T): Int {
    // require(this == this.sorted)
    var low = 0; var high = this.size

    while (low < high) {
        val m = (low + high).ushr(1) // (l+r)/2

        if(this[m] >= element) high = m
        else low = m + 1
    }

    return high
}

// upperBound 구현
// @return: element 초과의 값이 처음 나오는 위치
fun <T : Comparable<T>> List<T>.upperBound(element: T): Int {
    // @require(this == this.sorted)
    var low = 0; var high = this.size

    while (low < high) {
        val m = (low + high).ushr(1) // (l+r)/2

        if(this[m] <= element) low = m + 1
        else high = m
    }

    return high
}

@OptIn(ExperimentalTime::class)
fun testLowerBound(){
    val lst0 = listOf<Int>()
    val lst1 = listOf(1,2,4,5,8,9,10)
    val lst2 = listOf(1,2,2,5,5)

    val tcList = listOf(
        Tc(input = Pair(lst0, 1), expected = 0),
        Tc(input = Pair(lst1, 8), expected = 4),
        Tc(input = Pair(lst1, 3), expected = 2),
        Tc(input = Pair(lst1, -1), expected = 0),
        Tc(input = Pair(lst1, 10), expected = 6),
        Tc(input = Pair(lst1, 11), expected = lst1.size),
        Tc(input = Pair(lst2, 7), expected = lst2.size),
        Tc(input = Pair(lst2, 2), expected = 1),
        Tc(input = Pair(lst2, 5), expected = 3),
        Tc(input = Pair(lst2, 0), expected = 0),
    )

    tcList.forEach { tc ->
        val (lst, element) = tc.input

        val (actual1, duration1) = measureTimedValue { lst.lowerBound(element) }
//        val (actual2, duration2) = measureTimedValue { lst.lowerBound2(element) }

        println("${tc}; actual1=$actual1;")// actual2=$actual2;")
        println("duration1=$duration1;")   // duration2=$duration2")
        println()

        require(actual1 == tc.expected)
    }

    println("test1 success")
}

fun main(){
    testLowerBound()
}

//// Implemented using binary-search
//// @require(this == this.sorted)
//// @return: element 이상의 값이 처음 나오는 위치
//fun <T: Comparable<T>> List<T>.lowerBound2(element: T): Int {
//    // binarySearch 는 element 값을 발견하면 바로 리턴하므로
//    // this[idx] 는 lower bound 가 아닐 수 있다.
//    var idx = this.binarySearch(element, fromIndex = 0, toIndex = this.size)
//    if(idx < 0) return -idx-1
//
//    do {
//        idx = this.binarySearch(element, fromIndex = 0, toIndex = idx+1)
//                    .takeIf { it != idx } ?: break
//    }while (true)
//
//    return idx
//}