# 804 Unique Morse Code Words
def word_to_morse(word):
    morse_map = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    morse_str = ''
    for char in word:
        index = ord(char) - ord('a')
        morse_str += morse_map[index]
    return morse_str

def get_num_unique_morse_code_words(words):
    unique_morse_words = {}
    count = 0
    for word in words:
        morse_word = word_to_morse(word)
        if not morse_word in unique_morse_words:
            count += 1
            unique_morse_words[morse_word] = True
    return count