import numpy as np
import math as mt
import pandas as pd
import matplotlib.pyplot as plt

# 防止画图中文报错
import matplotlib

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 排列组合可以直接从math库中引用
# 排列即A(k,n)，函数为 mt.perm(n, k=None)，n中选k
# 组合即C(k,n)，函数为 mt.comb(n, k)，n中选k

# 计算 组合-情况数量-概率-奖金-各组别期望-总期望
# 最后以 df 形式返回
def st1():
    # 总的可能数量
    total = mt.comb(24, 12)  # 2704156
    # print(total)

    df0 = pd.DataFrame({'组合': ['合计'],
                        '情况数': [mt.comb(24, 12)]})
    # print(df0)
    # 每种情况
    # ① 三个数不同，乘数6
    df1 = pd.DataFrame({'组合': ['840', '831', '750', '741', '732', '651', '642', '543'],
                        '情况数': [6 * mt.comb(8, 8) * mt.comb(8, 4) * mt.comb(8, 0),
                                   6 * mt.comb(8, 8) * mt.comb(8, 3) * mt.comb(8, 1),
                                   6 * mt.comb(8, 7) * mt.comb(8, 5) * mt.comb(8, 0),
                                   6 * mt.comb(8, 7) * mt.comb(8, 4) * mt.comb(8, 1),
                                   6 * mt.comb(8, 7) * mt.comb(8, 3) * mt.comb(8, 2),
                                   6 * mt.comb(8, 6) * mt.comb(8, 5) * mt.comb(8, 1),
                                   6 * mt.comb(8, 6) * mt.comb(8, 4) * mt.comb(8, 2),
                                   6 * mt.comb(8, 5) * mt.comb(8, 4) * mt.comb(8, 3)]})

    # ② 两个数相同，乘数3
    df2 = pd.DataFrame({'组合': ['822', '660', '633', '552'],
                        '情况数': [3 * mt.comb(8, 8) * mt.comb(8, 2) * mt.comb(8, 2),
                                   3 * mt.comb(8, 6) * mt.comb(8, 6) * mt.comb(8, 0),
                                   3 * mt.comb(8, 6) * mt.comb(8, 3) * mt.comb(8, 3),
                                   3 * mt.comb(8, 5) * mt.comb(8, 5) * mt.comb(8, 2)]})

    # ③ 三个数相同，乘数1
    df3 = pd.DataFrame({'组合': ['444'],
                        '情况数': [1 * mt.comb(8, 4) * mt.comb(8, 4) * mt.comb(8, 4)]})

    # 汇总并计算概率
    df = pd.concat((df0, df1, df2, df3), ignore_index=True)
    df['概率P'] = df['情况数'] / df['情况数'].iloc[0]
    # df.reset_index(drop=True)
    # print(df)

    # 记录中奖金额
    bonus = pd.DataFrame({'组合': ['840', '831', '750', '741', '732', '651', '642',
                                   '822', '660', '633', '552', '444', '543'],
                          '奖金': [50, 10, 20, 2, 2, 1, 1, 10, 20, 1, 1, 1, -5]})
    # 合并两表
    df = pd.merge(df, bonus, how='left', on='组合')

    # 按照情况数升序排列，把合计放在最下面
    df = df.sort_values(by=['情况数'], ascending=True)

    # 计算期望
    df['各组合乘积'] = df['概率P'] * df['奖金']
    # df['总期望E'] = df['各组合期望'].sum()
    total_exp = df['各组合乘积'].sum()
    # 添加总期望到DataFrame
    df.iloc[-1, -1] = total_exp

    # 重置索引index
    df = df.reset_index(drop=True)
    print('各组合乘积 的最后一行为，当前游戏规则下的期望：')
    print(df)
    return df


