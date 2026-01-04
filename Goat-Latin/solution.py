'''
You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

    If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
        For example, the word "apple" becomes "applema".
    If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
        For example, the word "goat" becomes "oatgma".
    Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
        For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.

Return the final sentence representing the conversion from sentence to Goat Latin.

'''

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        sentence = sentence.split(' ')
        for s in range(0,len(sentence)):
            if sentence[s][0] in vowels:
                sentence[s] = sentence[s]+"ma"+("a"*(s+1))
            else:
                sentence[s] = sentence[s][1:]+sentence[s][0]+"ma"+("a"*(s+1))
        return (' '.join(sentence))
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.toGoatLatin("I speak Goat Latin"))  # Output: "Imaa speakmaaa oatGmaaaa atinLmaaaaa"
    print(sol.toGoatLatin("The quick brown fox jumped over the lazy dog"))  # Output: "eThmaaa uickqmaaaa rownbmaaaaa oxfmaaaaaa umpedjmaaaaaaa overmaaaaaaaa hetmaaaaaaaaa azylmaaaaaaaaaa ogdmaaaaaaaaaaa"
    print(sol.toGoatLatin("Hello world"))  # Output: "elloHmaaa orldwmaaaa"
