package main.kotlin
import kotlin.math.*;

fun main(){
  val n = readln().toInt()
  val pairs = List<Pair<Long, Long>>(n) {
    readln().split(" ").let {
      it[0].toLong() to it[1].toLong()
    }
  }

  println(solve(n, pairs))
}

fun solve(n: Int, pairs: List<Pair<Long, Long>>): Long {
  return pairs.sortedWith(compareBy({ it.first }, { it.second })).let { sorted ->
    val sums = Array(n) { 0L }
    sums[0] = sorted[0].second.toLong()

    for(i in 1 until n) {
      sums[i] = sums[i-1] + sorted[i].second.toLong()
    }
    
    search(arr=sums, pairs=sorted)
  }
}

fun search(arr: Array<Long>, pairs: List<Pair<Long, Long>>): Long {
  var low = 0
  val n = arr.size
  var high = n - 1
  var pos = 987654321L
  
  while(low <= high){
    val mid  = (low+high)/2
    val lsum = arr[mid]
    val rsum = arr[n-1] - arr[mid]
    
    if(lsum >= rsum){
      high = mid-1
      pos = min(pos, pairs[mid].first)
    }else{
      low = mid+1
    }
  }

  return pos
}
