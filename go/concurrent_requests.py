package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"sync"
)

// Struct to unmarshal the JSON response
type Response struct {
	Origin string `json:"origin"`
}

// Function to make an HTTP request and print the response
func fetchURL(wg *sync.WaitGroup, url string, id int) {
	defer wg.Done()

	resp, err := http.Get(url)
	if err != nil {
		fmt.Printf("Error fetching URL %d: %v\n", id, err)
		return
	}
	defer resp.Body.Close()

	var result Response
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		fmt.Printf("Error decoding response for URL %d: %v\n", id, err)
		return
	}

	fmt.Printf("Response from URL %d: %v\n", id, result)
}

func main() {
	var wg sync.WaitGroup
	url := "https://httpbin.org/ip"

	// Make 10 concurrent requests
	for i := 0; i < 10; i++ {
		wg.Add(1)
		go fetchURL(&wg, url, i+1)
	}

	// Wait for all requests to finish
	wg.Wait()
}