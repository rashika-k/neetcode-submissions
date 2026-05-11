"""
remove spaces, non alpha
is alnum(),lower

out:bool

edge case:

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cl_str = s.lower().replace(" ","")  

        left_ptr = 0
        right_ptr = len(s)-1

        while left_ptr < right_ptr:
            if not s[left_ptr].isalnum():
                left_ptr +=1
            elif not s[right_ptr].isalnum():
                right_ptr -=1
            elif s[left_ptr].lower() == s[right_ptr].lower():
                left_ptr +=1
                right_ptr -=1
            else:
                return False

            # if s[left_ptr] != s[right_ptr]:
            #     return False
            # else:
            #     left_ptr += 1
            #     right_ptr -= 1
        return True


        