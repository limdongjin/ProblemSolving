import java.util.HashMap;

public class Lcs {
    private HashMap<String, Integer> cache;

    public int length(String x, String y){
        x = " " + x;
        y = " " + y;
        cache = new HashMap<>();
        int res = _length(x, y, x.length() - 1, y.length() - 1);
        return res;
    }

    private int _length(String x, String y, int xi, int yi){
        String key_name = xi + "," + yi;
        int result = 0;
        if(xi == 0 || yi == 0) return 0;
        if(cache.containsKey(key_name)) return cache.get(key_name);

        if(x.charAt(xi) == y.charAt(yi)) result = _length(x, y, xi -1, yi -1) + 1;
        else result = Math.max(_length(x, y, xi -1, yi), _length(x, y, xi, yi-1));

        return result;
    }
}
