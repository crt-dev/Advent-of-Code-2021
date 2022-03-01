package org.crtdev.aoc.solution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Day9 {

    private List<Long> input;

    public void read(String fileName) throws IOException {
        this.input = new ArrayList<>();
        ClassLoader classLoader = getClass().getClassLoader();
        InputStream inputStream = classLoader.getResourceAsStream(String.format("%s.txt", fileName));
        try (BufferedReader br = new BufferedReader(new InputStreamReader(inputStream))) {
            String line;
            while ((line = br.readLine()) != null) {
                input.add(Long.parseLong(line));
            }
        }
    }

    public boolean isValid(long target, List<Long> subList) {
        for (int j = 0; j < subList.size(); j++) {
            var v1 = subList.get(j);
            for (int k = 0; k < subList.size(); k++) {
                if (j == k) {
                    continue;
                }
                var v2 = subList.get(k);
                if (target == v1 + v2) {
                    return true;
                }
            }
        }
        return false;
    }

    public long solve(int preamble, boolean p2) throws Exception {
        for (int i = preamble; i < this.input.size(); i++) {
            List<Long> sublist = this.input.subList(i - preamble, i);
            var target = this.input.get(i);
            var valid = this.isValid(target, sublist);
            //System.out.println(String.format("%d %b", target, valid));
            if (!valid) {
                if (!p2) {
                    return target;
                } else {
                    var weaknessList = this.input.subList(0, i);
                    Long weakness = this.findWeakness(target, weaknessList);
                    //System.out.println(String.format("%d %b %d", target, valid, weakness));
                    if (weakness != null) {
                        return weakness;
                    }
                }

            }
        }

        throw new Exception("All values are valid");
    }

    public Long findWeakness(long target, List<Long> subList) {
        for (int j = 0; j < subList.size(); j++) {
            var continuousTotal = new ArrayList<Long>();
            continuousTotal.add(subList.get(j));
            for (int k = j + 1; k < subList.size(); k++) {
                continuousTotal.add(subList.get(k));
                long sum = continuousTotal.stream().mapToLong(t -> t).sum();
                if (sum == target) {
                    long min = continuousTotal.stream().mapToLong(t -> t).min().getAsLong();
                    long max = continuousTotal.stream().mapToLong(t -> t).max().getAsLong();
                    return min + max;
                } else if (sum < target) {
                    continue;
                } else {
                    break;
                }
            }
        }
        return null;
    }
}