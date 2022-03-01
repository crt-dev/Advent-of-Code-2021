package org.crtdev.aoc.solution;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Data
@AllArgsConstructor
@Builder
class Bag {
    public String colour;
    public int number;
}

public class Day7 {

    private Map<String, List<Bag>> input;

    public void read(String fileName) throws IOException {
        this.input = new HashMap<>();
        ClassLoader classLoader = getClass().getClassLoader();
        InputStream inputStream = classLoader.getResourceAsStream(String.format("%s.txt", fileName));

        try (BufferedReader br = new BufferedReader(new InputStreamReader(inputStream))) {
            String line;
            while ((line = br.readLine()) != null) {
                line = line.replace(".", "");
                line = line.replace("bags", "");
                line = line.replace("bag", "");
                String[] elements = line.split("  contain ");

                List<Bag> bags = new ArrayList<>();
                if (!elements[1].contains("no other")) {
                    String[] contents = elements[1].split(", ");
                    for (String content : contents) {
                        bags.add(Bag.builder()
                                .number(Integer.parseInt(content.substring(0, 1)))
                                .colour(content.substring(2).trim())
                                .build());
                    }
                }
                this.input.put(elements[0], bags);
            }
        }
    }

    public int solve() {
        int bagsWithShinyGold = 0;
        for (var bag : this.input.entrySet()) {
            int numShinyGold = this.findShinyGoldNum(bag.getKey());
            if (numShinyGold >= 1) {
                bagsWithShinyGold++;
            }
        }

        return bagsWithShinyGold;
    }

    private int findShinyGoldNum(String bag) {
        var contents = this.input.get(bag);
        int shinyGoldNum = 0;
        if (!contents.isEmpty()) {
            for (var content : contents) {
                if (content.colour.equals("shiny gold")) {
                    shinyGoldNum += content.number;
                } else {
                    shinyGoldNum += this.findShinyGoldNum(content.colour);
                }
            }
        }
        return shinyGoldNum;
    }

    public int solve2() {
        return this.getBags("shiny gold");
    }

    private int getBags(String bag) {
        var contents = this.input.get(bag);
        int count = 0;
        if (!contents.isEmpty()) {
            for (var content : contents) {
                int bags = content.number;
                int subBags = this.getBags(content.colour);
                count += bags + (bags * subBags);
            }
        }
        return count;
    }
}