from typing import List
class Solution:

    PASS="Guilherme"
    PASS_LEN=len(PASS)
    def encode(self, strs: List[str]) -> str:
        j, e = 0, ""
        for s in strs:
            l = len(s)
            e += str(l) + "&" + self._encode(j, s)
            j += 1
        return e

    def _encode(self, j: int, s: str) -> str:
        e = ""
        for c in s:
            p = ord(self.PASS[j % self.PASS_LEN])
            c = ord(c)
            e += f"{p * c}#"

        return e

    def decode(self, s: str) -> List[str]:
        i, j, e = 0, 0, ''
        size, decoded, word, letter = None, [], '', ''
        for c in s:
            if c == '&':
                size = int(letter)
                i, letter = 0, ''
                continue

            if c == '#':
                i += 1
                word += self._decode(j, letter)
                letter = ''
                continue

            if i == size:
                decoded.append(word)
                j += 1
                i, word, letter = 0, '', c
                continue

            letter += c

        if size is not None:
            decoded.append(word)

        return decoded

    def _decode(self, j: int, c: str) -> str:
        if c == '':
            return ''

        c = int(c)
        p = ord(self.PASS[j % self.PASS_LEN])
        return chr(int(c / p))

s = Solution()
# encoded = s.encode(["oi", "asd"])
# print("Encoded: ", encoded)
# print("Decoded: " + " ".join(s.decode(encoded)))

# encoded = s.encode(["neet","code","love","you"])
# print("Encoded: ", encoded)
# print("Decoded: " + " ".join(s.decode(encoded)))

# encoded = s.encode(["we","say",":","yes"])
# print("Encoded: ", encoded)
# print("Decoded: " + " ".join(s.decode(encoded)))

encoded = s.encode([""])
print("Encoded: ", encoded)
print("Decoded", s.decode(encoded))
print("Decoded: " + " ".join(s.decode(encoded)))