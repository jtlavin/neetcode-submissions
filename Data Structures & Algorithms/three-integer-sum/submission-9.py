class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        solutions_list = []
        print(sorted_nums)
        for i in range(len(sorted_nums)):
            if i >0 and sorted_nums[i]==sorted_nums[i-1]:
                continue
            L, R = i+1, len(sorted_nums)-1
            while L < R:
                total_sum = sorted_nums[i] + sorted_nums[L] + sorted_nums[R]
                if total_sum < 0:
                    L += 1
                elif total_sum > 0:
                    R -= 1
                else:
                    print(f"i ={i}, L={L}, R={R}")
                    solutions_list.append([sorted_nums[i], sorted_nums[L], sorted_nums[R]])
                    L += 1
                    R -= 1
                    while L < R and sorted_nums[L]==sorted_nums[L-1]:
                        print(f"i ={i}, L={L}, R={R}")
                        L+=1
#                    if sorted_nums[R]==sorted_nums[R+1]:
#                        print(f"i ={i}, L={L}, R={R}")
#                        R -=1

        return solutions_list
