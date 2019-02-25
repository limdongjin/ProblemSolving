public class LcsIteration {
    public final int length(final String x, final String y){
        int[][] cache = new int[x.length() + 5][y.length() + 5];
        int xLength = x.length(), yLength = y.length();
        if(x.length() == 0|| y.length() == 0) return 0;

        for (int xi = 0; xi < xLength; xi++) {
            for(int yi = 0; yi < yLength; yi++) {
                boolean isSameChar = (x.charAt(xi) == y.charAt(yi));
                boolean isZeroXiOrYi = (xi == 0 || yi == 0);
                boolean isZeroXi = (xi == 0);
                boolean isZeroYi = (yi == 0);
                if(isSameChar && !isZeroXiOrYi){
                    cache[xi][yi] = cache[xi - 1][yi -1] + 1;
                }else if(isSameChar){
                    cache[xi][yi] = 1;
                }else if(isZeroXiOrYi){
                    if(isZeroXi && !isZeroYi) cache[xi][yi] = cache[xi][yi - 1];
                    else if(!isZeroXi) cache[xi][yi] = cache[xi - 1][yi];
                }else{
                    cache[xi][yi] = Math.max(cache[xi - 1][yi], cache[xi][yi - 1]);
                }
            }
        }
        return cache[xLength - 1][yLength - 1];
    }
}
