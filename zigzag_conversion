#https://oj.leetcode.com/problems/zigzag-conversion/

'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".'''

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows==1:
            return s
        res = ''
        lens = len(s)
        for i in range(nRows):
            head = i
            calc = 2*nRows-2-2*i
            while head<lens:
                if calc!=0:
                    res += s[head]
                    head += calc
                calc = 2*nRows-2-calc
        return res
