# MoBalls

本项目的灵感来自于B站UP主———— SuperB太 的某期B站视频，选自其中的街头夜市摸球游戏。

见以下视频链接的03:03 

https://m.bilibili.com/video/BV19w411q7Ph?buvid=XY62E0F690F564E262A6C396BB2EC4F3E5D08&from_spmid=dt.opus-detail.ywh.0&is_story_h5=false&mid=gvp5X%2BNEU0aS70ISbme%2BTw%3D%3D&p=1&plat_id=116&share_from=ugc&share_medium=android&share_plat=android&share_session_id=6e14d4a8-3049-407c-a6f2-1ead776bbe70&share_source=WEIXIN&share_tag=s_i&spmid=united.player-video-detail.0.0&timestamp=1720951186&unique_k=SZK1gjf&up_id=85754245

## 各代码文件关系
main.py 是主函数，已将所有代码封装好，直接打开填写参数即可开始游玩游戏

moball_class.py 是摸球游戏类，基于对组件的调用完成封装

moball_components.py 是摸球游戏的各组件，在类中对其进行调用

./images 和 ./info_print_out 是运行 main.py 的输出

./images输出当前次游戏的可视化数据：金额走势图、组合分布和频数

./info_print_out 输出 csv 文件，记录每次游戏时的金额数据变动，表头为：

| Round | PlayerName | Group | Bonus | Result |
|-------|------------|-------|-------|--------|

## 数理知识点
需要掌握的数理知识：期望（Expectation）

期望可以理解为执行某概率游戏一次的平均收益，在本游戏中的计算公式为：
$$
\sum _ { 1 } ^ { i } group _ { i } bonus _ { i }
$$


B太视频中组合 543 的收益是-10，这是这个摸球概率游戏的关键所在，类似于木桶的最短板。

由于它的存在，导致整个摸球概率游戏的期望E为 -4.25，反过来可计算得，其他组合受益不变，543的受益大于-1.2时，期望E为正。

## 摸球游戏规则：
游戏池子共有24个球，分别是🔴、🟡、🔵三种颜色，每个颜色8个球。
每次从池子中无放回地抽取12个球，根据抽取的颜色组合数，获取相应的奖金。

例如：某次抽到8个红球4个黄球0个蓝球，组合为840，可得到奖金100元，以此类推。

---
## 摸球游戏方式
支持两种游戏方式：
① 单次式游戏(一串)，每次游戏后询问是否继续游戏；
② 批量式游戏(一把)，默认每批(batches)6次，每批量结束后询问是否继续游戏，
是的话继续游戏，否则结束游戏并进行金额结算。
--------------------
## 游戏的奖金规则如下：
| Group Bonus | Value |
|-------------|-------|
| 840         | 50    |
| 831         | 10    |
| 822         | 10    |
| 750         | 20    |
| 660         | 20    |
| 741         | 2     |
| 732         | 2     |
| 651         | 1     |
| 642         | 1     |
| 633         | 1     |
| 552         | 1     |
| 444         | 1     |
| 543         | -5    |
--------------------
# 游戏可修改参数：
1 batches：批量式游戏中一把的次数，数量越大，

2 init_amount：游戏玩家的初始金额

3 moball_model：内置的游戏后门（1~5），设置了5种游戏模式，输入整数1到5即可。

1起飞(大金额) 2容易(小金额) 3平局(批次为0) 4地狱(全是负) 5正常抽 6 诱惑模式(前期在前3种模式下选择，后期变为模式5)

不同模式下的不同结果：
![](https://github.com/Trampoline811/MoBalls/blob/main/images/gt0714_2205.png "1起飞模式")

![](https://github.com/Trampoline811/MoBalls/blob/main/images/gt0714_2210.png "2洒水模式")

![](https://github.com/Trampoline811/MoBalls/blob/main/images/gt0714_2211.png "3平庸模式")

![](https://github.com/Trampoline811/MoBalls/blob/main/images/gt0714_2216.png "4地狱模式")

![](https://github.com/Trampoline811/MoBalls/blob/main/images/gt0714_2215.png "5正常模式")

![](https://github.com/Trampoline811/MoBalls/blob/main/images/tram0717_1126.png "6诱惑模式")

# 游戏可探索修改数据：
1 组合Group和奖金Bonus可根据自己的需要进行修改，其存放在 组件的rules()函数下，

  B太视频里是-10，我这里修改为-5，

  建议每次修改之后可在 analyse.py 中先看看修改后的期望，期望将会影响整个游戏的走势。







