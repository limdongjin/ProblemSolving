//package main.kotlin.p2482
//
//import kotlin.reflect.KProperty
//
//// 2482 색상환
//
//fun main(){
//    val n = readln().toInt()
//    val k = readln().toInt()
//
//    print(solve(n, k))
//}
//
//fun solve(n: Int, k: Int): Int {
//    return (go_with_memoize(n-3, k-1) % 1_000_000_003).toInt()
////    if(k == 1) return n
////
////    val dp = Array(n+1) { Array(n+1){ -1L } }
////        .apply {
////            for(y in 1..n) {
////                this[y][0] = 0           // 0 개의 색을 선택 -> 경우의 수 = 0
////                this[y][1] = y.toLong() //  크기가 y인 배열에서 1 개의 색을 선택 -> 경우의 수 = y
////            }
////        }
////
////    // dp[n][k] = go(0번 색 선택) + go(0번 색 선택x)
////    dp[n][k] = go(n-3, k-1, dp) + go(n-1, k, dp)
////
////    return (dp[n][k] % 1_000_000_003).toInt()
//}
//
//class Memoize2<T, T2, R>(val f: (T, T2) -> R) {
//    private val values = mutableMapOf<Pair<T, T2>, R>()
////    operator fun getValue(thisRef: Nothing?, props: KProperty<*>) = { p: Pair<T, T2> ->
////        values.getOrPut(p) { f(p.first, p.second) }
////    }
//
//    operator fun getValue(r: R, property: KProperty<*>, prop2: KProperty<*>): (T2, T2) -> R {
//        TODO()
//    }
//}
//
////fun <T, T2, R> ((T, T2)-> R).memoize(): (T, T2) -> R = Memoize2(this)
//
////val go_with_memoize = { n: Int, k: Int ->
////    _go(n, k)
////}.memoize()
//typealias GoFunc = (Int, Int) -> Long
//
//val go_with_memoize: (Int, Int) -> Long by Memoize2 { n: Int, k: Int ->
//    TODO()
////    when {
////        n < 0 || k < 0 -> return 0
////        n/2 + 1 < k -> return 0 // ex, 크기가 20인 배열에서 11개의 요소를 선택할 수 없다.
////        k == 1 -> return n.toLong()
////        k == 0 -> return 0
////    }
////
////    // dp[n][k] = go(첫번째 색 선택) + go(선택x)
////    return (_go(n-2, k-1) + _go(n-1, k)) % 1_000_000_003
//}
//
////
////fun go(n: Int, k: Int, dp: Array<Array<Long>>): Long {
////    when {
////        n < 0 || k < 0 -> return 0
////        dp[n][k] != -1L -> return dp[n][k]
////        n/2 + 1 < k -> return 0 // ex, 크기가 20인 배열에서 11개의 요소를 선택할 수 없다.
////    }
////
////    // dp[n][k] = go(첫번째 색 선택) + go(선택x)
////    dp[n][k] = (go(n-2, k-1, dp) + go(n-1, k, dp)) % 1_000_000_003
////
////    return dp[n][k]
////}