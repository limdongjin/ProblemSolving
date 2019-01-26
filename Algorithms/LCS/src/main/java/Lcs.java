import java.util.HashMap;

public class Lcs {
    private HashMap<String, Integer> cache;

    public final int length(String x, String y){
        cache = new HashMap<>();
        return _length(x, y, x.length() - 1, y.length() - 1);
    }

    private int _length(final String x, final String y, final int xi, final int yi){
        String key_name = xi + "," + yi;
        int result;
        if(xi == -1 || yi == -1) return 0;
        if(cache.containsKey(key_name)) return cache.get(key_name);

        if(x.charAt(xi) == y.charAt(yi)) result = _length(x, y, xi -1, yi -1) + 1;
        else result = Math.max(_length(x, y, xi -1, yi), _length(x, y, xi, yi-1));

        cache.put(key_name, result);

        return result;
    }
}
