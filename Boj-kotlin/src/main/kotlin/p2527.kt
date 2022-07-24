package main.kotlin.p2527

fun main() = with(System.`in`.bufferedReader()){
    fun readInts() = readLine().split(" ").map(String::toInt)

    repeat(4){
        println(solve(lst=readInts()))
    }
}

fun solve(lst: List<Int>): String {
    val rect1 = Rectangle(bottomLeft = Point(x=lst[0],y=lst[1]), topRight = Point(x=lst[2], y=lst[3]))
    val rect2 = Rectangle(bottomLeft = Point(x=lst[4],y=lst[5]), topRight = Point(x=lst[6], y=lst[7]))

    return when {
        predicateD(rect1, rect2) -> "d"
        predicateC(rect1, rect2) -> "c"
        predicateB(rect1, rect2) -> "b"
        else -> "a"
    }
}
fun predicateC(rect1: Rectangle, rect2: Rectangle): Boolean {
    return rect1.bottomLeft == rect2.topRight || rect1.topRight == rect2.bottomLeft
            || rect1.bottomRight == rect2.topLeft || rect1.topLeft == rect2.bottomRight
}
fun predicateB(rect1: Rectangle, rect2: Rectangle): Boolean {
    return rect1.bottomLeft.x == rect2.topRight.x || rect1.topRight.x == rect2.bottomLeft.x ||
            rect1.bottomLeft.y == rect2.topRight.y || rect1.topRight.y == rect2.bottomLeft.y
}
fun predicateD(rect1: Rectangle, rect2: Rectangle): Boolean {
    return rect1.topRight.x < rect2.bottomLeft.x || rect1.bottomLeft.x > rect2.topRight.x ||
            rect1.bottomLeft.y > rect2.topRight.y || rect1.topRight.y < rect2.bottomLeft.y
}

data class Rectangle(val bottomLeft: Point, val topRight: Point){
    val bottomRight = Point(x=topRight.x, y=bottomLeft.y)
    val topLeft = Point(x=bottomLeft.x, y=topRight.y)
}

data class Point(val y: Int, val x: Int){
    override fun equals(other: Any?): Boolean {
        if(other is Point){
            return this.y == other.y && this.x == other.x
        }
        return false
    }

    override fun hashCode(): Int {
        var result = y
        result = 31 * result + x
        return result
    }
}
