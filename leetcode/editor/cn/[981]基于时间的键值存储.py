# 设计一个基于时间的键值数据结构，该结构可以在不同时间戳存储对应同一个键的多个值，并针对特定时间戳检索键对应的值。 
# 
#  实现 TimeMap 类： 
# 
#  
#  TimeMap() 初始化数据结构对象 
#  void set(String key, String value, int timestamp) 存储键 key、值 value，以及给定的时间戳 
# timestamp。 
#  String get(String key, int timestamp)
#  
#  返回先前调用 set(key, value, timestamp_prev) 所存储的值，其中 timestamp_prev <= timestamp 。
#  
#  如果有多个这样的值，则返回对应最大的 timestamp_prev 的那个值。 
#  如果没有值，则返回空字符串（""）。 
#  
#  
#  
#  
# 
#  示例： 
# 
#  
# 输入：
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4]
# , ["foo", 5]]
# 输出：
# [null, null, "bar", "bar", null, "bar2", "bar2"]
# 
# 解释：
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // 存储键 "foo" 和值 "bar" ，时间戳 timestamp = 1   
# timeMap.get("foo", 1);         // 返回 "bar"
# timeMap.get("foo", 3);         // 返回 "bar", 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，所以唯
# 一的值位于时间戳 1 处（即 "bar"） 。
# timeMap.set("foo", "bar2", 4); // 存储键 "foo" 和值 "bar2" ，时间戳 timestamp = 4  
# timeMap.get("foo", 4);         // 返回 "bar2"
# timeMap.get("foo", 5);         // 返回 "bar2"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= key.length, value.length <= 100 
#  key 和 value 由小写英文字母和数字组成 
#  1 <= timestamp <= 10⁷ 
#  set 操作中的时间戳 timestamp 都是严格递增的 
#  最多调用 set 和 get 操作 2 * 10⁵ 次 
#  
#  Related Topics 设计 哈希表 字符串 二分查找 👍 166 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from bisect import bisect_right
from collections import defaultdict


class TimeMap(object):

    def __init__(self):
        self.dct = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.dct[key].append([timestamp, value])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        a=bisect_right(self.dct[key], [timestamp, "z"*101])
        return "" if a == 0 else self.dct[key][a-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# leetcode submit region end(Prohibit modification and deletion)
