package main.kotlin.p17825

fun combsWithRep(n: Int, lst: List<Int>): List<List<Int>> = when(n){
    0 -> listOf(emptyList())
    else -> when(lst.isEmpty()){
        true -> emptyList()
        false -> combsWithRep(n-1, lst)
                    .map(listOf(lst[0])::plus)
                    .plus(combsWithRep(n, lst.subList(1, lst.size)))
    }
}

fun <T> permutations(el: List<T>, fin: List<T> = listOf(), sub: List<T> = el): List<List<T>> {
    return if(sub.isEmpty()) listOf(fin)
        else sub.distinct().flatMap { permutations(el, fin+it, sub-it) }
}

enum class Track(val id: Int) {
    T_DEFAULT(1), T_10_19(2),
    T_20_24(3), T_25_35(4),
    T_30_26(5)
}

data class Piece(var track: Track, var index: Int)
typealias Pieces = List<Piece>

fun score(piece: Piece): Int = with(piece) {
    return when(track){
        Track.T_DEFAULT -> index*2
        Track.T_10_19 -> 10 + index*3
        Track.T_20_24 -> 20 + index*2
        Track.T_25_35 -> 25 + index*5
        Track.T_30_26 -> when(index){
            0 -> 30
            1 -> 28
            2 -> 27
            3 -> 26
            else -> -1
        }
    }
}

fun Pieces.move(id: Int, v: Int): Int {
    // val piece = this[id]
    val piece = this[id]

    if(piece.index == 21) return -1

    piece.index += v
    when (piece.track) {
        Track.T_DEFAULT -> {
            if (piece.index > 20) return 0

            // 트랙이 바뀌는 지점
            when(piece.index){
                5 -> {
                    piece.track = Track.T_10_19
                    piece.index = 0
                }
                10 -> {
                    piece.track = Track.T_20_24
                    piece.index = 0
                }
                15 -> {
                    piece.track = Track.T_30_26
                    piece.index = 0
                }
                else -> {}
            }
        }
        Track.T_10_19 -> {
            when(piece.index){
                in 4..6 -> {
                    piece.track = Track.T_25_35
                    piece.index = piece.index - 4
                }
                7 -> {
                    piece.track = Track.T_DEFAULT
                    piece.index = 20
                }
                in 8..50 -> {
                    piece.track = Track.T_DEFAULT
                    piece.index = 21
                    return 0
                }
                else -> {}
            }
        }
        Track.T_20_24 -> {
            when(piece.index){
                in 3..5 -> {
                    piece.track = Track.T_25_35
                    piece.index = piece.index - 3
                }
                6 -> {
                    piece.track = Track.T_DEFAULT
                    piece.index = 20
                }
                in 7..50 -> {
                    piece.track = Track.T_DEFAULT
                    piece.index = 21
                    return 0
                }
                else -> {}

            }
        }
        Track.T_25_35 -> {
            when(piece.index){
                3 -> {
                    piece.track = Track.T_DEFAULT
                    piece.index = 20
                }
                in 4..50 -> {
                    piece.track = Track.T_DEFAULT
                    piece.index = 21
                    return 0
                }
            }
        }
        Track.T_30_26 -> {
            when(piece.index){
                in 4..6 -> {
                    piece.track = Track.T_25_35
                    piece.index = piece.index - 4
                }
                7 -> {
                    piece.track = Track.T_DEFAULT
                    piece.index = 20
                }
                in 8..50 -> {
                    piece.track = Track.T_DEFAULT
                    piece.index = 21
                    return 0
                }
                else -> {}
            }
        }
    }

    // 이동할 칸에 다른 말 있는지 체크
    for (i in this.indices) {
        if(i == id) continue
        if (piece.track == this[i].track && piece.index == this[i].index){
            return -1
        }
    }

    // 현재 칸의 점수 반환
    return score(piece)
}

fun solve(numbers: List<Int>): Int {
    fun simulate(case: List<Int>): Int {
        val pieces: Pieces = List(4) { Piece(Track.T_DEFAULT, 0) }
        var sum = 0

        for ((index, pieceId) in case.withIndex()) {
            sum += pieces.move(pieceId, numbers[index])
                .takeIf { it >= 0 } ?: return -1
        }

        return sum
    }

    return combsWithRep(10, (0..3).toList())
        .asSequence()
        .flatMap(::permutations)
        .maxOf(::simulate)
}

fun main() {
    val numbers = readln().split(" ").map(String::toInt)
    println(solve(numbers))
}
