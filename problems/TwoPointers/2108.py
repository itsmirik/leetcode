from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        palindrome = ''

        for word in words:
            if word == word[::-1]:
                palindrome = word
                break

        if palindrome:
            return palindrome
        else:
            return ''


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
