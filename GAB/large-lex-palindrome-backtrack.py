class Solution:
    def lexPalindromicPermutation(self, s, target):
        target_str = target

        cnt = []
        for i in range(26):
            cnt.append(0)

        for i in range(len(s)):
            ch = s[i]
            index = ord(ch) - ord('a')
            cnt[index] = cnt[index] + 1

        odd = 0
        mid_char = ""

        for i in range(26):
            if cnt[i] % 2 != 0:
                odd = odd + 1
                mid_char = chr(i + ord('a'))

        if odd > 1:
            return ""

        half_cnt = []
        for i in range(26):
            half_cnt.append(cnt[i] // 2)

        n_half = len(s) // 2

        half_str = []
        for i in range(n_half):
            half_str.append("")

        def find(k, is_greater):
            if k == n_half:
                rev_half = []
                i = len(half_str) - 1
                while i >= 0:
                    rev_half.append(half_str[i])
                    i = i - 1

                res = ""
                for c in half_str:
                    res = res + c
                res = res + mid_char
                for c in rev_half:
                    res = res + c

                if res > target_str:
                    return True
                else:
                    return False

            if is_greater:
                start = ord('a')
            else:
                start = ord(target_str[k])

            c_ord = start
            while c_ord <= ord('z'):
                idx = c_ord - ord('a')

                if half_cnt[idx] > 0:
                    half_str[k] = chr(c_ord)
                    half_cnt[idx] = half_cnt[idx] - 1

                    if find(k + 1, is_greater or chr(c_ord) > target_str[k]):
                        return True

                    half_cnt[idx] = half_cnt[idx] + 1

                c_ord = c_ord + 1

            return False

        if find(0, False):
            result = ""
            for c in half_str:
                result = result + c

            result = result + mid_char

            i = len(half_str) - 1
            while i >= 0:
                result = result + half_str[i]
                i = i - 1

            return result

        return ""


sol = Solution()

s = "aabb"
target = "abba"

output = sol.lexPalindromicPermutation(s, target)
print("Input string:", s)
print("Target string:", target)
print("Output:", output)