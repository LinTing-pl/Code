# 给定一个整数数组 nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。 
# 
#  示例 2: 
# 
#  
# 输入: nums = [1,2,3,4], k = 3
# 输出: false 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= len(nums) <= 16 
#  0 < nums[i] < 10000 
#  每个元素的频率在 [1,4] 范围内 
#  
#  Related Topics 位运算 记忆化搜索 数组 动态规划 回溯 状态压缩 👍 561 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # 划分子集的目标值
        target, rem = divmod(sum(nums), k)
        # 如果不能整除，可以直接返回
        if rem: return False

        # 递归调用，判断是否可以用当前的nums数组去凑到k个target
        # 注意，这里有递归调用，再次到这里的时候，groups还是那个groups，但是nums不是当初的nums了
        def search(groups):
            # 整个nums数组已经全用完了，还没有从递归中return上来，说明可以完成这个任务，所以return True
            if not nums: return True
            # 从nums中取出最大的数
            v = nums.pop()
            # 判断放到哪个组里面
            for i, group in enumerate(groups):
                # 如果这个组加上这个数v，还没有超过target
                if group + v <= target:
                    # 那么就把这个数放到这个组里
                    groups[i] += v
                    # 继续判断后续能否完成任务，如果可以，直接返回True，这会在递归中一路返回上去
                    # 在这里递归找到v应该放到哪个组里面
                    if search(groups): return True
                    # 否则，这个数不应该放到这个组里，把v从这个组里面拿出来，继续尝试其他的组
                    groups[i] -= v
                # 如果这个组有数字了，先不要往这个组放了，去放到下一个组
                # 感觉也有点启发式算法的意思，为什么要这么搞呢？
                # 因为数组被排序了，单调性原理
                if not group:
                    # print("break ... ")
                    break
            # print('nums:', nums, 'v:', v, 'Groups:', groups)
            # 找了一圈发现v没有找到对应的位置，必须把v放回去原来的数组
            nums.append(v)
            # 并且返回False，表示这次回溯是失败的，这个v没有找到对应位置
            return False

        # 排序，有助于快速拿到结果
        nums.sort()
        # 如果有比目标值大的数值在里面，可以直接返回FALSE
        if nums[-1] > target: return False
        # 如果有相等的，那么相等的必然自己成组，也不需要判断，从nums中去除，并且减少组的数目
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return search([0] * k)
# leetcode submit region end(Prohibit modification and deletion)
