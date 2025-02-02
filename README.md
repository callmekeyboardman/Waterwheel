# Waterwheel

水车：一种利用水力发展出来的一种运转机械。

在现代社会，数据信息就是水，互联网是传输水的机械。

该项目就是利用互联网，从网上自动获取所需统计数据，并生成可视化图表。

# 概述

分为以下几个模块：

- application：服务层，存储逻辑脚本
- domain：领域层，核心模块
- infrastructure：基础设施层
    - external：访问外部网站
    - repository：持久仓库层

## 依赖

> python 版本：3.12+
>
> Excel依赖库：xlwt（导出xls文件）、openpyxl（导出xlsx文件）
> 
> http依赖库：requests

可以使用下面的 CMD 命令安装:

> ```shell
> pip install xlwt
> pip install openpyxl
> pip install requests
> ```

# 已有功能

1、CpiService
> 20250202

查询 2021~至今 每个月的 CPI 数据，导出 excel、绘制同比值趋势图表。

1、GoldReserveService
> 20250203

查询 近20年的黄金储备，导出 excel、绘制同比值趋势图表。

如果当年储备数据还未公布（为0），会使用前一年数据代替。
