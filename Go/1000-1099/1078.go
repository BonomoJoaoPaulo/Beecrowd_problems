package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scanln(&n)

	for i := 1; i < 11; i++ {
		tab := n * i
		fmt.Printf("%d x %d = %d\n", i, n, tab)
	}
}
