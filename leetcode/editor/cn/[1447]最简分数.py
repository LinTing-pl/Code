# 给你一个整数 n ，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于 n 的 最简 分数 。分数可以以 任意 顺序返回。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 2
# 输出：["1/2"]
# 解释："1/2" 是唯一一个分母小于等于 2 的最简分数。 
# 
#  示例 2： 
# 
#  输入：n = 3
# 输出：["1/2","1/3","2/3"]
#  
# 
#  示例 3： 
# 
#  输入：n = 4
# 输出：["1/2","1/3","1/4","2/3","3/4"]
# 解释："2/4" 不是最简分数，因为它可以化简为 "1/2" 。 
# 
#  示例 4： 
# 
#  输入：n = 1
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 100 
#  
#  Related Topics 数学 字符串 数论 👍 84 👎 0


# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        isPrime = [True] * (n + 1)
        primes = []
        for i in range(2, n + 1):
            if isPrime[i]:
                for j in range(i * i, n + 1, i):
                    isPrime[j] = False
                primes.append(i)
        ans = []
        # 枚举分母
        for i in range(2, n + 1):
            if isPrime[i]:
                ans += ["{}/{}".format(j, i) for j in range(1, i)]
            else:
                idx, ps = 0, set()
                # 分母的所有质因子
                while idx < len(primes) and primes[idx] < i // 2 + 1:
                    if not i % primes[idx]:
                        ps.add(primes[idx])
                    idx += 1
                s = set()
                # 构造分母的所有最大公约数不为1的分子
                for p in ps:
                    for j in range(p, i, p):
                        s.add(j)
                ans += ["{}/{}".format(j, i) for j in range(1, i) if j not in s]
        return ans
# leetcode submit region end(Prohibit modification and deletion)
