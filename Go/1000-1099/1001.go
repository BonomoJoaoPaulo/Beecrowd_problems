package main

import (
	"fmt"
)

func main() {
	var first_value int
	var second_value int

	fmt.Scanln(&first_value)
	fmt.Scanln(&second_value)

	sum := first_value + second_value

	fmt.Println("X =", sum)
}
