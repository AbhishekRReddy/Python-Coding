class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Convert the string into the string with lower letters and no numeric
        #Slice notatiion [start:end:step]
        new_str = ''
        for l in s:
            if l.isalnum():
                new_str += l.lower()
        rev_str = new_str[::-1]
        print(rev_str)
        return new_str == rev_str


        
