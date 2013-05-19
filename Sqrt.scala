// uses Newton's method
object Sqrt {
    def abs(x: Double) = if (x >= 0) x else -x

    def sqrt(x: Double) = {
        def sqrtIter(guess: Double, x: Double): Double =
            if (isGoodEnough(guess, x)) guess 
            else sqrtIter(improve(guess, x), x) 
        def isGoodEnough(guess: Double, x: Double) =
            abs(guess * guess - x) / x < 0.0001 // note we divide by x so that it works for both large and small numbers

        def improve(guess: Double, x: Double) =
            (guess + x / guess) / 2
        sqrtIter(1.0, x)
    }

}

