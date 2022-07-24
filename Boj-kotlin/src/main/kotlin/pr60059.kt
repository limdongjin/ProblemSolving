package main.kotlin

// https://school.programmers.co.kr/learn/courses/30/lessons/60059

class Solution {

    fun solution(key: Array<IntArray>, lock: Array<IntArray>): Boolean {
        // testKey(key)

        val m = key.size; val n = lock.size

        // coordinates of "1"
        val keyOneSets: List<Set<Pair<Int, Int>>> =
            findRotatedKeys(key)
                .map { rKey ->
                    ((0 until m) product (0 until m))
                        .filter { rKey[it.first][it.second] == 1 }
                        .toSet()
                }

        // coordinates of "0"
        val lockZeroSet: Set<Pair<Int, Int>> =
            ((0 until n) product (0 until n))
                .filter { lock[it.first][it.second] == 0 }
                .toSet()
        val isOpenedAt = isOpenedAt(lockZeroSet, n)

        return ((-m..m+n) product (-m..m+n))
            .any { pos ->
                keyOneSets.any { rKey -> isOpenedAt(pos, rKey) }
            }
    }

    fun isOpenedAt(lockZeroSet: Set<Pair<Int, Int>>, n: Int): (Pair<Int, Int>, Set<Pair<Int, Int>>) -> Boolean {
        return { pos: Pair<Int, Int>, key: Set<Pair<Int, Int>> ->
            isOpenedAt(lockZeroSet, n, pos=pos, key=key)
        }
    }

    fun isOpenedAt(lockZeroSet: Set<Pair<Int, Int>>, n: Int,
                   pos: Pair<Int, Int>, key: Set<Pair<Int, Int>>): Boolean {
        return lockZeroSet == key.map { (y, x) -> Pair(pos.first+y, pos.second+x) }
            .filter { it.first in 0 until n && it.second in 0 until n }
            .toSet()
    }

    fun findRotatedKeys(key: Array<IntArray>): List<Array<IntArray>> =
        (0 until 3).fold(listOf(key)) { acc, _ ->
            val prevKey: Array<IntArray> = acc.lastOrNull()!!
            acc.plusElement(rotated90(prevKey))
        }


    private fun rotated90(arr: Array<IntArray>): Array<IntArray> {
        val n = arr.size; val m = arr[0].size
        val newArr = Array(m){ IntArray(n) }

        for(y in arr.indices) for(x in arr[y].indices){
            // (y', x') = (-x, y)
            newArr[y][x] = arr[m-1-x][y]
        }

        return newArr
    }

    infix fun IntRange.product(r2: IntRange) =
        sequence<Pair<Int, Int>>{
            for(k1 in this@product) for(k2 in r2) yield(k1 to k2)
        }

    ///////////////////////////////////////////////
    private fun testKey(key: Array<IntArray>){
        fun isKeyImmutable(key: Array<IntArray>): () -> Boolean {
            val keyBackup = key.map { it.copyOf() }.toTypedArray()
            return { key.contentDeepEquals(keyBackup) }
        }
        val isKeyImmutable: () -> Boolean = isKeyImmutable(key)
        val checkImmutabilityOfKey: () -> Unit = { check(isKeyImmutable()) { "Key MUST immutable." } }

        val key90 = rotated90(key)
        checkImmutabilityOfKey()

        val key180 = rotated90(key90)
        checkImmutabilityOfKey()

        val key270 = rotated90(key180)
        checkImmutabilityOfKey()

        val key360 = rotated90(key270)
        checkImmutabilityOfKey()

        fun Array<IntArray>.contentFlattenSorted(): List<Int> =
            this.map(IntArray::toList).flatten().sorted()

        check(listOf(key, key90, key180, key270, key360)
            .map{ it.contentFlattenSorted() }
            .distinct()
            .size
                == 1) { "check rotated key's element." }

        check(key.contentDeepEquals(key360)) { "(expected) key == key360" }

        println("testKey OK")
    }
}