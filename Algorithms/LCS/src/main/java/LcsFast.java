import java.util.Arrays;
import java.util.HashMap;

public class LcsFast {
    private int[][] cache;
    public final int length(final String x, final String y){
        cache = new int[x.length() + 5][y.length() + 5];
        return _length(x, y, x.length() - 1, y.length() - 1);
    }

    private int _length(final String x, final String y, final int xi, final int yi){
        int result;

        if(xi == -1 || yi == -1) return 0;
        if(cache[xi][yi] != 0) return cache[xi][yi];
        if(x.charAt(xi) == y.charAt(yi)) result = _length(x, y, xi -1, yi -1) + 1;
        else result = Math.max(_length(x, y, xi -1, yi), _length(x, y, xi, yi -1));

        cache[xi][yi] = result;

        return result;
    }
}
