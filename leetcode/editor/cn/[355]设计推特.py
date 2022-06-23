# 设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近 10 条推文。 
# 
#  实现 Twitter 类： 
# 
#  
#  Twitter() 初始化简易版推特对象 
#  void postTweet(int userId, int tweetId) 根据给定的 tweetId 和 userId 创建一条新推文。每次调用此函
# 数都会使用一个不同的 tweetId 。 
#  List<Integer> getNewsFeed(int userId) 检索当前用户新闻推送中最近 10 条推文的 ID 。新闻推送中的每一项都必须是
# 由用户关注的人或者是用户自己发布的推文。推文必须 按照时间顺序由最近到最远排序 。 
#  void follow(int followerId, int followeeId) ID 为 followerId 的用户开始关注 ID 为 
# followeeId 的用户。 
#  void unfollow(int followerId, int followeeId) ID 为 followerId 的用户不再关注 ID 为 
# followeeId 的用户。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", 
# "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# 输出
# [null, null, [5], null, null, [6, 5], null, [5]]
# 
# 解释
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // 用户 1 发送了一条新推文 (用户 id = 1, 推文 id = 5)
# twitter.getNewsFeed(1);  // 用户 1 的获取推文应当返回一个列表，其中包含一个 id 为 5 的推文
# twitter.follow(1, 2);    // 用户 1 关注了用户 2
# twitter.postTweet(2, 6); // 用户 2 发送了一个新推文 (推文 id = 6)
# twitter.getNewsFeed(1);  // 用户 1 的获取推文应当返回一个列表，其中包含两个推文，id 分别为 -> [6, 5] 。推文 
# id 6 应当在推文 id 5 之前，因为它是在 5 之后发送的
# twitter.unfollow(1, 2);  // 用户 1 取消关注了用户 2
# twitter.getNewsFeed(1);  // 用户 1 获取推文应当返回一个列表，其中包含一个 id 为 5 的推文。因为用户 1 已经不再关注用
# 户 2 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= userId, followerId, followeeId <= 500 
#  0 <= tweetId <= 10⁴ 
#  所有推特的 ID 都互不相同 
#  postTweet、getNewsFeed、follow 和 unfollow 方法最多调用 3 * 10⁴ 次 
#  
#  Related Topics 设计 哈希表 链表 堆（优先队列） 👍 293 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Twitter(object):
    def __init__(self):
        self.count = 0
        self.user_post = collections.defaultdict(list)
        self.user_follow = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.user_post[userId].append([self.count, tweetId])
        self.count += 1

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        person = self.user_follow[userId]
        tmp = []
        tmp.extend(self.user_post[userId][-10:])
        for p in person:
            tmp.extend(self.user_post[p][-10:])
        tmp.sort(key=lambda x: -x[0])
        res = []
        for ele in tmp[:10]:
            res.append(ele[1])
        return res

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId != followeeId:
            self.user_follow[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.user_follow[followerId]:
            self.user_follow[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# leetcode submit region end(Prohibit modification and deletion)
