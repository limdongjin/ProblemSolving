package permutations

fun allPermutations(a: Array<Int>) = sequence {
    a.sort()

    do yield(a)
    while(nextPermutation(a))
}

fun nextPermutation(a: Array<Int>,
                    fromInclusive: Int = 0,
                    endExclusive: Int = a.size): Boolean {

    // 1. Find the largest index k, such that a[k] < a[k+1].
    //   if no such index exists, the permutations is last perm.
    val k = (fromInclusive until endExclusive-1)
        .lastOrNull { a[it] < a[it+1] }
        .takeIf { it != null } ?: return false

    // 2. Find the largest index i(>=k), such that a[k] < a[i]
    val i = (k+1 until endExclusive)
        .last { a[k] < a[it] }

    // 3. swap
    a.swap(k, i)

    // 4. reverse
    a.reverse(k+1, endExclusive)

    return true
}

private fun Array<Int>.swap(i: Int, j: Int) =
    get(i).also { set(i, value = get(j)) }
        .also { set(j, value = it) }