package main.kotlin;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

// package main.kotlin.pbus.jav
class Solution2 {
//    public static void main(String[] args) {
//
//        var actual = solution(1, 1, 5, new String[]{"08:00", "08:01", "08:02", "08:03"});
//        System.out.println(actual);
////        == "09:00"
//    }

    public static String solution(int n, int t, int m, String[] timetable) {
        List<Integer> busTimes = Stream.iterate(time2int("09:00"), it -> it + t).limit(n).toList();

        List<Integer> crews = Arrays.stream(timetable)
                .map(Solution2::time2int)
                .sorted()
                .collect(Collectors.toList());

        Collections.reverse(crews);

        busTimes.subList(0, busTimes.size()-1).forEach(busTime -> {
            // crews = crews.dropLast(crews.takeLast(m).count { it <= busTime })
            var subList = crews.subList(Math.max(crews.size() - m, 0), crews.size());
            int droppedNum = (int) subList.stream().filter(it -> it <= busTime).count();

            for(var i=0; i<droppedNum; i++) crews.remove(crews.size()-1);
        });

        var lastBusTime = busTimes.get(busTimes.size()-1);

        List<Integer> droppedCrews = crews.subList(Math.max(crews.size() - m, 0), crews.size()).stream().filter(it -> it <= lastBusTime).toList();

        Integer myTime;
        if(droppedCrews.size() == m){
            myTime = droppedCrews.get(0);
        }else {
            myTime = busTimes.get(busTimes.size()-1);
        }

        return timeInt2string(myTime);
    }

    public static String timeInt2string(int time){
        return String.format("%02d:%02d", time / 60, time % 60);
    }

    private static int time2int(String s) {
        String[] split = s.split(":");
        int h = Integer.parseInt(split[0]);
        int m = Integer.parseInt(split[1]);
        return h*60 + m;
    }
}

//class Solution {
//    fun solution(n: Int, t: Int, m: Int, timetable: Array<String>): String {
//        fun String.time2int() = this.split(":").map(String::toInt).let { it[0]*60 + it[1] }
//        fun Int.toTimeString(): String =
//                listOf(this / 60, this % 60)
//                        .map(Int::toString)
//                        .joinToString(":") { it.padStart(2, '0') }
//
//        val busTimes = generateSequence("09:00".time2int()) { it + t }.take(n).toList()
//        var crews: List<Int> = timetable.map(String::time2int).sorted().reversed()
//
//        for(busTime in busTimes.dropLast(1)){
//            crews = crews.dropLast(crews.takeLast(m).count { it <= busTime })
//        }
//        crews = crews.takeLast(m).filter { it <= busTimes.last() }
//
//        val myTime: Int = if(crews.size == m) crews.first() - 1 else busTimes.last()
//        return myTime.toTimeString()
//    }
//}
