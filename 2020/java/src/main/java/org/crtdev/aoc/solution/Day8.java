package org.crtdev.aoc.solution;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.stream.Collectors;


@Data
@AllArgsConstructor
@Builder
class Instruction {
    public String operation;
    public int argument;
}

public class Day8 {

    private List<Instruction> input;

    public void read(String fileName) throws IOException {
        this.input = new ArrayList<>();
        ClassLoader classLoader = getClass().getClassLoader();
        InputStream inputStream = classLoader.getResourceAsStream(String.format("%s.txt", fileName));
        try (BufferedReader br = new BufferedReader(new InputStreamReader(inputStream))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] elements = line.split(" ");
                input.add(Instruction.builder()
                        .operation(elements[0])
                        .argument(Integer.parseInt(elements[1]))
                        .build());
            }
        }
    }

    public int solve() {
        return this.evaluate(this.input, false);
    }

    public Integer evaluate(List<Instruction> instructions, boolean p2) {
        int accumulator = 0;
        int i = 0;
        var tracker = new HashSet<>();

        while (i < instructions.size()) {
            var instruction = instructions.get(i);

            if (tracker.contains(i)) {
                if (p2) {
                    return null;
                } else {
                    break;
                }

            } else {
                tracker.add(i);
            }

            if (instruction.operation.equals("acc")) {
                accumulator += instruction.argument;
                i++;
            } else if (instruction.operation.equals("jmp")) {
                i += instruction.argument;
            } else if (instruction.operation.equals("nop")) {
                i++;
            }
        }

        return accumulator;
    }

    public int solve2() throws Exception {
        var target = new HashSet<>(Arrays.asList("jmp", "nop"));
        var filtered = this.input.stream().filter(i -> target.contains(i.operation))
                .collect(Collectors.toList());

        for (var item : filtered) {
            var copy = new ArrayList<>(this.input);
            int index = copy.indexOf(item);
            var newInstruction = Instruction.builder()
                    .operation(copy.get(index).operation.equals("jmp") ? "nop" : "jmp")
                    .argument(copy.get(index).argument).build();
            copy.set(index, newInstruction);

            Integer result = this.evaluate(copy, true);
            if (result != null) {
                return result;
            }
        }

        throw new Exception("Found no non looping solutions");
    }
}