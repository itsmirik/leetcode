from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.is_palindrome(word):
                return word

        return ''

    def is_palindrome(self, word: str) -> bool:
        n = len(word)
        if n == 1:
            return True

        left, right = 0, n - 1
        while left < right:
            if word[left] != word[right]:
                return False

            left += 1
            right -= 1

        return True


if __name__ == '__main__':
    # print(Solution().firstPalindrome(["abc", "car", "ada", "racecar", "cool"]))
    # print(Solution().is_palindrome('atata'))
    # print(Solution().firstPalindrome(["notapalindrome","racecar"]))
    # print(Solution().firstPalindrome(["def", "ghi"]))
    # print(Solution().firstPalindrome(["xngla", "e", "itrn", "y", "s", "pfp", "rfd"]))
    print(Solution().firstPalindrome(
        [
            "knywrurkwbrtpalvuuzbczcwzpdqibcwwyflwiddixemsrwblupyerjgvcpavdjfhmujitcsmdbvhxw",
            "ovkeowhqvwlndtpxdnimgietvjsqydbuuwmxkfxxgn",
            "damomwtjugmsrfyvytaheg",
            "bngqatscosdakdwjz",
            "jwzcowuantgqlzjrzgpapcugxvviltrhmcwijtpqapmxjfcilrsmsbeffphcxmaozlczncoxxjmuqijhidxqinhywrtah",
            "ujvoejixvaioikkwzxgtmkchckrigfejjpheiiehpjjefgirkchckmtgxzwkkioiavxijeovju",
            "kacjvcouuigbhydrryaperxvjetwsycmnlkxujaqngjhhotqskclquklxsozfryfxwiksstmropcdvhgsnosgvltqo",
            "qrbsdxxolwzmyltproznfgyydxkkejwdiwpvfzvjoxqvwguoerhclytzvolymbxummwsoqtttyttik",
            "tkekt",
            "esrshrlfoihhjrouleucwpeubygivoatrfraphgwpvtkanwu",
            "kwzrfelynncvsrwvaukiinhjdydmlimggjldhflygemzwnjizzlsuqwahsufwmwhfjkjpngdfsudyavtogoaqzknpew",
            "sdgpcnvsbzxhyjt"
        ]
    ))
