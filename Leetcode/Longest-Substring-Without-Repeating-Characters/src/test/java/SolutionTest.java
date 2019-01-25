import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class SolutionTest {
    Solution solution;

    @Before
    public void setUp() throws Exception {
        solution = new Solution();
    }

    @Test
    public void abcabcbb_의_답은_3_abc(){
        int result = solution.lengthOfLongestSubstring("abcabcbb");
        assertEquals( 3, result);
    }
    @Test
    public void bbbbb_의_답은_1_b(){
        int result = solution.lengthOfLongestSubstring("bbbbb");
        assertEquals(1, result);
    }
    @Test
    public void pwwkew_의_답은_3_wke(){
        int result = solution.lengthOfLongestSubstring("pwwkew");
        assertEquals(3, result);
    }
    @Test
    public void aab_의_답은_2_ab(){
        int result = solution.lengthOfLongestSubstring("aab");
        assertEquals(2, result);
    }
    @Test
    public void dvdf_의_답은_3_vdf(){
        int result = solution.lengthOfLongestSubstring("dvdf");
        assertEquals(3, result);
    }
    @Test
    public void anviaj_의_답은_5_nviaj(){
        int result = solution.lengthOfLongestSubstring("anviaj");
        assertEquals(5, result);
    }
    @Test
    public void abcabdbb_의_답은_4_cabd(){
        int result = solution.lengthOfLongestSubstring("abcabdbb");
        assertEquals(4, result);
    }
}