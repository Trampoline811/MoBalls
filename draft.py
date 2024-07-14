import pandas as pd
import random


# 测试像字典一样，在DF中取数据
def t0():
    # 创建DataFrame
    data = {'Name': ['Tom', 'Bob', 'John'], 'Age': [4, 5, 6], 'High': [165, 170, 175]}
    df = pd.DataFrame(data)
    print(df)

    # 查找Name为'Tom'的数据的'Age'列的值
    age_tom = df.loc[df['Name'] == 'Tom', 'Age']
    values_bob = df.loc[df['Name'] == 'Bob', ['Age', 'High']].values[0]
    values_ = df.loc[df['Name'] == 'Bob', ['Age', 'High']].values

    value_john0 = df.loc[df['Name'] == 'John', ['Age']]
    value_john1 = df.loc[df['Name'] == 'John', 'Age']
    value_john2 = df.loc[df['Name'] == 'John', 'Age'].values
    value_john3 = df.loc[df['Name'] == 'John', 'Age'].values[0]
    value_john4 = df.loc[df['Name'] == 'John', ['Age']].values[0]
    values0 = df.iloc[-2:, -1].values
    value1 = df.iloc[-2, -1]

    # print(value_john0, type(value_john0))
    # print(value_john1, type(value_john1))
    # print(value_john2, type(value_john2))   # [6] <class 'numpy.ndarray'>
    # print(value_john3, type(value_john3))   # 6 <class 'numpy.int64'>
    # print(value_john4, type(value_john4))   # [6] <class 'numpy.ndarray'>
    print(values0, type(values0))  # [170 175] <class 'numpy.ndarray'>
    print(value1, type(value1))  # 170 <class 'numpy.int64'>
    print(value1 > 0)

    print(df['Age'].value_counts())


# 测试给已有数据df添加数据
def t1():
    def add_student(df, student_data):
        """
        将一个学生的数据作为新行添加到DataFrame中。

        参数:
        df (pd.DataFrame): 要添加数据的DataFrame。
        student_data (dict): 包含学生信息的字典，键是列名，值是包含单个学生数据的列表。

        返回:
        pd.DataFrame: 添加了新数据后的DataFrame。
        """
        # 将学生数据转换为DataFrame
        new_df = pd.DataFrame(student_data)
        # 将新的DataFrame添加到原始的DataFrame中，并重置索引
        df = df.append(new_df, ignore_index=True)
        return df

    # 原始DataFrame
    data = {'Name': ['Tom'], 'Age': [4], 'High': [165]}
    df = pd.DataFrame(data)
    print(df)

    # 使用函数添加学生数据
    df = add_student(df, {'Name': ['Bob'], 'Age': [5], 'High': [170]})
    df = add_student(df, {'Name': ['Alice'], 'Age': [6], 'High': [160]})

    # 显示更新后的DataFrame
    print(df)


def t2():
    new_info = {'Round': [3],
                'PlayerName': ['GT'],
                'Group': [840],
                'Bonus': [100],
                'Result': [100 + 100]}
    new_df = pd.DataFrame(new_info)
    print(new_df)


# 报错IndexError: index 0 is out of bounds for axis 0 with size 0
# 逐个对rules的数据进行测试
def t3(group):
    def rules_():
        rules = pd.DataFrame({'Group': ['840', '831', '750', '741', '732', '651', '642', '543',
                                        '822', '660', '633', '552', '444'],
                              'Bonus': [100, 10, 20, 2, 2, 1, 1, -5, 10, 20, 1, 1, 1]})
        return rules

    bonus = rules_().loc[rules_()['Group'] == group, 'Bonus'].values[0]
    print(bonus)


# 测试游戏的4个模式，实现后门实现1
def t4():
    import random

    # 定义球的颜色和数量
    colors = ['Red', 'Yellow', 'Blue']
    balls = {color: 8 for color in colors}

    # 定义不同模式下的返回值
    patterns = {
        'mode1': [840, 831, 750, 822, 660],
        'mode2': [741, 732, 651, 642, 633, 552, 444],
        'mode3': [543],
        'mode4': None  # 正常模式，不控制结果
    }

    # 抽取球的函数
    def draw_balls(total_balls=24, drawn_balls=12):
        # 随机抽取球，无放回
        drawn = random.sample(range(total_balls), drawn_balls)
        return drawn

    # 计算组合的函数
    def calculate_combination(drawn_balls):
        counts = {color: sum(1 for ball in drawn_balls if ball < balls[color] * 3) for color in colors}
        # 计算组合，例如：840表示8个红球，4个黄球，0个蓝球
        combination = counts['Red'] * 100 + counts['Yellow'] * 10 + counts['Blue']
        return combination

    # 游戏模式控制
    def game_mode(mode):
        while True:
            if mode in patterns and patterns[mode]:  # 检查是否有预设的模式组合
                yield patterns[mode].pop(0)  # 返回下一个组合
                if not patterns[mode]:  # 如果该模式的组合已经用完，则重新填充
                    patterns[mode].extend(patterns[mode])  # 这里假设我们想要无限重复模式组合
            else:
                # 正常模式，随机抽取
                drawn_balls = draw_balls()
                combination = calculate_combination(drawn_balls)
                yield combination

    # 示例：启动游戏，模式1
    mode = 'mode1'
    game = game_mode(mode)

    for _ in range(10):  # 模拟抽取10次
        print(next(game))


