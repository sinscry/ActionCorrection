
if __name__ == '__main__':
    # TODO： 计算右侧幻椅式扭转标准
    sx = 2576
    sy = 1932
    sum = 0

    # TODO: 1.  手肘和膝盖的平均距离
    # x = [965, 640, 720, 500, 286, 640, 640, 482, 480, 1080]
    # y = [663, 640, 391, 261, 176, 447, 360, 384, 247, 1980]
    # r = [29, 11, 16, 16, 13, 15, 24, 9, 12, 35]
    # i=0
    # for i in range(10):
    #     if (sx/x[i]) >= (sy/y[i]):
    #         sum += sy/y[i]*r[i]
    #         print(sy/y[i]*r[i])
    #     else:
    #         sum += sx/x[i]*r[i]
    #         print(sx/x[i]*r[i])
    # sum = str(sum/10)
    # print("右侧幻椅式扭转，手肘和膝盖的平均距离："+sum)  # 66.82

    #  TODO: 2. 手腕和肩膀的距离(没有p4)
    x = [965, 640, 720, 286, 640, 640, 482, 480, 1080]
    y = [663, 640, 391, 176, 447, 360, 384, 247, 1980]
    r = [41, 63, 30, 30, 87, 30, 62, 14, 58]
    for i in range(9):
        if (sx/x[i]) >= (sy/y[i]):
            sum += sy/y[i]*r[i]
            print(sy/y[i]*r[i])
        else:
            sum += sx/x[i]*r[i]
            print(sx/x[i]*r[i])
    sum = str(sum/9)
    print("右侧幻椅式扭转，手腕离肩膀的垂直距离："+sum)  # 176.86