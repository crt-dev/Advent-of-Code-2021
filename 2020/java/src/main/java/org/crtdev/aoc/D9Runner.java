package org.crtdev.aoc;

import org.crtdev.aoc.solution.Day9;

public class D9Runner {
    private static String EXERCISE = "d09";
    private static String EXAMPLE = EXERCISE + "ex";

    public static void main(String[] args) throws Exception {
        solve(EXAMPLE, 1, 5); //127
        solve(EXERCISE, 1, 25); //393911906
        solve(EXAMPLE, 2, 5); //62
        solve(EXERCISE, 2, 25); //59341885
    }

    public static void solve(String input, int part, int preamble) throws Exception {
        var solution = new Day9();
        solution.read(input);
        var p1 = part == 1 ? solution.solve(preamble, false) : solution.solve(preamble, true);
        System.out.println(String.format("Part %d%s: %s", part, input.equals(EXAMPLE) ? "ex" : "", p1));
    }
}