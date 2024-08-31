package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)

	vector := make([]int, 0, 10)
	j := n

	for i := 0; i < 10; i++ {
		vector = append(vector, j)
		j *= 2
	}

	for index, value := range vector {
		fmt.Printf("N[%d] = %d\n", index, value)
	}
}
