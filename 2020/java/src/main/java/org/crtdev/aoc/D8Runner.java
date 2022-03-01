package org.crtdev.aoc;

import org.crtdev.aoc.solution.Day8;

public class D8Runner {
    private static String EXERCISE = "d08";
    private static String EXAMPLE = EXERCISE + "ex";

    public static void main(String[] args) throws Exception {
        solve(EXAMPLE, 1); //5
        solve(EXERCISE, 1); //1709
        solve(EXAMPLE, 2); //8
        solve(EXERCISE, 2); //1976
    }

    public static void solve(String input, int part) throws Exception {
        Day8 solution = new Day8();
        solution.read(input);
        var p1 = part == 1 ? solution.solve() : solution.solve2();
        System.out.println(String.format("Part %d%s: %s", part, input.equals(EXAMPLE) ? "ex" : "", p1));
    }
}
