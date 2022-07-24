package main.kotlin.p1036
import java.math.BigInteger
import kotlin.math.pow


fun main() = with(System.`in`.bufferedReader()){
  // test()
  val n = readLine()!!.toInt()
  val arr = Array(n) { readLine()!! }
  val k = readLine()!!.toInt()

  println(solve(n, arr, k))
}

fun solve(n: Int, arr: Array<String>, k: Int): String {
  val big36 = BigInteger("36")
  val dig: MutableMap<Char, BigInteger> = (('0'..'9').toList() + ('A'..'Z').toList()).associate { it to BigInteger.ZERO }.toMutableMap()
  
  arr.forEach { word ->
    word.reversed().forEachIndexed { i: Int, ch: Char ->
      dig[ch] = dig[ch]!! + big36.pow(i)
    }
  }
  
  // dig[ch] : ch 를 'Z' 로 바꿨을때의 차 
  var i = 0
  dig.keys.forEach { ch ->
    dig[ch] = dig[ch]!! * BigInteger((35 - i).toString())
    i++
  }
  
  // dig[ch] 값이 큰 순서로 정렬 -> 상위 K개의 문자를 'Z' 로 바꾼다
  dig.map { (k, v) -> k to v }.sortedByDescending { it.second }.subList(0, k).forEach { (ch, v) ->
    for(i in 0 until n) arr[i] = arr[i].replace(ch, 'Z')
  }
  
  // 1. 36진수 word -> 10진수num
  // 2. sum
  // 3. 36진수 문자열로 변환
  return arr.sumOf { word -> BigInteger(word, 36) }.toString36()
}

// 10진수 -> 36진수
fun BigInteger.toString36(): String {
  val big36 = BigInteger("36")
  val d = ('0'..'9').toList() + ('A'..'Z').toList()

  val a: BigInteger = this / big36
  val b = (this % big36).toInt()
  val w = d[b].toString()

  return if(a != BigInteger.ZERO) a.toString36() + w else w
}

fun test(){
  require(solve(n=1, arr=arrayOf("HELLO"), k=2) == "ZZLLO")
  require(solve(n=5, arr=arrayOf("GOOD", "LUCK", "AND", "HAVE", "FUN"), k=7) == "31YUB")
  require(solve(n=5, arr=arrayOf("500", "POINTS", "FOR", "THIS", "PROBLEM"), k=5) == "1100TC85")
}
