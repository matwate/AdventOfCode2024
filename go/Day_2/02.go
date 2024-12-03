package main

import (
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func parse_input(path string) []string {
	file, err := os.Open(path)
	if err != nil {
		panic(err)
	}
	defer func() {
		if err := file.Close(); err != nil {
			panic(err)
		}
	}()
	contents, err := io.ReadAll(file)
	if err != nil {
		panic(err)
	}
	lines := strings.Split(string(contents), "\n")
	return lines
}

func convert_to_int(input string) []int {
	split := strings.Split(input, " ")
	var result []int
	for _, i := range split {
		res, err := strconv.Atoi(i)
		if err != nil {
			panic(err)
		}
		result = append(result, res)
	}
	return result
}

func main() {
	parse_input("02_input.txt")
}
