package main.kotlin.permutations

object HeapsAlgorithms {
    private fun <T> Array<T>.swap(i: Int, j: Int) =
        this[i].also { this[i] = this[j] }.also { this[j] = it }

    fun <T> permutations(a: Array<T>) = sequence {
        yield(a)

        val c = Array(a.size) { 0 }
        var i = 0

        while (i < a.size) {
            println(a.toList())
            if (c[i] >= i) {
                // Reset the state
                c[i] = 0

                // Popping the stack
                i += 1
                continue
            }

            // then, c[i] < i == true

            // swap
            a.swap(
                when(i%2){0 -> 0 else -> c[i]},
                i
            )

            // yield output
            yield(a)

            // increment of the for-loop counter
            c[i] += 1

            // simulate recursive call reaching the base case
            i = 0
        }
        return@sequence
    }
}