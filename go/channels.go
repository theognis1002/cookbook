package main

import "fmt"

func main() {

    messages := make(chan string)

    go func() { messages <- "ping" }()

    msg := <-messages
    fmt.Println(msg)
}

"""
	data := <- a // read from channel a  
	a <- data // write to channel a  
"""
