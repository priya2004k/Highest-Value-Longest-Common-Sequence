def parse_input(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    K = int(lines[0])

    value = {}
    for i in range(1, K + 1):
        char, val = lines[i].split()
        value[char] = int(val)

    A = lines[K + 1]
    B = lines[K + 2]

    return A, B, value

def HighestValueLongestCommonSequence(a, b, value):
    def dp(a, b, i, j, value):
        # base case if the length is 0
        if i == 0 or j == 0:
            return (0, "")

        # if last chars match this is a valid common subsequence
        if a[i - 1] == b[j - 1]:
            val, subseq = dp(a, b, i - 1, j - 1, value)
            return (val + value[a[i - 1]], subseq + a[i - 1])

        else:
            val1, subseq1 = dp(a, b, i, j - 1, value)
            val2, subseq2 = dp(a, b, i - 1, j, value)

            if val1 > val2:
                return (val1, subseq1)
            else:
                return (val2, subseq2)
    return dp(a, b, len(a), len(b), value)


if __name__ == "__main__":
    A, B, value = parse_input("inputs/test1.in")
    print(HighestValueLongestCommonSequence(A, B, value))