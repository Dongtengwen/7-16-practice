hero_type=['坦克','战士','刺客','法师','射手','辅助']
tank=['苏烈','刘邦','钟馗','张飞','牛魔']
fighter=['孙悟空','哪吒','杨戬','亚瑟','关羽']
assassin=['庞统','花木兰','荆柯','李白','韩信']
magician=['周瑜','诸葛亮','大乔','貂蝉','张良']
shooter=['后裔','黄忠','狄仁杰','孙尚香','公孙离']
supporter=['明世隐','孙膑','梦琪','太乙真人','蔡文姬']
dict_heroType={'坦克':tank,'战士':fighter,'刺客':assassin,'法师':magician,'射手':shooter,'辅助':supporter}
print('王者荣耀游戏角色:')
for i in hero_type:
    print('===%s===:'%i)
    for j in dict_heroType[i]:
        print('%s\t'%j,end="")
    print()
