package main

import (
	"fmt"
)

// Function to sum numbers in a slice and send the result on a channel
func sum(numbers []int, resultChan chan int) {
	sum := 0
	for _, number := range numbers {
		sum += number
	}
	// Send the result to the channel
	resultChan <- sum
}

func main() {
	// Define some slices of numbers
	numbers1 := []int{1, 2, 3, 4, 5}
	numbers2 := []int{6, 7, 8, 9, 10}
	numbers3 := []int{11, 12, 13, 14, 15}

	// Create a channel to receive results
	resultChan := make(chan int, 3) // Buffered channel with capacity of 3

	// Start goroutines to compute the sum of each slice
	go sum(numbers1, resultChan)
	go sum(numbers2, resultChan)
	go sum(numbers3, resultChan)

	// Collect results from the channel
	totalSum := 0
	for i := 0; i < 4; i++ {
		totalSum += <-resultChan
	}

	// Print the total sum
	fmt.Println("Total Sum:", totalSum)
}
