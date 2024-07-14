import moball_class as p


if __name__ == '__main__':
    # 玩家姓名
    player_name = 'tram'
    # 游戏模式，individual-单次式/epochs-批量式，输入错误时兼容为individual-单次式
    play_model = 'epochs'
    # 初始金额
    init_amount = 100
    # 每批次数量
    batches = 6
    # 将以上数据输入给程序，开始游玩~
    player = p.MoBallGame(player_name, play_model,
                          batches=batches,
                          init_amount=init_amount,
                          moball_model=4)
    player.play_()
    # 游戏结束后的画图分析
    player.draw_analyse()
    # 游戏结束后的数据汇总，输出为 csv 格式
    player.info_print()
    print('*' * 15, '游戏结束~', '*' * 15)

