package main.kotlin.p2428

fun main(){
    val n= readln()!!.toInt()
    val nums = readln()!!.split(" ").map(String::toInt)

    println(solve(n, nums))
}

fun solve(n: Int, nums: List<Int>): Long {
    // 정렬
    return nums.sorted().let { sorted->
        (0 until n).sumOf { (calcCntOfPairs(sorted, it)-it).toLong() }
    }
}

// @return i=k 일때 검사해야 하는 쌍의 개수
fun calcCntOfPairs(nums: List<Int>, k: Int): Int {
    var low = k+1
    var high = nums.size-1
    var ans = k
    val predicate1 = { i: Int, j: Int -> nums[i]*10 < nums[j]*9 }

    // 바이너리 서치
    while(low <= high){
        val mid = (low+high)/2

        when(predicate1(k,mid)) {
            true -> high=mid-1          // 왼쪽으로
            else -> {ans=mid;low=mid+1} // 오른쪽
        }
    }

    return ans
}