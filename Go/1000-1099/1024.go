package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var numberOfTexts int
	fmt.Scan(&numberOfTexts)
	scanner := bufio.NewScanner(os.Stdin)
	fullEncryptedText := make([]string, 0, numberOfTexts)

	for i := 0; i < numberOfTexts; i++ {
		scanner.Scan()
		text := scanner.Text()
		//fmt.Println("text:", text)
		textAfterFirstPass := firstPass(text)
		//fmt.Println("textAfterFirstPass:", textAfterFirstPass)
		textAfterSecondPass := secondPass(textAfterFirstPass)
		//fmt.Println("textAfterSecondPass:", textAfterSecondPass)
		encryptedTextPiece := thirdPass(textAfterSecondPass)
		//fmt.Println("encryptedTextPiece:", encryptedTextPiece)

		fullEncryptedText = append(fullEncryptedText, encryptedTextPiece)
	}
	for _, text := range fullEncryptedText {
		fmt.Println(text)
	}
}

func firstPass(text string) string {
	runes := []rune(text)

	for i, char := range runes {
		if (char >= 'a' && char <= 'z') || (char >= 'A' && char <= 'Z') {
			runes[i] += 3
			if runes[i] > 'z' {
				runes[i] -= 26
			} else if runes[i] > 'Z' && runes[i] < 'a' {
				runes[i] -= 26
			}
		}
	}
	resultText := string(runes)

	return resultText
}

func secondPass(text string) string {
	runes := []rune(text)

	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	resultText := string(runes)

	return resultText
}

func thirdPass(text string) string {
	runes := []rune(text)
	mid := len(runes) / 2

	for i := mid; i < len(runes); i++ {
		runes[i] -= 1
	}
	resultText := string(runes)

	return resultText
}
