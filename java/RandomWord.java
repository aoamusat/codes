import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomWord {

    public static void main(String[] args) {
        String champion = "", s;
        int i = 1;
        boolean ok;
        while (!StdIn.isEmpty()) {
            s = StdIn.readString();
            ok = StdRandom.bernoulli(1.0/(double) i);
            if (ok) {
                champion = s;
            }
            ++i;
        }
        StdOut.println(champion);

    }

}