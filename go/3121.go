func numberOfSpecialChars(word string) int {
    letter := map[rune]bool{}
    for _, c := range word{
        letter[c] = true
        if letter[c - 32]{
            letter[c] = false
        }
    }

    var special_count = 0
    for i:='A'; i <= 'Z'; i++{
        if letter[i] && letter[i + 32]{
            special_count++
        }
    }
    return special_count
}