package main

import (
	"fmt"
	"io"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func parse_input(path string) (sort.IntSlice, sort.IntSlice) {
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
	var left, right sort.IntSlice
	for _, line := range lines {
		a := strings.Split(line, " ")
		fmt.Println(a)
		if len(a) == 4 {
			a_int, err := strconv.Atoi(a[0])
			if err != nil {
				panic(err)
			}
			b_int, err := strconv.Atoi(a[3])
			if err != nil {
				panic(err)
			}
			left = append(left, a_int)
			right = append(right, b_int)
		}
	}
	return left, right
}

func main() {
	left, right := parse_input("01_input.txt")
	sort.Sort(left)
	sort.Sort(right)
	var sum int = 0
	var similarity int = 0
	for i, l := range left {
		sum += int(math.Abs(float64(l - right[i])))
		similarity += Counts(right, l) * l
	}
	fmt.Println(sum)
	fmt.Println(similarity)
}

func Counts[S ~[]E, E comparable](s S, e E) int {
	var n int
	for _, v := range s {
		if v == e {
			n++
		}
	}
	return n
}
