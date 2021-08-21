class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                     "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                     "y", "z"]
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
                 ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-",
                 ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--",
                 "--.."]

        zip_chars = zip(alphabets, morse)
        char_dict = dict(zip_chars)

        all_morse_words = []

        for word in words:
            morse_chars = []
            for char in word:
                morse_chars.append(char_dict[char])
            morse_word = "".join(morse_chars)
            if morse_word not in all_morse_words:
                all_morse_words.append(morse_word)

        return len(all_morse_words)
