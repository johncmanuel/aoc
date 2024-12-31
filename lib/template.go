package main

import (
	"fmt"
	"os"
	"strings"
)

var f = "./input.txt"

func main() {
	f := "./input.txt"
	lines, err := readFileToArray(f)
	if err != nil {
		fmt.Println(err)
		return
	}
	soln1(lines)
	soln2(lines)
}

func soln1(lines []string) {
	// get the soln my man
}

func soln2(lines []string) {
	// get the soln my man
}

func readFileToArray(filename string) ([]string, error) {
	content, err := os.ReadFile(filename)
	if err != nil {
		return nil, fmt.Errorf("error reading file: %v", err)
	}

	lines := strings.Fields(string(content))

	return lines, nil
}
