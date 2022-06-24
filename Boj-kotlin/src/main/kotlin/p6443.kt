package main.kotlin.p6443

fun main() = with(System.`in`.bufferedReader()){
    val n = readLine().toInt()
    val words = List(n){ readLine() }

    println(solve(n, words))
}

fun solve(n: Int, words: List<String>): String
    = words.asSequence().flatMap(::allAnagrams).joinToString("\n")

fun allAnagrams(word: String) = sequence {
    val arr = word.encoded().sorted().toIntArray()

    do {
        yield(arr.decoded())
    } while (nextPermutation(arr))
}
fun String.encoded(): List<Int> = this.map { it - 'a' }
fun IntArray.decoded(): String = this.map { 'a'.plus(it) }.joinToString("")

fun nextPermutation(arr: IntArray): Boolean {
    val k = (0 until  arr.size-1)
        .lastOrNull { arr[it] < arr[it+1] }
        ?: return false

    val i = (k+1 until arr.size).last { arr[k] < arr[it] }

    arr.swap(i, k)
    arr.reverse(fromIndex = k+1, toIndex = arr.size)

    return true
}
fun IntArray.swap(i: Int, j: Int) = this[i].also { this[i] = this[j] }.let { this[j] = it }