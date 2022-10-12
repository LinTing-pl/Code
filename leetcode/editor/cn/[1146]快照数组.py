# 实现支持下列接口的「快照数组」- SnapshotArray： 
# 
#  
#  SnapshotArray(int length) - 初始化一个与指定长度相等的 类数组 的数据结构。初始时，每个元素都等于 0。 
#  void set(index, val) - 会将指定索引 index 处的元素设置为 val。 
#  int snap() - 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。 
#  int get(index, snap_id) - 根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。 
#  
# 
#  
# 
#  示例： 
# 
#  输入：["SnapshotArray","set","snap","set","get"]
#      [[3],[0,5],[],[0,6],[0,0]]
# 输出：[null,null,0,null,5]
# 解释：
# SnapshotArray snapshotArr = new SnapshotArray(3); // 初始化一个长度为 3 的快照数组
# snapshotArr.set(0,5);  // 令 array[0] = 5
# snapshotArr.snap();  // 获取快照，返回 snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // 获取 snap_id = 0 的快照中 array[0] 的值，返回 5 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= length <= 50000 
#  题目最多进行50000 次set，snap，和 get的调用 。 
#  0 <= index < length 
#  0 <= snap_id < 我们调用 snap() 的总次数 
#  0 <= val <= 10^9 
#  
#  Related Topics 设计 数组 哈希表 二分查找 👍 88 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from bisect import bisect_right


class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.length = length
        self.rec = collections.defaultdict(list)  # key表示index,val为[p,val]的列表
        # 这个val表示的是实时值，而不是增量值，不需要再次求前缀和
        self.p = 0  # 从0开始自增，记录操作数目
        self.sid = 0  # 从0开始自增，记录快照id
        self.srec = dict()  # key表示sid，val表示先前的p

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.rec[index].append([self.p, val])
        self.p += 1

    def snap(self):
        """
        :rtype: int
        """
        self.srec[self.sid] = self.p
        self.sid += 1
        self.p += 1
        return self.sid - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        p = self.srec[snap_id]  # 获取它所对应的有效pp
        # 找到 <= p的最后一个。在self.rec[index]里面二分找
        if not self.rec[index]:
            return 0
        else:
            k = bisect_right(self.rec[index], [p, 0xffffffff]) - 1
            if k < 0:
                return 0
            else:
                return self.rec[index][k][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# leetcode submit region end(Prohibit modification and deletion)
