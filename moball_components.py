# 一共有24个球，3种颜色，每个颜色的球有8个，红黄蓝
# 每次摸球12个，按照规则算钱
import random
from collections import Counter
import pandas as pd
import numpy as np


# 设定模式，模式1 2 3 4的结果由此输出，并集成在下面moballs_()函数返回
def moball_modelsetted_res(model):
    # 设定游戏模式 model： 1起飞(大金额) 2容易(小金额) 3平局(批次为0) 4地狱(全是负) 5正常抽
    # 设置模式-权重组合字典
    # 1 在大金额组合里面抽，并凑成数据
    # 2 在小金额组合里面抽，并凑成数据
    # 3 依照该概率抽，每batch的期望为0
    # 4 只抽543，扣钱!
    # 5 正常抽
    # 6 诱惑模式
    model_weight_target_combinations_dic = {
        1: ([0.06, 0.32, 0.32, 0.15, 0.15], ['840', '831', '822', '750', '660']),
        2: ([0.1, 0.1, 0.16, 0.16, 0.16, 0.16, 0.16], ['741', '732', '651', '642', '633', '552', '444']),
        3: ([1 / 6] * 6, ['651', '642', '633', '552', '444', '543']),
        4: ([1], ['543'])
    }
    weight, target_combinations = model_weight_target_combinations_dic[model]

    # 从预设的组合中随机选择一个
    target_combination = np.random.choice(target_combinations, p=weight)
    A_num, B_num, C_num = (int(i) for i in target_combination)
    # 根据选择的组合，决定抽取的球
    res_lettet = np.array(['A' + str(num) for num in random.sample(range(1, 9), A_num)] +
                          ['B' + str(num) for num in random.sample(range(1, 9), B_num)] +
                          ['C' + str(num) for num in random.sample(range(1, 9), C_num)])
    # 将字母替换成数字
    # 构造替换字典
    replace_dics = [
        {'A': '红', 'B': '黄', 'C': '蓝'},
        {'A': '红', 'B': '蓝', 'C': '黄'},
        {'A': '黄', 'B': '红', 'C': '蓝'},
        {'A': '黄', 'B': '蓝', 'C': '红'},
        {'A': '蓝', 'B': '红', 'C': '黄'},
        {'A': '蓝', 'B': '黄', 'C': '红'}
    ]
    replace_dic = random.choice(replace_dics)
    # 结果形式转换，将A1转换为红1形式，并打乱顺序输出
    result = np.array([replace_dic[x[0]] + x[1] for x in res_lettet])
    random.shuffle(result)
    return result


# 单次摸球游戏，返回摸球结果、各颜色球频次、颜色组合数据
def moballs_(model):
    group_balls = np.array(['红' + str(i) for i in range(1, 9)] + \
                           ['黄' + str(i) for i in range(1, 9)] + \
                           ['蓝' + str(i) for i in range(1, 9)])  # np形式数据
    if model in [5, 6]:
        res = np.random.choice(group_balls, size=12, replace=False)
    else:
        res = moball_modelsetted_res(model)

    # 计算组合模式
    # 说明 dic遍历适用于已经知道dic结果的情况（闭环），而counter函数适用于不知道结果的情况（开放）
    counts = {
        '红': 0, '黄': 0, '蓝': 0
    }
    for i in res:
        counts[i[0]] = counts.get(i[0], None) + 1
    # counts = Counter([i[0] for i in res])  # 字典 {‘黄’:5, '蓝':4, '红'：3}
    group = ''.join(sorted([str(v) for v in counts.values()], reverse=True))  # 543 660 等

    # 返回摸球结果、各颜色球频次、颜色组合数据
    print(f'摸球模式：{model}')
    return res, counts, group


# 摸球游戏规则
# 注意这里840必须降序排列，否则和上面的输出 group 匹配不上
def rules_():
    rules = pd.DataFrame({'Group': ['840', '831', '822', '750', '660', '741', '732', '651', '642',
                                    '633', '552', '444', '543'],
                          'Bonus': [50, 10, 10, 20, 20, 2, 2, 1, 1, 1, 1, 1, -5]})
    return rules


# 玩家信息初始化
def init_player_info(player_name, init_amount=100):
    data = [[0, player_name, '--', '--', init_amount]]
    info = pd.DataFrame(data, columns=['Round', 'PlayerName', 'Group', 'Bonus', 'Result'])
    return info


# 记录玩家每次游玩信息的函数
def record_player_info(ori_info, player_name, round_num, group, bonus):
    # 将当前轮次的金额和结果添加到DataFrame中
    new_info = {'Round': [round_num],
                'PlayerName': [player_name],
                'Group': [group],
                'Bonus': [bonus],
                'Result': [ori_info.iloc[-1]['Result'] + bonus]
                }
    new_df = pd.DataFrame(new_info, index=[ori_info.index[-1] + 1])
    # 将新的DataFrame添加到原始的DataFrame中
    info = ori_info.append(new_df, ignore_index=True)
    return info


if __name__ == '__main__':
    # random.seed(100)
    model = 3
    # res, counts, group = moballs_(model)
    print(rules_())
    # info = init_player_info(player_name='GT')
    # print(info)
    # info = record_player_info(info, player_name='GT', group='840', round_num=1, bonus=100)  # 注意这里的变化
    # print(info)
    # info = record_player_info(info, player_name='GT', group='444', round_num=2, bonus=1)  # 同样注意这里的变化
    # print(info)
    # bonus = rules_().loc[rules_()['Group'] == group, 'Bonus'].values[0]
    # print(f'结果{res}')
    # print(f'组合{group}', f'奖金{bonus}')
    # deltaamount = rules_().loc[rules_()['Group'] == moballs_()[2], 'Bonus'].values[0]

    # for i in range(10):
    #     res, counts, group = moballs_(model)
    #     bonus = rules_().loc[rules_()['Group'] == group, 'Bonus'].values[0]
    #     print(f'结果{res}')
    #     print(f'组合{group}', f'奖金{bonus}')
    # print('Done!')

    # 测试一下按照模式抽球的结果
    # print(moball_modelsetted_res(model=1))
    print(moballs_(model=6))

    pass
