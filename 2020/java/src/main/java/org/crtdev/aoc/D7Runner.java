package org.crtdev.aoc;

import org.crtdev.aoc.solution.Day7;

import java.io.IOException;

public class D7Runner {
    private static String EXERCISE = "d07";
    private static String EXAMPLE = EXERCISE + "ex";

    public static void main(String[] args) throws IOException {
        solve(EXAMPLE, 1); //4
        solve(EXERCISE, 1); //177
        solve(EXAMPLE, 2); //32
        solve(EXERCISE + "ex2", 2); //126
        solve(EXERCISE, 2); //34988
    }

    public static void solve(String input, int part) throws IOException {
        Day7 solution = new Day7();
        solution.read(input);
        var p1 = part == 1 ? solution.solve() : solution.solve2();
        System.out.println(String.format("Part %d%s: %s", part, input.equals(EXAMPLE) ? "ex" : "", p1));
    }
}

//53 + 31 = 84