# 探究 bonus_of_543 和 期望 关系，将以上封装为函数，
# 输入 543奖金金额，返回总期望
def get_moball_game_exp(bonus_of_543):
    # 总的可能数量
    df0 = pd.DataFrame({'组合': ['总数'],
                        '情况数': [mt.comb(24, 12)]})

    # 每种情况
    # ① 三个数不同，乘数6
    df1 = pd.DataFrame({'组合': ['_840', '_831', '_750', '_741', '_732', '_651', '_642', '_543'],
                        '情况数': [6 * mt.comb(8, 8) * mt.comb(8, 4) * mt.comb(8, 0),
                                   6 * mt.comb(8, 8) * mt.comb(8, 3) * mt.comb(8, 1),
                                   6 * mt.comb(8, 7) * mt.comb(8, 5) * mt.comb(8, 0),
                                   6 * mt.comb(8, 7) * mt.comb(8, 4) * mt.comb(8, 1),
                                   6 * mt.comb(8, 7) * mt.comb(8, 3) * mt.comb(8, 2),
                                   6 * mt.comb(8, 6) * mt.comb(8, 5) * mt.comb(8, 1),
                                   6 * mt.comb(8, 6) * mt.comb(8, 4) * mt.comb(8, 2),
                                   6 * mt.comb(8, 5) * mt.comb(8, 4) * mt.comb(8, 3)]})

    # ② 两个数相同，乘数3
    df2 = pd.DataFrame({'组合': ['_822', '_660', '_633', '_552'],
                        '情况数': [3 * mt.comb(8, 8) * mt.comb(8, 2) * mt.comb(8, 2),
                                   3 * mt.comb(8, 6) * mt.comb(8, 6) * mt.comb(8, 0),
                                   3 * mt.comb(8, 6) * mt.comb(8, 3) * mt.comb(8, 3),
                                   3 * mt.comb(8, 5) * mt.comb(8, 5) * mt.comb(8, 2)]})

    # ③ 三个数相同，乘数1
    df3 = pd.DataFrame({'组合': ['_444'],
                        '情况数': [1 * mt.comb(8, 4) * mt.comb(8, 4) * mt.comb(8, 4)]})

    # 汇总并计算概率
    df = pd.concat((df0, df1, df2, df3))
    df['概率P'] = df['情况数'] / df['情况数'].iloc[0]

    # 中奖金额
    bonus = pd.DataFrame({'组合': ['_840', '_831', '_750', '_741', '_732', '_651', '_642', '_543',
                                   '_822', '_660', '_633', '_552', '_444'],
                          '奖金': [50, 10, 20, 2, 2, 1, 1, bonus_of_543, 10, 20, 1, 1, 1]})
    # 合并两表
    df = pd.merge(df, bonus, how='left', on='组合')

    # 按照情况数升序排列，把合计放在最下面
    df = df.sort_values(by=['情况数'], ascending=True)

    # 计算期望
    df['各组合乘积'] = df['概率P'] * df['奖金']
    # df['总期望E'] = df['各组合期望'].sum()
    total_exp = df['各组合乘积'].sum()
    # 添加总期望到DataFrame
    df.iloc[-1, -1] = total_exp

    # 重置索引index
    df = df.reset_index(drop=True)
    # print(df)
    # 返回期望
    return df.iloc[-1, -1]


# 画图函数
def draw(start, end, step):
    lis = np.linspace(start, end, step)
    x = [i for i in lis]
    y = [get_moball_game_exp(j) for j in lis]
    x_y = [(round(k, 3), round(get_moball_game_exp(k), 3)) for k in lis]
    points = [x_y[0], x_y[-1]]

    # 画图
    plt.figure('x轴：组合_543 和 y轴：总期望 的关系')
    plt.plot(x, y, color='olive')
    plt.show()
    print(f'来找找盈亏平衡点吧：'
          f'{[i for i in x_y if -0.2 < i[1] < 0.2]}')

    return x_y, points


# 反推表达式和平衡点
def balance_point(points):
    # 定义两个点
    # 定义两个点
    x1, y1 = points[0]
    x2, y2 = points[1]

    # 计算斜率 k
    k = round((y2 - y1) / (x2 - x1), 3)

    # 计算截距 b
    b = round(y1 - k * x1, 3)

    # 计算当 y=0 时的 x 值
    x_at_y0 = round(-b / k, 3)

    # 打印结果
    print('经过计算：')
    print(f"直线的表达式为：y = {k}x + {b}")
    print(f"当 y=0 时，x 的值为：x = {x_at_y0}")


if __name__ == '__main__':
    # st1()
    # print(f'摸球游戏的平均期望：'
    #       f'{round(get_moball_game_exp(bonus_of_543=-5), 4)}')
    points = draw(-10, 0, 101)[1]

    balance_point(points)

    print('Done~')
