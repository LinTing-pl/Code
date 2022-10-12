# 给定一个整数数组 arr ，以及一个整数 target 作为目标值，返回满足 i < j < k 且 arr[i] + arr[j] + arr[k] ==
#  target 的元组 i, j, k 的数量。 
# 
#  由于结果会非常大，请返回 10⁹ + 7 的模。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [1,1,2,2,3,3,4,4,5,5], target = 8
# 输出：20
# 解释：
# 按值枚举(arr[i], arr[j], arr[k])：
# (1, 2, 5) 出现 8 次；
# (1, 3, 4) 出现 8 次；
# (2, 2, 4) 出现 2 次；
# (2, 3, 3) 出现 2 次。
#  
# 
#  示例 2： 
# 
#  
# 输入：arr = [1,1,2,2,2,2], target = 5
# 输出：12
# 解释：
# arr[i] = 1, arr[j] = arr[k] = 2 出现 12 次：
# 我们从 [1,1] 中选择一个 1，有 2 种情况，
# 从 [2,2,2,2] 中选出两个 2，有 6 种情况。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= arr.length <= 3000 
#  0 <= arr[i] <= 100 
#  0 <= target <= 300 
#  
#  Related Topics 数组 哈希表 双指针 计数 排序 👍 96 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        ans = 0
        arr.sort()

        for i, x in enumerate(arr):
            # We'll try to find the number of i < j < k
            # with A[j] + A[k] == T, where T = target - A[i].

            # The below is a "two sum with multiplicity".
            T = target - arr[i]
            j, k = i + 1, len(arr) - 1

            while j < k:
                # These steps proceed as in a typical two-sum.
                if arr[j] + arr[k] < T:
                    j += 1
                elif arr[j] + arr[k] > T:
                    k -= 1
                # These steps differ:
                elif arr[j] != arr[k]:  # We have A[j] + A[k] == T.
                    # Let's count "left": the number of A[j] == A[j+1] == A[j+2] == ...
                    # And similarly for "right".
                    left = right = 1
                    while j + 1 < k and arr[j] == arr[j + 1]:
                        left += 1
                        j += 1
                    while k - 1 > j and arr[k] == arr[k - 1]:
                        right += 1
                        k -= 1

                    # We contributed left * right many pairs.
                    ans += left * right
                    ans %= MOD
                    j += 1
                    k -= 1

                else:
                    # M = k - j + 1
                    # We contributed M * (M-1) / 2 pairs.
                    ans += (k - j + 1) * (k - j) / 2
                    ans %= MOD
                    break

        return ans
# leetcode submit region end(Prohibit modification and deletion)
