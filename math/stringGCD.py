def gcdOfStrings(str1: str, str2: str):
    len1, len2 = len(str1), len(str2)
    start = min(len1, len2)

    def isDivisor(s):
        if len1 % s or len2 % s:
            return False

        factor1, factor2 = len1 // s, len2 // s
        return str1[:s] * factor1 == str1 and str2[:s] * factor2 == str2

    for s in range(start, 0, -1):
        if isDivisor(s):
            return str1[:s]

    return ""


print(gcdOfStrings("ABCABC", "ABC"))
