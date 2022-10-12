# TinyURL是一种URL简化服务， 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl 时
# ，它将返回一个简化的URL http://tinyurl.com/4e9iAk. 
# 
#  要求：设计一个 TinyURL 的加密 encode 和解密 decode 的方法。你的加密和解密算法如何设计和运作是没有限制的，你只需要保证一个URL可
# 以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL。 
#  Related Topics 设计 哈希表 字符串 哈希函数 👍 145 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import numpy as np


class Codec:
    def __init__(self):
        self.diction = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        i = str(np.random.randint(0, 10000000))
        self.diction[i] = longUrl

        return 'http://tinyurl.com/' + i

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl[19:]
        return self.diction[key]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# leetcode submit region end(Prohibit modification and deletion)
