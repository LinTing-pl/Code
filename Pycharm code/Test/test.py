#!/Users/env python
# -*- coding:utf-8 -*-
# @author：麟听 WeChat:15019763969


# ①
# def jiecheng(num):
#     """求阶乘，num为阶乘"""
#     if num > 0:
#         return num * jiecheng(num - 1)
#     else:
#         return 1


# ②
# import math
# def S(radius):
#     """求圆的面积,radius为圆的半径"""
#     return radius**2*math.pi


# ③
# def issushu(num):
#     """判断是否是素数"""
#     if num <= 1:
#         return False
#     if num == 2:
#         return True
#     for i in range(2, int(num / 2) + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# def sushu(a, b, start=True, end=False):
#     """求区间所有的素数，默认为[a,b)左闭右开区间"""
#     result = []
#     if start:
#         a = a
#     else:
#         a = a + 1
#     if end:
#         b = b + 1
#     else:
#         b = b
#     for i in range(a, b):
#         if issushu(i):
#             result.append(i)
#     return result


# ④
# def nPingFanHe(num):
#     """求前n项的平方和"""
#     result = sum(map(lambda x: x ** 2, range(1, num + 1)))
#     return result


# ⑤
# def isOushu(num):
#     """判断是否是偶数"""
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
#
# def oushu(a, b, start=True, end=False):
#     """求区间中的偶数，默认[a,b),左闭右开区间"""
#     result = []
#     if start:
#         a = a
#     else:
#         a = a + 1
#     if end:
#         b = b + 1
#     else:
#         b = b
#     for i in range(a, b):
#         if isOushu(i):
#             result.append(i)
#     return result


# ⑥
# def paixu(iterable, button=False):
#     """对可迭代对象排序，button控制升降序，默认为False升序"""
#     obj = sorted(iterable, key=lambda x: x["grade"], reverse=button)
#     return obj


# ⑦
# def datedefference(date1, date2=None):
#     """计算两个日期的时间差，date1:year-month-day;date2默认为None"""
#     import datetime
#     if date2 is None:
#         date2 = datetime.datetime.now()
#     else:
#         date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
#     date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
#     return date2 - date1


# ⑧
# def datedeff(date1, days):
#     """计算时间差，date1:year-month-day；days：天数"""
#     import datetime
#     date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
#     time_gap = datetime.timedelta(days=days)
#     time_result = date1 - time_gap
#     return time_result.strftime("%Y-%m-%d")


