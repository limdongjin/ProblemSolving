package permutations

import main.kotlin.permutations.HeapsAlgorithms
import org.junit.jupiter.api.DynamicTest
import org.junit.jupiter.api.TestFactory
import kotlin.test.junit.JUnitAsserter.assertEquals

internal class HeapsAlgorithmsKtTest {

    private val arrays = listOf(
        arrayOf(1, 2, 3, 4, 5),
        arrayOf(5, 2, 3, 1, 4),
        arrayOf(1),
    )


    @TestFactory
    fun provideArrays() = arrays.map {
        DynamicTest.dynamicTest("permutation is valid?"){
            permutation_is_valid(it)
        }
    }

    private fun permutation_is_valid(a: Array<Int>) = with(HeapsAlgorithms) {
        val set = buildSet {
            permutations(a)
                .forEach { add(it.toList()) }
        }

        assertEquals(
            message = "is not exist duplicated data?",
            expected = (1..a.size).reduce(Int::times),
            actual = set.size
        )
    }

}