import sys

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
    memo = {}
    def dp(i, j, value):
        # base case if the length is 0
        if i == 0 or j == 0:
            return (0, "")

        if (i, j) in memo:
            return memo[(i, j)]

        res = None
        # if last chars match this is a valid common subsequence
        if a[i - 1] == b[j - 1]:
            val, subseq = dp(i - 1, j - 1, value)
            res = (val + value[a[i - 1]], subseq + a[i - 1])

        else:
            val1, subseq1 = dp(i, j - 1, value)
            val2, subseq2 = dp(i - 1, j, value)

            if val1 > val2:
                res = (val1, subseq1)
            else:
                res =  (val2, subseq2)
        memo[(i, j)] = res
        return res
    return dp(len(a), len(b), value)


def main():
    args = sys.argv[1:]
    if args:
        input_file = str(args[0])

    else:
        input_file = 'tests/test1.in'

    A, B, value = parse_input(input_file)
    hv_result, hv_string = HighestValueLongestCommonSequence(A, B, value)
    output_file = input_file.removesuffix('.in') + '.out'

    with open(output_file, 'w') as f:
        f.write(str(hv_result) +'\n')
        f.write(str(hv_string) +'\n')

if __name__ == "__main__":
    main()