# 测试游戏的4个模式，实现后门实现2
def t5():
    import random

    # 定义球的颜色
    colors = ['Red', 'Yellow', 'Blue']

    # 预设的组合模式1
    predefined_combinations_mode1 = [
        {'Red': 8, 'Yellow': 4, 'Blue': 0},
        {'Red': 8, 'Yellow': 3, 'Blue': 1},
        {'Red': 7, 'Yellow': 5, 'Blue': 0},
        {'Red': 8, 'Yellow': 2, 'Blue': 2},
        {'Red': 6, 'Yellow': 6, 'Blue': 0}
    ]

    # 抽取球的函数，无放回抽样
    def draw_balls(combination):
        balls = []
        for color, count in combination.items():
            balls.extend([color] * count)
        return balls

    # 游戏模式控制
    def game_mode(mode):
        if mode == 1:
            # 模式1：返回预设的组合
            combination = random.choice(predefined_combinations_mode1)
            return draw_balls(combination)
        else:
            # 其他模式或正常模式：随机抽取
            # 随机选择12个球
            balls = random.sample(range(24), 12)
            # 计算每种颜色的球数
            combination = {color: sum(1 for ball in balls if ball < 8) for color in colors}
            return draw_balls(combination)

    # 示例：启动游戏，模式1
    mode = 1
    drawn_balls = game_mode(mode)
    print(drawn_balls, len(drawn_balls))  # 这将打印模式1下预设的组合之一

    # 示例：启动游戏，正常模式
    mode = 4
    drawn_balls = game_mode(mode)
    print(drawn_balls, len(drawn_balls))  # 这将打印随机抽取的12个球的组合


# 测试游戏的4个模式，实现后门实现3
def t6():
    import random

    def draw_balls():
        balls = ['红'] * 8 + ['黄'] * 8 + ['蓝'] * 8
        random.shuffle(balls)
        return balls[:12]

    def calculate_combination(drawn_balls):
        red_count = drawn_balls.count('红')
        yellow_count = drawn_balls.count('黄')
        blue_count = drawn_balls.count('蓝')
        return red_count * 100 + yellow_count * 10 + blue_count

    def play_game(target_combinations):
        while True:
            drawn_balls = draw_balls()
            combination = calculate_combination(drawn_balls)
            if combination in target_combinations:
                return combination

    target_combinations = [840, 831, 750, 822, 660]
    for i in range(8):
        result = play_game(target_combinations)
        print("抽到的组合为：", result)


def t7():
    import numpy as np
    from collections import Counter

    # 摸球游戏
    # 设定游戏模式 model：1起飞(大金额) 2容易(小金额) 3平局(批次为0) 4地狱(全是负) 5正常抽
    def moballs(model, weight):
        group_balls = ['红' + str(i) for i in range(1, 9)] + \
                      ['黄' + str(i) for i in range(1, 9)] + \
                      ['蓝' + str(i) for i in range(1, 9)]
        group_balls = np.array(group_balls)  # 转换为numpy数组

        # 使用模式1抽取
        if model == 1:
            # 预设的组合模式1
            target_combinations = ['840', '831', '750', '822', '660']
            # 从预设的组合中随机选择一个
            target_combination = np.random.choice(target_combinations)
            A_num, B_num, C_num = int(target_combination[0]), int(target_combination[1]), int(target_combination[2])
            # 根据选择的组合，决定抽取的球
            res = np.array(['A' + str(num) for num in random.sample(range(1, 9), A_num)] +
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
            replace_dics = random.choice(replace_dics)
            # 构建新的序列
            new_sequence = []
            for item in res:
                letter = item[0]
                color = replace_dics.get(letter)  # 如果字母没有颜色，则随机选择
                new_sequence.append(color + item[1:])

        # 计算组合模式
        counts = Counter([i[0] for i in new_sequence])  # 字典 {'黄': 5, '蓝': 4, '红': 3}
        group = ''.join(sorted([str(v) for v in counts.values()], reverse=True))

        return res, counts, group

    # 假设 weight 是一个表示抽取概率的数组或列表
    weight = [1 / 24.0] * 24  # 简化为每个球被抽到的概率相同

    # 调用函数，传入模式1
    res, counts, group = moballs(1, weight)
    print("抽取结果:", res)
    print("球的数量:", counts)
    print("组合:", group)


def t8():
    import random

    # 原始序列
    sequence = ['A6', 'A1', 'A7', 'A2', 'A8', 'A3', 'A4', 'A5', 'B8', 'B2', 'C3', 'C5']

    # 定义颜色列表
    colors = ['红', '黄', '蓝']

    def replace_with_unique_colors(sequence):
        new_sequence = []
        used_colors = {}

        # 随机分配颜色给每个字母，并确保整个序列中颜色不重复
        for item in sequence:
            letter = item[0]
            number = item[1:]
            if letter not in used_colors:
                # 如果字母还没有分配颜色，随机选择一个未被使用的颜色
                available_colors = colors.copy()
                while available_colors:
                    color = random.choice(available_colors)
                    if color not in used_colors.values():
                        used_colors[letter] = color
                        break
                    available_colors.remove(color)

        # 构建新的序列
        for item in sequence:
            letter = item[0]
            color = used_colors.get(letter, random.choice(colors))  # 如果字母没有颜色，则随机选择
            new_sequence.append(color + item[1:])

        return new_sequence

    # 执行替换并打印结果
    for i in range(10):
        new_sequence = replace_with_unique_colors(sequence)
        print(new_sequence)


if __name__ == '__main__':
    t7()
