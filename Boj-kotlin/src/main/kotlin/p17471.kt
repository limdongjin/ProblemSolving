package main.kotlin.p17471
import kotlin.math.abs

fun readInts() = readLine()!!.split(" ").map(String::toInt)

fun main() = with(System.`in`.bufferedReader()){
  val n = readInts().first()
  val populs = readInts()
  val adj: Array<Array<Boolean>> = Array(n){ Array(n){ false } }
  repeat(n){ area1 ->
    val inps = readInts()

    if(inps.size == 1) return@repeat

    inps.subList(1, inps.size).map(Int::dec).forEach { area2 ->
      adj[area1][area2] = true
      adj[area2][area1] = true 
    }
  }
  
  println(solve(n, populs, adj))
}


fun solve(n: Int, populs: List<Int>, adj: Array<Array<Boolean>>): Int {
  return allGroupingCases(n)
           .map { groups -> calcSumsOfTwoGroups(groups, populs, adj) }
           .filterNotNull()
           .minOfOrNull { diff(it) }
           ?: -1
}

fun allGroupingCases(n: Int): List<Pair<Set<Int>, Set<Int>>> {
  val lst = (0 until n).toList()
  val lstSet = lst.toSet()
  
  val ret = mutableListOf<Pair<Set<Int>, Set<Int>>>()

  for(i in 0 until n/2 + 1){
    if(i > n) break
    combinations(lst, r=i).forEach { case1 ->
      ret.add(case1.toSet() to lstSet.subtract(case1.toSet()))
    }
  }

  return ret
}

fun combinations(lst: List<Int>, r: Int): List<List<Int>> {
  val n = lst.size
  val selected = Array<Boolean>(n){ false }.apply{ fill(true, n-r, n) }
  // require(selected.count { it } == r)
 
  val ret = mutableListOf<List<Int>>()
  do {
    ret.add(lst.filterIndexed { idx, _ -> selected[idx] }.toList())
  }while(nextPermutation(selected))

  return ret
}

fun <T: Comparable<T>> nextPermutation(a: Array<T>): Boolean {
  fun Array<T>.swap(i: Int, j: Int) = this[i].also { this[i] = this[j] }.let { this[j] = it }

  val k = (0 until a.size-1).lastOrNull { a[it] < a[it+1] } ?: return false
  val i = (k+1 until a.size).last { a[k] < a[it] }
  a.swap(k, i)
  a.reverse(k+1, a.size)

  return true
}

fun diff(p: Pair<Int, Int>) = abs(p.first - p.second) // .also{ println("p=$p, diff=$it") }
fun calcSumsOfTwoGroups(groups: Pair<Set<Int>, Set<Int>>, populs: List<Int>, adj: Array<Array<Boolean>>): Pair<Int, Int>? {
  val n = adj.size
  fun bfs(group: Set<Int>, start: Int): Pair<Int, Int>{
    val q = ArrayDeque<Int>().apply { addLast(start) }
    val visited = mutableSetOf(start)
    var s = 0

    while(q.isNotEmpty()){
      val area1 = q.removeFirst()
      s += populs[area1]
      (0 until n).filter { adj[area1][it] }.forEach { area2 ->
        if(area2 in visited || area2 !in group) return@forEach
        q.addLast(area2)
        visited.add(area2) 
      }
    }

    return s to visited.size
  }
  
  val (group1: Set<Int>, group2: Set<Int>) = groups  
  if(group1.size == 0 || group2.size == 0) return null

  val (sum1, cnt1) = bfs(group1, group1.first())
  val (sum2, cnt2) = bfs(group2, group2.first())
  
  if(cnt1 + cnt2 != n) return null

  // println(sum1 to sum2)

  return sum1 to sum2
}


