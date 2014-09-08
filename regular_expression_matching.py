#https://oj.leetcode.com/problems/regular-expression-matching/

'''Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
isMatch("aaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*a*c" ) → false
'''

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        #for the fxxking TLE! isMatch("aaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*a*c" ) 
        if p!='' and p[-1]!='*' and p[-1]!='.' and (s=='' or s[-1]!=p[-1]):
            return False
        while p!='' and p[-1]!='*' and p[-1]!='.' and s!='' and s[-1]==p[-1]:
            s = s[0:len(s)-1]
            p = p[0:len(p)-1]
        
        if p=='':
            return s==''
            
        if len(p)==1 or p[1]!='*':
            if s!='' and  (s[0]==p[0] or p[0]=='.'):
                return self.isMatch(s[1:],p[1:])
        else:
            if self.isMatch(s,p[2:]):
                return True
            while (s!='' and (s[0]==p[0] or p[0]=='.')):
                s = s[1:]
                if self.isMatch(s,p[2:]):
                    return True
        return False
