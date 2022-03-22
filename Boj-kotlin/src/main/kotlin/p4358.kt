package main.kotlin

import java.io.BufferedReader

import java.io.InputStreamReader

// 생태학

private fun main() = with(BufferedReader(InputStreamReader(System.`in`))){

    val treeDict = mutableMapOf<String, Int>()

    do {
        val tree = readLine() ?: break
        treeDict[tree] = treeDict.getOrDefault(tree, 0) + 1
    }while (true)

    with(treeDict){
        val total = values.sum()
        toSortedMap()
            .forEach { (key, value) ->
                val v = "%.4f".format(value.div(total.toFloat()).times(100))
                println("$key $v")
            }

    }
}