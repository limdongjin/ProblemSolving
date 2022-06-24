package main.kotlin.p9997

fun main() = with(System.`in`.bufferedReader()){
//    test()
    val n = readLine().toInt()
    val words = List(n){ readLine()!! }

    println(solve(n, words))
}

fun solve(n: Int, words: List<String>): Int = go(encodedWords=words.map(String::encoded), idx=0, acc=0)
fun go(encodedWords: List<Int>, idx: Int, acc: Int): Int = when (idx) {
    encodedWords.size -> when(isCompleteSentence(acc)){
        true -> 1
        false -> 0
    }
    else -> go(encodedWords, idx + 1, acc.or(encodedWords[idx])) + go(encodedWords, idx + 1, acc)
}

fun isCompleteSentence(s: Int) = (s == (1).shl(26).minus(1))
fun String.encoded() = this.fold(initial = 0) { acc, c -> acc.or((1).shl(c - 'a')) }

fun test(){
    require("a".encoded() == 1)
    require("b".encoded() == 2)
    require("c".encoded() == 4)
    require("abc".encoded() == 7)
    require("the".encoded() == (Math.pow(2.0, ('t'-'a').toDouble())
                    +Math.pow(2.0, ('h'-'a').toDouble())
                    +Math.pow(2.0, ('e'-'a').toDouble())).toInt())
    require(solve(9, listOf(
        "the", "quick", "brown", "fox", "jumps", "over", "a", "sleazy", "dog"
    )) == 2)
    require(solve(3, listOf("a", "b", "c")) == 0)
    require(solve(15, listOf(
        "abcdefghijkl",
        "bcdefghijklm",
        "cdefghijklmn",
        "defghijklmno",
        "efghijklmnop",
        "fghijklmnopq",
        "ghijklmnopqr",
        "hijklmnopqrs",
        "ijklmnopqrst",
        "jklmnopqrstu",
        "klmnopqrstuv",
        "lmnopqrstuvw",
        "mnopqrstuvwx",
        "nopqrstuvwxy",
        "opqrstuvwxyz"
    )) == 8189)
}