# ⑨
# def daterange(begin_date, end_date):
#     """遍历日期，date1:year-month-day；date2:year-month-day"""
#     import datetime
#     begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
#     end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
#     day = datetime.timedelta(days=1)
#     date_list = []
#     while begin_date <= end_date:
#         date_list.append(begin_date)
#         begin_date = begin_date + day
#     return date_list
# import math
# import numpy as np
# import cv2  # cv2为opencv-contrib-python库，包含了主模块和contrib模块
# import imutils  # imutils是在OPenCV基础上的一个封装，达到更为简结的调用OPenCV接口的目的，它可以轻松的实现图像的平移，旋转，缩放，骨架化等一系列的操作。
#
# # #幂律变换 γ>1
# image = cv2.imread(r'C:\Users\Linting\Desktop\img1.png')  # 读取图片
# gamma_img1 = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.float64)# 返回一个 image.shape[0]*3*image.shape[1]的64位浮点数类型的三维矩阵X（即图片的宽*3*图片的高 单位为px）
# # 遍历矩阵X,进行幂律变换，伽马值γ=5
# for i in range(image.shape[0]):
#     for j in range(image.shape[1]):
#         gamma_img1[i, j, 0] = math.pow(image[i, j, 0], 5)
#         gamma_img1[i, j, 1] = math.pow(image[i, j, 1], 5)
#         gamma_img1[i, j, 2] = math.pow(image[i, j, 2], 5)
# cv2.normalize(gamma_img1, gamma_img1, 0, 255, cv2.NORM_MINMAX)  # 将图片的值放缩到 0-255 之间,采用min_max的方式
# gamma_img1 = cv2.convertScaleAbs(gamma_img1)  # 通过线性变换将数据转回原来的uint8形式（该操作可实现图像增强等相关线性操作的快速运算）,否则将无法显示图像，而只是一副灰色的窗口
# cv2.imshow('image', imutils.resize(image, 400))  # 展示原图
# cv2.imshow('gamma Y>1 transform', imutils.resize(gamma_img1, 400))  # 展示伽马矫正后的图片
# if cv2.waitKey(0) == 27:
#     cv2.destroyAllWindows()
#
# # # 幂律变换，γ<1
# image = cv2.imread(r'C:\Users\Linting\Desktop\city.png')  # 读取图片
# gamma_img2 = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.float64)# 返回一个 image.shape[0]*3*image.shape[1]的64位浮点数类型的三维矩阵X（即图片的宽*3*图片的高 单位为px）
# # 遍历矩阵X,进行幂律变换，伽马值γ=0.4
# for i in range(image.shape[0]):
#     for j in range(image.shape[1]):
#         gamma_img2[i, j, 0] = math.pow(image[i, j, 0], 0.4)
#         gamma_img2[i, j, 1] = math.pow(image[i, j, 1], 0.4)
#         gamma_img2[i, j, 2] = math.pow(image[i, j, 2], 0.4)
# cv2.normalize(gamma_img2, gamma_img2, 0, 255, cv2.NORM_MINMAX)  # 将图片的值放缩到 0-255 之间,采用min_max的方式
# gamma_img2 = cv2.convertScaleAbs(gamma_img2)  # 通过线性变换将数据转回原来的uint8形式（该操作可实现图像增强等相关线性操作的快速运算）,否则将无法显示图像，而只是一副灰色的窗口
# cv2.imshow('image', imutils.resize(image, 400))  # 展示原图
# cv2.imshow('gamma Y<1 transform', imutils.resize(gamma_img2, 400))  # 展示伽马矫正后的图片
# if cv2.waitKey(0) == 27:
#     cv2.destroyAllWindows()
# import cv2
# import numpy as np
# a=[[0,0,1,0,0,0,0],[0,1,1,1,1,1,0],[0,1,1,1,1,1,1],[1,1,1,1,1,1,0],[0,1,1,1,1,1,0],[0,0,0,1,0,0,0]]
# b=[]
# for i in range(len(a)):
#     b.append(np.array(a[i]))
# img=np.array(b)
# img=img.astype('uint8')
# # img=cv2.imread(r'C:\Users\Linting\Desktop\default.jpeg')
# print(img,'\n')
# #创建矩形结构单元
# g=np.array([[1,1,1],[1,1,1],[1,1,1]])
# #形态学处理,开运算
# img_open=cv2.erode(img,g)
# print(img_open,'\n')
# img_open=cv2.dilate(img_open,g)
# print(img_open)

#
# img_hat=img-img_open
# cv2.imshow('img',img)
# #cv2.imshow('erode',edge_dilate)
# cv2.imshow('img_open',img_open)
# cv2.imshow('img_open_',img_hat)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# img_open=cv2.morphologyEx(img,cv2.MORPH_OPEN,g)
import jieba
from wordcloud import WordCloud

