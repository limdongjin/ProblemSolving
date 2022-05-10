package main.kotlin.p16719

fun main() {
    val srcStr = readln()

    solve(srcStr)
}

fun solve(src: String) {
    val displayed = Array(src.length) { false }
    go(src, displayed)
}

fun go(src: String, displayed: Array<Boolean>, start: Int = 0, endInclusive: Int = src.length - 1) {
    if(start > endInclusive) return

    val midIdx = start + src.slice(start..endInclusive)
                                .let { sliced ->
                                    sliced.indexOf(sliced.minOrNull()!!)
                                }

    // add src[midIdx] to result string
    displayed[midIdx] = true

    // print result string
    println(src.filterIndexed { idx, _ -> displayed[idx] })

    // call right
    go(src, displayed, midIdx + 1, endInclusive)

    // call left
    go(src, displayed, start, midIdx - 1)
}