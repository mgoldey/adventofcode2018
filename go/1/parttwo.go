package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
)

func contains(this_slice []int, target_value int) bool {
    for _, a_value := range this_slice {
        if a_value == target_value {
            return true
        }
    }
    return false
}

func main() {
    ctr := 0
    found_values := []int{0}
    for true {
        file, _ := os.Open("input.dat")
        scanner := bufio.NewScanner(file)
        for scanner.Scan() {
            myint, _ := strconv.Atoi(scanner.Text())
            ctr = ctr + myint
            if contains(found_values, ctr) {
                fmt.Println(ctr)
                os.Exit(0)
            } else {
                found_values = append(found_values, ctr)
            }
        }
    }
}
