class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen={}

        for i in range(len(nums)):
            current = nums[i]

            if current in seen:
                seen[current]+=1
            else:
                seen[current]=1


        count_list=[]

        for number, count in seen.items():
            count_list.append((count,number))

        count_list.sort(reverse=True)

        result=[]
        for i in range(k):
            result.append(count_list[i][1])

        return result



        