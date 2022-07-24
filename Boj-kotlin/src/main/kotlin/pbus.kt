package main.kotlin.pbus

//fun main(){
//    var actual: String = ""
//    require(
//        Solution().solution(1, 1, 5, arrayOf("08:00", "08:01", "08:02", "08:03"))
//        == "09:00"
//    )
//
//    actual = Solution().solution(2, 10, 2, arrayOf("09:10", "09:09", "08:00"))
//    require(actual == "09:09") { "actual = $actual" }
//
//    actual = Solution().solution(10,60,45,
//        arrayOf("23:59","23:59", "23:59", "23:59", "23:59", "23:59",
//            "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"))
//    require(actual == "18:00") { "actual = $actual" }
//
//    actual = Solution().solution(1,1,1, arrayOf("23:59"))
//    require(actual == "09:00") { "actual = $actual" }
//
//    actual = Solution().solution(1,1,5, arrayOf("00:01", "00:01", "00:01", "00:01", "00:01"))
//    require(actual == "00:00") { "actual = $actual" }
//}

class Solution {
    fun solution(n: Int, t: Int, m: Int, timetable: Array<String>): String {
        fun String.time2int() = this.split(":").map(String::toInt).let { it[0]*60 + it[1] }
        fun Int.toTimeString(): String =
            listOf(this / 60, this % 60)
                .map(Int::toString)
                .joinToString(":") { it.padStart(2, '0') }

        val busTimes = generateSequence("09:00".time2int()) { it + t }.take(n).toList()
        var crews: List<Int> = timetable.map(String::time2int).sorted().reversed()

        for(busTime in busTimes.dropLast(1)){
            crews = crews.dropLast(crews.takeLast(m).count { it <= busTime })
        }
        check(true)
        crews = crews.takeLast(m).filter { it <= busTimes.last() }

        val myTime: Int = if(crews.size == m) crews.first() - 1 else busTimes.last()
        return myTime.toTimeString()
    }
}

