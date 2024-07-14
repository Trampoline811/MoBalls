import moball_components as mbs
import datetime
import emoji
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta, date, time


class MoBallGame:
    def __init__(self, player_name, play_model, batches=5, init_amount=100,
                 moball_model=5, tempt=False):
        self.play_model = play_model
        self.player_name = player_name
        self.batches = batches
        self.init_amount = init_amount
        self.data = None
        self.__moball_model = moball_model
        self.tempt = tempt

    def illustrate(self):
        colour1 = emoji.emojize(':red_circle:')
        colour2 = emoji.emojize(':yellow_circle:')
        colour3 = emoji.emojize(':blue_circle:')
        print('~' * 8, f'{self.player_name}你好，欢迎体验摸球游戏！', '~' * 8)
        print(f'本游戏池子共有24个球，分别是{colour1}、{colour2}、{colour3}三种颜色，每个颜色8个球。',
              '每次从池子中无放回地抽取12个球，根据抽取的颜色组合数，获取相应的奖金。',
              '例如：某次抽到8个红球4个黄球0个蓝球，组合为840，可得到奖金100元，以此类推。', sep='\n')
        print('-' * 20)
        print('本游戏支持两种游戏方式：',
              '① 独立式(一串)，单次式游戏，每次游戏后询问是否继续游戏，',
              '② 批量式(一把)，批量式游戏，默认一批为6次，每批量结束后询问是否继续游戏，',
              '是的话继续游戏，否则结束游戏并进行金额结算。', sep='\n')
        print('-' * 20)
        print(f'游戏的奖金规则如下：', f'{mbs.rules_().to_string(index=False)}', sep='\n')

    def play_(self):
        emoji_dic = {'红': emoji.emojize(':red_circle:'),
                     '黄': emoji.emojize(':yellow_circle:'),
                     '蓝': emoji.emojize(':blue_circle:')}
        # 玩前声明
        self.illustrate()
        # 确定play_model，默认为individual
        play_model_tup = ('individual', 'epochs')
        self.play_model = self.play_model if self.play_model in play_model_tup else 'individual'
        input('准备好了么，请按任意键开始游戏~' + '\n')
        # 得到玩家信息初始化df
        info = mbs.init_player_info(self.player_name, self.init_amount)
        times, epoch = 0, 0
        while True:
            # 单串模式执行摸球游戏
            if self.play_model == 'individual':
                times += 1
                if self.__moball_model == 6:
                    # 给定一个诱惑字典，可扩展成其他形式
                    times_moballmodel_dic = {
                        1: 1, 2: 2, 3: 3, 4: 4, 5: 4,
                        11: 1, 12: 2, 13: 3, 14: 4, 15: 4,
                        22: 1, 23: 4, 24: 4, 25: 3, 26: 2}
                    # 如果6模式下的次数触发，则诱惑字典启动，否则按照6继续抽
                    if times in times_moballmodel_dic:
                        self.__moball_model = times_moballmodel_dic[times]
                        res, counts, group = mbs.moballs_(self.__moball_model)
                        # 从上面返回的 group 拿到规则对应的奖金
                        bonus = mbs.rules_().loc[mbs.rules_()['Group'] == group, 'Bonus'].values[0]
                        self.__moball_model = 6
                    else:
                        res, counts, group = mbs.moballs_(self.__moball_model)
                        # 从上面返回的 group 拿到规则对应的奖金
                        bonus = mbs.rules_().loc[mbs.rules_()['Group'] == group, 'Bonus'].values[0]

                # 更新玩家信息表
                info = mbs.record_player_info(ori_info=info,
                                              player_name=self.player_name,
                                              round_num=times,
                                              group=group,
                                              bonus=bonus)
                # 显示本次摸球游戏的结果
                print(f'第{times}次摸球游戏结果：' + '\n' + f'{"-".join(res)}' + '\n' + \
                      f'{"，".join([f"{emoji_dic[k]}{v}个" for k, v in counts.items()])}' + '\n' + \
                      f'初始金额{self.init_amount}，组合{group}，奖金为{bonus}，结余{info.iloc[-1, -1]}')
                print('-' * 20)

            # 撸串模式执行游戏
            if self.play_model == 'epochs':
                epoch += 1
                # 诱惑模式
                if self.__moball_model == 6:
                    # 给定一个诱惑字典，可扩展成其他形式
                    epoch_moballmodel_dic = {
                        1: 1, 2: 2, 3: 3, 4: 4, 5: 4,
                        11: 1, 12: 2, 13: 3, 14: 4, 15: 4,
                        22: 1, 23: 4, 24: 4, 25: 3, 26: 2}
                    # 如果6模式下的次数触发，则诱惑字典启动，否则按照6继续抽
                    if epoch in epoch_moballmodel_dic:
                        self.__moball_model = epoch_moballmodel_dic[epoch]
                        # epoch是把数，batch_size是每把的串数，遍历执行摸球函数
                        for batch in range(1, self.batches + 1):
                            res, counts, group = mbs.moballs_(self.__moball_model)
                            # 从上面返回的 group 拿到规则对应的奖金
                            bonus = mbs.rules_().loc[mbs.rules_()['Group'] == group, 'Bonus'].values[0]
                            # 每batch更新玩家信息表
                            info = mbs.record_player_info(ori_info=info,
                                                          player_name=self.player_name,
                                                          round_num=f'{epoch}_{batch}',
                                                          group=group,
                                                          bonus=bonus)
                        self.__moball_model = 6
                    else:
                        # epoch是把数，batch_size是每把的串数，遍历执行摸球函数
                        for batch in range(1, self.batches + 1):
                            res, counts, group = mbs.moballs_(self.__moball_model)
                            # 从上面返回的 group 拿到规则对应的奖金
                            bonus = mbs.rules_().loc[mbs.rules_()['Group'] == group, 'Bonus'].values[0]
                        # 每batch更新玩家信息表
                        info = mbs.record_player_info(ori_info=info,
                                                      player_name=self.player_name,
                                                      round_num=f'{epoch}_{batch}',
                                                      group=group,
                                                      bonus=bonus)

                # 显示本轮摸球游戏的结果
                bonus_sum_perepoch = sum(
                    info.iloc[((epoch - 1) * self.batches + 1):(epoch * self.batches + 1), -2].values)
                print(f'第{epoch}轮摸球游戏结束：' + '\n' + \
                      f'初始金额{self.init_amount}，本轮累计奖金为{bonus_sum_perepoch}，结余{info.iloc[-1, -1]}')
                print('-' * 20)

            # 每次/每轮结束后判断结余是否为正，正继续，否则退出游戏
            if info.iloc[-1, -1] <= 0:
                print('【提示】您的余额不足，系统已停止游戏并为您结算：')
                print(info.to_string(index=False))
                break

            # 询问是否继续游戏
            if input('是否继续游戏（按"y"继续，其他键退出）？') in ['Y', 'y']:
                continue
            else:
                print('为您结算：')
                # 最后输出
                print(info.to_string(index=False))
                break
        self.data = info
        return info

    # 画出结果图，并保存至本地
    def draw_analyse(self):
        if self.data is None:
            # 如果function1的结果尚未计算，则先调用function1
            self.play_()
        # 直接使用function1的结果，即self.data
        # 在这里进行function2的逻辑处理
        print("Analyse is using the result from game.")
        df = self.data
        # 确保'Round'列是数值类型
        # df['Round'] = pd.to_numeric(df['Round'])

        # 创建一个画布和两个子图
        plt.figure('Analyse')

        # 下部大子图 - 折线图
        plt.subplot(2, 1, 2)
        plt.plot(df.index, df['Result'], marker='o')
        # 设置标题
        plt.title('Result over Round')
        # 设置 x 轴的标签
        plt.xlabel('Round')
        # 设置 y 轴的标签
        plt.ylabel('Result')
        plt.grid(True)

        # 上部小子图1 - 条形图
        plt.subplot(2, 2, 1)
        group_counts = df['Group'].iloc[1:].value_counts()
        plt.bar(group_counts.index, group_counts.values, color='gold')

        # 为每个条形块添加数值标签
        for (index, value) in zip(group_counts.index, group_counts.values):
            plt.text(index, value, str(value), ha='center', va='bottom')

        # 设置x轴的刻度位置和标签
        plt.xticks(range(len(group_counts)))  # 设置刻度位置
        # plt.xticklabels(group_counts.index, rotation=45, ha='right')  # 设置标签

        plt.title('Distribution of Groups')
        plt.xlabel('Group')
        plt.ylabel('Frequency')

        # 上部小子图2 - 创建饼图
        plt.subplot(2, 2, 2)
        plt.pie(group_counts.values, labels=group_counts.index, autopct='%1.1f%%', startangle=90)
        plt.title('Distribution of Groups')
        plt.xlabel('Group')

        # 调整子图间距
        plt.tight_layout()

        # 保存图形到本地文件，指定文件名和格式
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime('%m%d_%H%M')
        plt.savefig(rf'./images/{self.player_name}{formatted_datetime}.png', format='png')  # 保存为PNG格式

        # 显示图形
        plt.show()

    # 结果输出到csv
    def info_print(self):
        df = self.data
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime('%m%d_%H%M')
        df.to_csv(rf'./info_print_out/{self.player_name}{formatted_datetime}.csv')


if __name__ == '__main__':
    # 游戏模式
    play_model = 'epochs'  # individual/epochs
    # 玩家姓名
    player_name = 'gt'
    # 初始金额
    init_amount = 100
    # info = play_(play_model, player_name, init_amount=init_amount)
    # draw_analyse(df=info)

    moball_game = MoBallGame(player_name, play_model, init_amount=init_amount,
                             moball_model=6)
    moball_game.play_()
    moball_game.draw_analyse()
    print('-' * 15, 'Done!', '-' * 15)
