from wordle import dictionary, randomanswer

class Wordle:
    """Main Wordle game taking optional arguments of the answer and whether to check against the dictionary.
        random_daily changes answer every day (see github/preritdas/wordle)."""
    def __init__(self, word: str = 'hello', real_words: bool = True, random_daily: bool = False):
        self.word = word.upper()
        self.real_words = real_words
        if random_daily == True:
            self.word = randomanswer.random_answer(daily=True)

    def run(self):
        """Run the game. Depends on bool real_words from instantiation."""

        # Answer viability test
        if len(self.word) != 5:
            raise Exception("The answer has to be a five-letter word.")
        if self.real_words == True and self.word.lower() not in dictionary.words:
            raise Exception(
                "The answer has to be a real word as you indicated you want dictionary checking."
                )

        # Begin iterating for attempts (6)
        for i in range(6):  # 6 attempts
            # For duplicate checking
            self.word_dup = list(self.word)

            failed_dictionary_test = False # by default

            # User attempt
            guess = str(input(f"Attempt {i + 1} >>> ")).upper()

            # Cheating checks

            # real_words = True
            if self.real_words == True and guess.lower() not in dictionary.words:
                failed_dictionary_test = True

            while (
                failed_dictionary_test == True
                or " " in guess
                or len(guess) > len(self.word)
            ):
                if " " in guess:
                    print(
                        "You can't have multiple words in your guess. Please run again."
                    )
                elif len(guess) > len(self.word):
                    print(
                        f"You can't guess a word with more than {len(list(self.word))} letters. Please run again."
                    )
                elif failed_dictionary_test == True: # Not a real word
                    print("That's not a real word. Try again.")
                guess = str(input(f"Attempt {i + 1} >>> ")).upper()

                # Correct failed dictionary test if real word is guessed
                if guess.lower() in dictionary.words:
                    failed_dictionary_test = False

            # prepare response list
            response = ['', '', '', '', '']

            # first correctness check
            for j in range(len(guess)):
                if guess[j] in self.word_dup and guess[j] == self.word[j]:
                    response[j] = f"*{guess[j]}*   "
                    self.word_dup.remove(guess[j])  # Duplicates

            # next present and absent check
            for j in range(len(guess)):
                # already response skip
                if response[j] != "":
                    continue
                # it's present(yellow)
                if guess[j] in self.word_dup:
                    response[j] = guess[j] + "   "
                    self.word_dup.remove(guess[j])  # Duplicates
                # other absent
                else:
                    response[j] = guess[j].lower() + "   "

            responseString = ""
            for letter in response:
                responseString += letter

            print(responseString)

            if guess == self.word:
                if (i + 1) == 1: # Passed in one try
                    print(f"Congratulations, you passed the wordle in {i + 1} try.")
                elif (i + 1) > 1:
                    print(f"Congratulations, you passed the wordle in {i + 1} tries.")
                else:
                    raise Exception("Fatal iteration error for largest for loop.")
                quit()
        print("You failed.")
        quit()