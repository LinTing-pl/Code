# 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其
# 余元素是 emails 表示该账户的邮箱地址。 
# 
#  现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为
# 人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。 
# 
#  合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是 按字符 ASCII 顺序排列 的邮箱地址。账户本身可以以 任意顺序 返回。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", 
# "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], [
# "Mary", "mary@mail.com"]]
# 输出：[["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']
# ,  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# 解释：
# 第一个和第三个 John 是同一个人，因为他们有共同的邮箱地址 "johnsmith@mail.com"。 
# 第二个 John 和 Mary 是不同的人，因为他们的邮箱地址没有被其他帐户使用。
# 可以以任何顺序返回这些列表，例如答案 [['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
# ['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']] 也是正确的
# 。
#  
# 
#  示例 2： 
# 
#  
# 输入：accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin",
# "Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co",
# "Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.
# co","Fern1@m.co","Fern0@m.co"]]
# 输出：[["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co",
# "Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],[
# "Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.
# co","Fern5@m.co"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= accounts.length <= 1000 
#  2 <= accounts[i].length <= 10 
#  1 <= accounts[i][j].length <= 30 
#  accounts[i][0] 由英文字母组成 
#  accounts[i][j] (for j > 0) 是有效的邮箱地址 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 字符串 👍 357 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        parent = {}
        size = {}  # 用来存储每个父节点对应多少个邮箱 方便路径优化
        names = {}

        # 并查集 并
        def find(x):
            if x not in parent:
                parent[x] = x
                size[x] = 1
            else:
                while x != parent[x]:
                    x = parent[x]
            return x

        # 并查集 查  并做路径优化，小树挂在大树下面
        def union(x, y):
            u, v = find(x), find(y)
            if u != v:
                if size[u] >= size[v]:
                    size[u] += size[v]
                    parent[v] = u
                else:
                    size[v] += size[u]
                    parent[u] = v

        for account in accounts:
            names[account[1]] = account[0]  # 把第一个邮箱和名字关联在names里不去管他
            parent[account[1]] = find(account[1])  # 把同一个account里的邮箱都关联在第一个邮箱下面作他的子节点
            for i in range(2, len(account)):
                union(account[1], account[i])

        # 并查集 集合 这里小小改动一下 不是丢到集合里了 而是丢到字典里去重
        mydict = dict()
        for key in parent:
            temp = find(key)
            if temp in mydict:
                mydict[temp].append(key)  # 这里其实也可以用二分插入 直接维护一个邮箱是排序好的列表，这样可以省的后面还要排序
            else:
                mydict[temp] = [key]
        res = []
        for key in mydict:
            res.append([names[key]] + sorted(mydict[key]))
        return res
# leetcode submit region end(Prohibit modification and deletion)
