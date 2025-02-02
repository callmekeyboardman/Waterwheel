import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


# 绘制折线图
# @param x_points x坐标轴值，单维列表
# @param y_points y坐标轴值，多维列表
# @param labels 图例，单维列表
# @param title 标题
# @param x_label x轴标签
# @param y_label y轴标签
def draw_plot(x_points: [], y_points: [], labels: [],
              title: str, x_label: str, y_label: str):
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']

    # 只有一根线
    if len(y_points) == 1:
        plt.plot(x_points, y_points[0], color='orangered', linestyle='-', marker='o', label=labels[0])
        for a, b in zip(x_points, y_points[0]):
            plt.text(a, b, b, ha='center', va='bottom', color='orangered', size='13')
    # 有两根线
    elif len(y_points) == 2:
        plt.plot(x_points, y_points[0], color='orangered', linestyle='-', marker='o', label=labels[0])
        plt.plot(x_points, y_points[1], color='royalblue', linestyle='-', marker='o', label=labels[1])
        # 显示每个数据点的值
        for a, b in zip(x_points, y_points[0]):
            plt.text(a, b, b, ha='center', va='bottom', color='orangered', size='13')
        for a, b in zip(x_points, y_points[1]):
            plt.text(a, b, b, ha='center', va='bottom', color='royalblue', size='13')
    # 更多的折线
    else:
        for i in range(len(y_points)):
            plt.plot(x_points, y_points[i], linestyle='-', marker='o', label=labels[i])
            for a, b in zip(x_points, y_points[i]):
                plt.text(a, b, b, ha='center', va='bottom', size='13')
    # X 轴的值旋转一下，方便展示
    plt.xticks(x_points, rotation=45)
    font_dict = {'family': "SimHei", 'color': 'black', 'size': 20}
    # 设置黑体
    plt.title(title, fontdict=font_dict)
    plt.xlabel(x_label, fontdict=font_dict)
    plt.ylabel(y_label, fontdict=font_dict)
    plt.grid()
    plt.legend()
    plt.show()
