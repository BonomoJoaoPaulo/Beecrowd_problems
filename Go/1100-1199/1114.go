package main

import (
	"fmt"
)

func main() {
	for {
		var password int
		fmt.Scanln(&password)
		if password == 2002 {
			fmt.Println("Acesso Permitido")
			return
		} else {
			fmt.Println("Senha Invalida")
		}
	}
}
