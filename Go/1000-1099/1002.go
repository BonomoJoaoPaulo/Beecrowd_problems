package main

import (
	"fmt"
)

func main() {
	pi := 3.14159

	var radius float64
	fmt.Scanln(&radius)

	area := pi * radius * radius // We can also use math.Pow9(radius, 2)

	fmt.Printf("A=%.4f\n", area)

}
