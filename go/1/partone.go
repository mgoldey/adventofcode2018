package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
)

func main() {

    // Perhaps the most basic file reading task is
    // slurping a file's entire contents into memory.
    file, _ := os.Open("input.dat")
    ctr := 0
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        myint, _ := strconv.Atoi(scanner.Text())
        ctr = ctr + myint
    }
    fmt.Println(ctr)
}
