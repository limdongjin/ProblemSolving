package main.kotlin.p2042
fun main() = with(System.`in`.bufferedReader()){
    val (n,m,k) = readLine().split(" ").map(String::toInt)
    val lst: List<Long> = List(n) { readLine().toLong() }
    val ops: List<List<Long>> = List(m+k){ readLine().split(" ").map(String::toLong) }

    println(solve(n,m,k,lst,ops).joinToString("\n"))
}

fun solve(n: Int,
          m: Int,
          k: Int,
          lst: List<Long>,
          ops: List<List<Long>>): List<Long> {
    val fenwick = FenwickTree.buildFrom(lst)
    val output = ArrayList<Long>()
    ops.forEach { (op, b, c) ->
        when(op){
            1L -> fenwick.update(b.toInt()-1, c)
            2L -> output.add(fenwick.rangeSum((b.toInt()-1) until c.toInt()))
            else -> require(false)
        }
    }

    return output
}

// segment tree
class FenwickTree(
    val n: Int,
    val tree: LongArray){

    fun rangeSum(range: IntRange): Long
        = prefixSum(range.last)-prefixSum(range.first -1)

    fun update(pos: Int, value: Long) {
        add(pos, value-rangeSum(pos..pos))
    }

    private fun prefixSum(toInclusive: Int): Long
        = generateSequence(toInclusive+1) { it - it.takeLowestOneBit() }
            .takeWhile { it > 0 } // pos++; while(pos > 0) { ret += tree[pos]; pos &= pos-1; }
            .sumOf { tree[it] }   // return ret;

    private fun add(pos: Int, value: Long) {
        generateSequence(pos+1) { it + it.takeLowestOneBit() }
            .takeWhile { it < tree.size }
            .forEach { tree[it] += value } //pos++;while(pos<tree.size){ tree[pos]+=val; pos+=(pos & -pos);}
    }

    companion object {
        fun buildFrom(lst: List<Long>): FenwickTree
            = FenwickTree(n=lst.size, tree=LongArray(lst.size+1))
                .apply { for((i,v) in lst.withIndex()) add(i, v); }
    }
}
