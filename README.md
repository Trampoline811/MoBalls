# MoBalls

本项目的灵感来自于B站UP主———— SuperB太 的某期B站视频，选自其中的街头夜市摸球游戏。
见以下视频链接的03:03处：
https://m.bilibili.com/video/BV19w411q7Ph?buvid=XY62E0F690F564E262A6C396BB2EC4F3E5D08&from_spmid=dt.opus-detail.ywh.0&is_story_h5=false&mid=gvp5X%2BNEU0aS70ISbme%2BTw%3D%3D&p=1&plat_id=116&share_from=ugc&share_medium=android&share_plat=android&share_session_id=6e14d4a8-3049-407c-a6f2-1ead776bbe70&share_source=WEIXIN&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1720951186&unique_k=SZK1gjf&up_id=85754245

# 数理知识点
需要掌握的数理知识：期望（Expectation）

期望可以理解为执行某概率游戏一次的平均收益，在本游戏中的计算公式为：
$$
\sum _ { 1 } ^ { i } group _ { i } bonus _ { i }
$$

在视频中发现组合 543 的收益是-10，这也是

摸球游戏规则：
游戏池子共有24个球，分别是🔴、🟡、🔵三种颜色，每个颜色8个球。
每次从池子中无放回地抽取12个球，根据抽取的颜色组合数，获取相应的奖金。
例如：某次抽到8个红球4个黄球0个蓝球，组合为840，可得到奖金100元，以此类推。
--------------------
支持两种游戏方式：
① 单次式游戏(一串)，每次游戏后询问是否继续游戏；
② 批量式游戏(一把)，默认每批(batches)6次，每批量结束后询问是否继续游戏，
是的话继续游戏，否则结束游戏并进行金额结算。
--------------------
游戏的奖金规则如下：
Group  Bonus
  840     50
  831     10
  822     10
  750     20
  660     20
  741      2
  732      2
  651      1
  642      1
  633      1
  552      1
  444      1
  543     -5
--------------------
可修改参数：

1 batches：批量式游戏中一把的次数，数量越大，

2 init_amount：游戏玩家的初始金额

3 moball_model：内置的游戏后门，设置了5种游戏模式，输入整数1到5即可， 1起飞(大金额) 2容易(小金额) 3平局(批次为0) 4地狱(全是负) 5正常抽

4 tempt：诱惑模式(T/F)，可以在主函数中主动调整游戏的结果，实现在指定次的指定受益，如第一次一定为正受益

可探索修改数据：
1 组合Group和奖金Bonus可根据自己的需要进行修改，
  B太视频里是-10，我这里修改为-5了，建议每次修改之后可以在 analyse 中先看看修改后的期望如何。






