package main.kotlin.p12915

fun main() = with(System.`in`.bufferedReader()){

  val (e, em, m, mh, h) = readLine()!!.split(" ").map(String::toInt)

  println(solve(e, em, m, mh, h))
}

fun solve(e: Int, em: Int, m: Int, mh: Int, h: Int): Int {
  // println("solve")
  fun isPossible(cnt: Int): Boolean {
    // easy: E+(EM)
    // medium: (EM)+M+(MH)
    // hard: (MH)+H
    var curEm = em; var curMh = mh;
    var easy = e
    
    if(easy < cnt){
      val diff = (cnt-easy).takeIf { it <= curEm } ?: return false
      curEm -= diff
    }
    
    var medium = m
    if(medium < cnt){
      var diff = (cnt-medium)

      if(diff <= curEm) { curEm -= diff; diff = 0 }
      else { diff -= curEm; curEm = 0; }
      
      if(diff > 0) {
        if(diff <= curMh) { curMh -= diff }
        else return false
      }
    }

    var hard = h
    if(hard < cnt){
      if(cnt - hard > curMh) return false
    }
    return true
  }

  return (0..300_000).upperBound(::isPossible) - 1
}

fun IntRange.upperBound(predicate: (Int) -> Boolean): Int {
  var low = start; var high = endInclusive+1
  
  while(low < high){
    val mid = (low+high).ushr(1)
    // println("$low $mid $high")
    if(predicate(mid)) low = mid+1
    else high = mid
  }

  return low
}



