print('2017~2018赛季NBA西部联盟前8名:')
teamList=['休斯顿 火箭','金州 勇士','波特兰 开拓者','犹他 爵士','新奥尔良 鹈鹄','圣安东尼奥 马刺','俄克拉荷马城 雷霆','明尼苏达 森林狼']
for i,t in enumerate(teamList):
    print(t.split()[1],end=""'\t')
    if i%2==1:
        print()

