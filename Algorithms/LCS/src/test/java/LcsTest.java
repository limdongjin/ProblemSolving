import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class LcsTest {
    Lcs lcs;
    @Before
    public void setUp(){
        lcs = new Lcs();
    }

    @Test
    public void 테스트3() {
        assertEquals(3, lcs.length("hello", "elo"));
    }
    @Test
    public void 비어있는문자열하나(){
        assertEquals(0, lcs.length("", "hello"));
    }
    @Test
    public void 둘다비어있는문자열(){
        assertEquals(0, lcs.length("", ""));
    }
    @Test
    public void 서로같은문자열(){
        assertEquals(11, lcs.length("hello world", "hello world"));
    }
    @Test
    public void 그냥테스트(){
        assertEquals(2, lcs.length("ABXC", "ADYC"));
    }
    @Test
    public void 테스트2(){
        assertEquals(3, lcs.length("ABXCD", "ADYCDD"));
    }
    @Test
    public void 공통부분없는경우(){
        assertEquals(0, lcs.length("ABXCD", "ZQWSRFLLL"));
    }
}