a="希望让人自由。风华绝代。一部美国近现代史。失去的才是永恒的。 怪蜀黍和小萝莉不得不说的故事。最美的谎言。最好的宫崎骏，最好的久石让。 拯救一个人，就是拯救整个世界。诺兰给了我们一场无法盗取的梦。爱是一种力量，让我们超越时空感知它的存在。永远都不能忘记你所爱的人。如果再也不能见到你，祝你早安，午安，晚安。每个人都要走一条自己坚定了的路，就算是粉身碎骨。 英俊版憨豆，高情商版谢耳朵。小瓦力，大人生。天籁一般的童声，是最接近上帝的存在。 香港电影史上永不过时的杰作。迪士尼给我们营造的乌托邦就是这样，永远善良勇敢，永远出乎意料。一生所爱。我们一路奋战不是为了改变世界，而是为了不让世界改变我们。比利·怀德满分作品。千万不要记恨你的对手，这样会让你失去理智。平民励志片。 满满温情的高雅喜剧。真正的幸福是来自内心深处。人人心中都有个龙猫，童年就永远不会消失。“不要跟我比惨，我比你更惨”再适合这部电影不过了。死亡不是真的逝去，遗忘才是永恒的消亡。无尽的黑暗。张艺谋最好的电影。童话世界的开端。史诗的终章。Tomorrow is another day.受过伤害的人总是笑得最开心，因为他们不愿意让身边的人承受一样的痛苦。最后那些最无聊的事情，才是最值得怀念的。 对我们国家而言，这样的电影多一部是一部。你不是在为你一个人战斗，你要让千千万万的女性看到女生并不是只能相夫教子。凝视卑弱生命，用电影改变命运。1957年的理想主义。 带着心爱的人在天空飞翔。瑰丽壮观、无人能及的冒险之旅。对敌人的仁慈，就是对自己残忍。骗子大师和执著警探的你追我跑故事。 旷古烁今。你给我翻译翻译，神马叫做TMD的惊喜。对天空的追逐，永不停止。 音乐能化解仇恨。承前启后的史诗篇章。史上最美的探戈。如果生活中有什么使你感到快乐，那就去做吧！不要管别人说什么。那些吻戏，那些青春，都在影院的黑暗里被泪水冲刷得无比清晰。爱情哪怕只有一天。视觉革命。传说的开始。经典之作，历久弥新。当一个死水般的体制内出现一个活跃的变数时，所有的腐臭都站在了光明的对面。优雅的孤独。去除成见，需要勇气。电影的现实意义大过电影本身。动物版《哈姆雷特》。邪恶与平庸蛰伏于同一个母体，在特定的时间互相对峙。人生不能像做菜，把所有的料都准备好了才下锅。爱是一切逻辑和原由。在时间之河里感受溺水之苦。别样人生。尽管有些不切实际的幻想，这部电影依旧是一部感人肺腑的佳作。暗恋的极致。4个臭皮匠顶个诸葛亮，盖·里奇果然不是盖的。美丽无罪。你以为你以为的就是你以为的。用音乐化解仇恨，让歌声串起美好。美利坚精神输出大片No1.自由万岁。奔跑的孩子是天使。绝对意义上的美轮美奂。10年的完美句点。安东尼·霍普金斯的顶级表演。孪生蝙蝠侠大战克隆金刚狼。昔日翩翩少年，今日大腹便便。小清新的故事里注入了大历史的情怀。海豚的微笑，是世界上最高明的伪装。人的命运被自己瞬间的抉择改变。往事如烟，无处祭奠。人生中应该拥有这样的一段豁然开朗。故事的高级讲法。爱情纠缠，男女一致。大时代中的人生，小人物的悲喜。我是一个演员。警察抓小偷，老鼠玩死猫。警恶惩奸，维护世界和平这个任务就交给你了，好吗？不一样的导演，不一样的哈利·波特。最不可能的那个人永远是最可能的。穷尽一生，我们要学会的，不过是彼此拥抱。关于连环杀人悬案的集体回忆。约翰尼·德普的独角戏。梦的勾结。以戏谑来戏谑戏谑。人言可畏。沉醉在电影的情感和视听氛围中无法自拔。《我是山姆》的《美丽人生》。浪漫忧郁的成人童话。每个人心中都有一座断背山。史诗大片的典范。华太师是黄霑，吴镇宇四大才子之一。魔法的密室之门已打开...我们都曾经是一一。死可能是一道门，逝去并不是终结，而是超越，走向下一程。深入内心的恐怖，出人意料的结局。缘分是个连绵词，最美不过一瞬。寂寞没有期限。诺兰就是保证。法式小清新。 人与自然的战争史诗。从没见过那么流氓的温柔，从没见过那么温柔的流氓。那些静得只能听见呼吸的日子里，你明白孤独即生活。一场华丽的意淫。Balalala~~~坏人的好总是比好人的好来得更感人。九年后的重逢是世俗和责任的交叠，没了悸动和青涩，沧桑而温暖。我的平常生活就是他人的幸福。年度最佳date movie。曾经的那段美好会沉淀为一辈子的记忆。相逢只要一瞬间，等待却像是一辈子。两张绝世的脸。 尊敬他人，尊敬你生活的这片土地，明白孤独是人生的常态。少女情怀总是诗。把每天当作最后一天般珍惜度过，积极拥抱生活，就是幸福。有时候幸福需要等一等。 和谐的生活离不开摸头与被摸头。触不到的恋人。任何信念的力量，都无法改变命运。不要给它起名字，起了名字就有感情了。你是我最好的朋友，你是我唯一的朋友 。惠及一生的美丽。无跨度十五年的欢乐与泪水。爱是摈弃傲慢与偏见之后的曙光。好的剧本是，就算你猜到了结局也猜不到全部。抱着梦想而活着的人是幸福的，怀抱梦想而死去的人是不朽的。Mr. I Don't Care其实也有Care的时候。没有一人完全善，也没有一人完全恶。揭露人性的丧尸题材力作。热血沸腾，那个低俗、性感的无耻混蛋又来了。再多各自牛逼的时光，也比不上一起傻逼的岁月。 百看不厌。 无想你时你在闹海。爱并不需要智商 。恐怖分子的“秋菊打官司”。要做就做得狠一点，这样才能活下去。写给影迷，动漫迷和游戏迷的一封情书。优秀的战争片不会美化战场，不会粉饰死亡，不会矮化敌人，不会无视常识，最重要的，不会宣扬战争。他给机器起名“克里斯托弗”，因为这是他初恋的名字。中国家庭的喜怒哀乐忍。时代悲歌。偷情本没有这样美。不得不说，《黑客帝国》系列是商业片与科幻、哲学完美结合的典范。愿我们都不用长大，每一座城堡都能永远存在。真相就在眼前。无怼天怼地，你走后，她与世界为敌。Jared Leto的腿比女人还美！穿越错位的时空，仰望陨落的星辰，你没留下你的名字，我却无法忘记那句“我爱你”。当这个世界闭上双眼，他却敞开了怀抱。老少皆宜，这就是好莱坞动画的魅力。故事的反转与反转，分裂电影的始祖。被上帝抛弃了的上帝之城。像吃了苏打饼一样干脆的电影。荒诞讽刺，千奇百巧，抽丝剥茧，百转千回。英雄泪短，兄弟情长。 动画片的圣经。香港浪漫主义警匪动作片的巅峰之作。是枝裕和的家庭习作。假戏真情，爱欲深海岁月流逝，来日可追。一个针管引发的血案。养狗三日，便会对你终其一生。所谓爱情，就是话唠一路，都不会心生腻烦，彼此嫌弃。天使暂时离开。始于荒诞，止于更荒诞。无这个世界从不善待努力的人，努力了也不一定会成功，但是知道自己在努力，就是活下去的动力。我们组成了家。上帝之城+猜火车+阿甘正传+开心辞典=山寨富翁迪士尼和皮克斯拿错剧本的产物。中国版《两杆大烟枪》。电影诗。爱，是个动词。松鼠才是角儿。骨灰级歌舞片。不要企图在重复中寻找已经失去的爱。感情不分食草或者食肉。黑暗之美。现代科幻电影的开山之作，最伟大导演的最伟大影片。宫崎骏的电影总让人感觉世界是美好的，阳光明媚的。无生活在自己的世界里，也可以让周围的人显得可笑和渺小。用剩余不多的时间，去燃烧整个生命。弱者送给弱者的一刀。爱情没有那么多借口，如果不能圆满，只能说明爱的不够。 人们可以登上月球，却永远无法探索人们内心的宇宙。坚硬的信仰。永远的小人物，伟大的卓别林。无无无邓肯·琼斯继《月球》之后再度奉献出一部精彩绝伦的科幻佳作。幸福是生生不息，却难以触及的远。 永远看不腻的喜剧。黑小鸭速效美白记。对爱的执着，可以超越一切。我们都有权利不与自己的过去和解。人生的N种可能性。人生如此，浮生如斯。谁人言，花彼岸，此生情长意短。谁都是不懂爱的罢了。少见的超越首部的续集，动作片中的经典。无无世界不完美，爱会有奇迹。有一些东西不应该被遗忘。“多么美好的一天！”轰轰轰砰咚，啪哒哒哒轰隆隆，磅~嬉笑怒骂，调风动月。被偷走的岁月，被伤害的生命，被禁锢的灵魂，终将被希望和善意救赎。昆汀同学越来越变态了，比北野武还杜琪峰。一部能引人思考的科幻励志片。每个美丽事物背后都是滴血的现实。小成本大魅力。一个精彩的世界观正在缓缓建立。中国式内在的美国电影。日本的家庭电影已经是世界巅峰了，步履不停是巅峰中的佳作。无做一颗让别人需要你的棋子。无谁说王家卫镜头很晃？传奇，不是每个人都可以拥有。没有了退路，只好飞向自由。无王家卫是一种风格，张国荣是一个代表。爱我就给我看你的播放列表。哗啦啦啦啦，天在下雨，哗啦啦啦啦，云在哭泣……找自己。爱情是一场没有尽头的虚幻追逐。大海啊，不全是水。当爱情跨越年龄的界限，它似乎能变得更久远一点，成为一种责任，一种水到渠成的相濡以沫。 爱上未来的你。 一个单凭体香达到高潮的男人。天使保护事件始末。你要相信，这世上真的有爱存在，不管在什么年纪 来啊，互相伤害啊！无拍掉身上的悲伤，从今天开始重新踏上追梦之旅。最忠于原著的一部。"
b=[]
for i in jieba.lcut(a):
    if len(i)>1:
        b.append(i)

wordcloud = WordCloud(background_color="white",font_path=r'C:\Users\Linting\Desktop\msyh.ttf').generate(" ".join(b))

import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")
plt.show()