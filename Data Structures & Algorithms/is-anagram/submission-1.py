class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        seen ={}

        for i in range(len(s)):
            current_str=s[i]

            if current_str in seen:
                seen[current_str]+=1

            else:
                seen[current_str]=1

        for i in range(len(t)):
            current_str=t[i]

            if current_str in seen:
                seen[current_str]-= 1
            else:
                return False

        for count in seen.values():
            if count!=0:
                return False

        return True
            


        