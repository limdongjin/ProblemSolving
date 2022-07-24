package main.kotlin.utils.factorial

tailrec fun factorial(n: Int, acc: Long = 1): Long = if(n <= 1) acc else factorial(n-1, n*acc)
//tailrec fun factorial(n: Long, acc: Long = 1L): Long = if(n == 1L) acc else factorial(n-1L, n*acc)
