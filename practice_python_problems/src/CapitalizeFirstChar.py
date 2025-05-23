class CapitalizeFirstChar:
    def convert_char_to_cap(self, input_word: str) -> str:
        if not input_word:
            return ""

        words = input_word.split(" ")
        result = []

        for word in words:
            if word and word[0].isalpha():
                word = word[0].upper() + word[1:]
                result.append(word)

        return " ".join(result)