class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Solution is to create a frequency hashmap that counts each character and the frequency it appears in the string. Then compare the 2
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}
        for i in range(len(s)):
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            t_count[t[i]] = 1 + t_count.get(t[i], 0)

        for ch in s_count:
            if s_count[ch] != t_count.get(ch, 0):
                return False

        return True

    def isAnagramSorted(self, s: str, t: str) -> bool:
        """
        Alternatively, we can use pythons built in TimSort and check if the strings equal each other.
        Time Complexity: O(nlogn)
        Space Complexity: O(1) or O(n) if we count the built in sort creating extra space
        """
        return sorted(s) == sorted(t)


def main():
    sol = Solution()
    test_1 = ("anagram", "nagaram")  # True
    test_2 = ("rat", "car")  # False

    for test in [test_1, test_2]:
        print(sol.isAnagram(*test))


if __name__ == "__main__":
    main()
