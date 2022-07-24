package main.kotlin.utils.compare
import java.util.Comparator
import kotlin.math.abs

fun myStringComparator() = Comparator { s1: String, s2: String ->
    normalized(listOf(s1, s2))
        .let { (newA, newB) -> newA.compareTo(newB) }
}

data class Tc<T, E>(val input: T, val expected: E)

private fun normalized(a: String, toN: Int): String {
    val diff = (toN-a.length)
    return a+a.last().toString().repeat(abs((diff)+diff)/2)
}

private fun normalized(lst: List<String>): List<String> {
    val maxL = lst.maxOf { it.length }
    "aa".compareTo("bb")
    return lst.map { normalized(it, maxL) }
}


fun test1() {

    // normal compare
    require(listOf("DB", "DBA").sorted() == listOf("DB", "DBA"))

    // special compare
    require(listOf("DB", "DBA").sortedWith(comparator = myStringComparator()) == listOf("DBA", "DB"))

    val tcList = listOf(
        Tc(input=listOf("CD", "BD", "BC", "AB"), expected=listOf("AB", "BC", "BD", "CD")),
        Tc(input=listOf("DB", "DBA"), expected=listOf("DBA", "DB")),
        Tc(input=listOf("DB", "DBA", "ABC", "ABD", "A", "DBC", "ADB", "AD"),
            expected=listOf("A", "ABC", "ABD", "ADB","AD", "DBA", "DB", "DBC")),
    )

    // Note that. listOf("DB", "DBA").sorted() == listOf("DB", "DBA")
    tcList.forEach { tc ->
        val actual = tc.input.sortedWith(comparator = myStringComparator())
        println("${tc}; actual=$actual;")

        require(actual == tc.expected)
    }

    println("test1() success!")
}

fun test2(){
    val tcList: List<Tc<List<String>, Map<String, List<String>>>> = listOf(
        Tc(
            input=listOf("CD", "BD", "BC", "AB"),
            expected=mapOf(
                "A" to listOf("AB"),
                "B" to listOf("BC", "BD"),
                "C" to listOf("CD"),
                "D" to listOf()
            )
        ),
        Tc(
            input=listOf("DB", "DBA"),
            expected= mapOf(
                "A" to listOf(),
                "B" to listOf(),
                "C" to listOf(),
                "D" to listOf("DBA", "DB")
            )
        ),
        Tc(
            input=listOf("DB", "DBA", "ABC", "ABD", "A", "DBC", "ADB", "AD"),
            expected= mapOf(
                "A" to listOf("A", "ABC", "ABD", "ADB","AD"),
                "B" to listOf(),
                "C" to listOf(),
                "D" to listOf("DBA", "DB", "DBC"),
            )
        ),
    );

    val getSetOfAllChars: (List<String>) -> Set<Char> = { ('A'..(it.flatMap(String::toList).maxOrNull()!!)).toSet() }
    val getSetOfKeyChars: (List<String>) -> Set<Char> = { it.map(String::first).toSet() }

    val getSetOfNotKeyChars: (List<String>) -> Set<Char> = { getSetOfAllChars(it) subtract getSetOfKeyChars(it) }
    val transformSortMapValue: (Map.Entry<Any, List<String>>) -> List<String> = {
        it.value.sortedWith(comparator = myStringComparator())
    }
    val transformToStrKey: (Map.Entry<Any, List<String>>) -> String = { it.key.toString() }

    val getGroupedMap: (List<String>) -> Map<String, List<String>> = { lst ->
        lst.groupBy(keySelector = { it.first() })
            .plus(getSetOfNotKeyChars(lst).associateWith { listOf() })
            .mapValues(transformSortMapValue)
            .mapKeys(transformToStrKey)
            .toSortedMap().toMap()
    }

    run { // test
        val lst1 = listOf("ABC", "AA", "AAC", "DE", "B")

        require(getSetOfAllChars(lst1) == setOf("A", "B", "C", "D", "E").map(String::first).toSet())
        require(getSetOfKeyChars(lst1) == setOf("A", "B", "D").map(String::first).toSet())
        require(getSetOfNotKeyChars(lst1) == setOf("C", "E").map(String::first).toSet())
    }

    tcList.forEach { tc ->
        val actual = getGroupedMap(tc.input)

        println("${tc}; actual=$actual;")

        require(actual.entries.all { it.value == tc.expected.getValue(it.key) })
        require(actual.keys == tc.expected.keys)
        require(actual == tc.expected)
    }

    println("test2() success!")
}

fun main(){
    test1()
    test2()
}


//fun String.specialComparator(a: String, b: String) {
//
//    normalized(listOf(a, b)).let {  }
//    Comparator { s1: String, s2: String ->
//        normalized(listOf(s1, s2))
//            .let { (newA, newB) -> newA.compareTo(newB) }
//    }
//
//    (a to b)
//        .let {
//            val diff = (b.length-a.length)
//            val newA = (a+a.last().toString().repeat((abs(diff)+diff)/2))
//            val newB = (b+b.last().toString().repeat((abs(-diff)-diff)/2))
//
//            newA to newB
//        }
//        .also { println(it) }
////        .let { it.first.zip(it.second) }
//        .let {
//
//            compareBy<String> { it }.thenComparator({ a, b -> compareValues(a, b) })
//            it.first.compareTo(it.second)
//        }
//
//    listOf("DB","DBA", "DBC")
//        .sortedWith(comparator = Comparator.comparing({}))
//        .sortedBy { it }
//        .sortedWith(compareBy { it })
//}