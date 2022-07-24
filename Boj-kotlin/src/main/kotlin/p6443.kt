package main.kotlin.p6443

fun main() = with(System.`in`.bufferedReader()){
    val n = readLine().toInt()
    val words = List(n){ readLine() }

    println(solve(n, words))
}

fun solve(n: Int, words: List<String>): String
    = words.asSequence().flatMap(::allAnagrams).joinToString("\n")

fun allAnagrams(word: String) = sequence {
    val arr = word.toCharArray().sorted().toTypedArray()

    do {
        yield(arr.joinToString(""))
    } while(nextPermutation(arr))
}
fun <T: Comparable<T>> nextPermutation(arr: Array<T>): Boolean {
    // Find the largest index k such that a[k] < a[k+1].
    val k = (0 until  arr.size-1)
        .lastOrNull { arr[it] < arr[it+1] }
        ?: return false

    // Find the largest index i such that a[k] < a[i]
    val i = (k+1 until arr.size).last { arr[k] < arr[it] }

    arr.swap(i, k)

    arr.reverse(k+1, arr.size)

    return true
}
fun <T> Array<T>.swap(i: Int, j: Int) = this[i].also { this[i] = this[j] }.let { this[j] = it }