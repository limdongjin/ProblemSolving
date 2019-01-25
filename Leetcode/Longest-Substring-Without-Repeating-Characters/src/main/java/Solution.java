import java.util.HashSet;

public class Solution {
    /*
    * Given a string, find the length of the longest substring without repeating characters.
    */
    public int lengthOfLongestSubstring(String s) {
        // 한 글자씩만 나와야한다. ex, abca 는 a 가 두번나오므로 안된다.
        int maxLength = 0;
        int i=0, j=0;
        int length = s.length();
        HashSet<Character> stringSet = new HashSet<>();

        while (j < length) {
            if(i > j) break;
            if (!stringSet.contains(s.charAt(j))){
                stringSet.add(s.charAt(j++));
                maxLength = Math.max(maxLength, j - i);
                continue;
            }
            stringSet.remove(s.charAt(i++));

        }

        return maxLength;
    }

}
