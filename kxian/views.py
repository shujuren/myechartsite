from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from pyecharts import Bar
from pyecharts import Kline
import tushare as ts
from pyecharts import Bar, Line, Grid
from pyecharts import Scatter, EffectScatter, Grid
from pyecharts import Bar, Line, Scatter, EffectScatter, Grid
import random
from pyecharts import HeatMap, Bar, Grid
import pandas as pd

REMOTE_HOST = "https://pyecharts.github.io/assets/js"

def index(request):
    template = loader.get_template('kxian/index.html')
    tu = mybar1_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))

def mybar1_fun():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar: Bar = Bar("x 轴和 y 轴交换")
    bar.add("商家A", attr, v1)
    bar.add("商家B", attr, v2, is_convert=True)
    return bar

def kxian1(request):
    template = loader.get_template('kxian/kxian1.html')
    tu = kxian1_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))

def kxian1_fun():
    from pyecharts import Kline
    api = ts.pro_api('acfe91c33583e4f34c757cfc5360f7e51eefd9f0c259f4204ea4720f')

    # 取000001的前复权行情
    df = ts.pro_bar(pro_api=api, ts_code='000001.SZ', adj='qfq', start_date='20181201', end_date='20181231')
    df = df.sort_index(axis=0)
    df1 = df[['open', 'high', 'open', 'close']]

    v1 = df1.values.tolist()
    kline = Kline("K 线图示例")

    aa = [i for i in df1.index.format()]

    kline.add("日K", aa, v1)
    return kline

def kxian2(request):
    template = loader.get_template('kxian/mypage1.html')
    tu = kxian2_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))

def kxian2_fun():
    from pyecharts import Kline
    api = ts.pro_api('acfe91c33583e4f34c757cfc5360f7e51eefd9f0c259f4204ea4720f')

    # 取000001的前复权行情
    df = ts.pro_bar(pro_api=api, ts_code='000001.SZ', adj='qfq', start_date='20181201', end_date='20181231')
    df = df.sort_index(axis=0)
    df1 = df[['open', 'high', 'open', 'close']]

    v1 = df1.values.tolist()
    kline = Kline("K 线图示例")

    aa = [i for i in df1.index.format()]

    kline.add("日K", aa, v1,is_datazoom_show=True)
    return kline

def kxian3(request):
    template = loader.get_template('kxian/mypage1.html')
    tu = kxian3_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))

def kxian3_fun():
    from pyecharts import Kline
    api = ts.pro_api('acfe91c33583e4f34c757cfc5360f7e51eefd9f0c259f4204ea4720f')

    # 取000001的前复权行情
    df = ts.pro_bar(pro_api=api, ts_code='000001.SZ', adj='qfq', start_date='20181201', end_date='20181231')
    df = df.sort_index(axis=0)
    df1 = df[['open', 'high', 'open', 'close']]

    v1 = df1.values.tolist()
    kline = Kline("K 线图示例")

    aa = [i for i in df1.index.format()]

    kline.add("日K", aa, v1,mark_point=["max"],is_datazoom_show=True)
    return kline

def kxian4(request):
    template = loader.get_template('kxian/mypage1.html')
    tu = kxian4_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))

def kxian4_fun():
    from pyecharts import Kline
    api = ts.pro_api('acfe91c33583e4f34c757cfc5360f7e51eefd9f0c259f4204ea4720f')

    # 取000001的前复权行情
    df = ts.pro_bar(pro_api=api, ts_code='000001.SZ', adj='qfq', start_date='20181201', end_date='20181231')
    df = df.sort_index(axis=0)
    df1 = df[['open', 'high', 'open', 'close']]

    v1 = df1.values.tolist()
    kline = Kline("K 线图示例")

    aa = [i for i in df1.index.format()]

    kline.add("日K", aa, v1,mark_point=["max"],is_datazoom_show=True,datazoom_orient="vertical",)
    return kline

def duotu1(request):
    template = loader.get_template('kxian/mypage1.html')
    tu = duotu1_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))

def duotu1_fun():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图示例", height=720)
    bar.add("商家A", attr, v1, is_stack=True)
    bar.add("商家B", attr, v2, is_stack=True)
    line = Line("折线图示例", title_top="50%")
    attr = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    line.add(
        "最高气温",
        attr,
        [11, 11, 15, 13, 12, 13, 10],
        mark_point=["max", "min"],
        mark_line=["average"],
    )
    line.add(
        "最低气温",
        attr,
        [1, -2, 2, 5, 3, 2, 0],
        mark_point=["max", "min"],
        mark_line=["average"],
        legend_top="50%",
    )

    grid = Grid()
    grid.add(bar, grid_bottom="60%")
    grid.add(line, grid_top="60%")
    return grid

def duotu2(request):
    template = loader.get_template('kxian/mypage1.html')
    tu = duotu2_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))

def duotu2_fun():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图示例", title_pos="65%")
    bar.add("商家A", attr, v1, is_stack=True)
    bar.add("商家B", attr, v2, is_stack=True, legend_pos="80%")
    line = Line("折线图示例")
    attr = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    line.add(
        "最高气温",
        attr,
        [11, 11, 15, 13, 12, 13, 10],
        mark_point=["max", "min"],
        mark_line=["average"],
    )
    line.add(
        "最低气温",
        attr,
        [1, -2, 2, 5, 3, 2, 0],
        mark_point=["max", "min"],
        mark_line=["average"],
        legend_pos="20%",
    )
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    scatter = Scatter("散点图示例", title_top="50%", title_pos="65%")
    scatter.add("scatter", v1, v2, legend_top="50%", legend_pos="80%")
    es = EffectScatter("动态散点图示例", title_top="50%")
    es.add(
        "es",
        [11, 11, 15, 13, 12, 13, 10],
        [1, -2, 2, 5, 3, 2, 0],
        effect_scale=6,
        legend_top="50%",
        legend_pos="20%",
    )

    grid = Grid(height=720, width=1200)
    grid.add(bar, grid_bottom="60%", grid_left="60%")
    grid.add(line, grid_bottom="60%", grid_right="60%")
    grid.add(scatter, grid_top="60%", grid_left="60%")
    grid.add(es, grid_top="60%", grid_right="60%")
    return grid

def duotu3(request):
    template = loader.get_template('kxian/duotu3.html')
    tu = duotu3_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))

def duotu3_fun():
    x_axis = [
        "12a", "1a", "2a", "3a", "4a", "5a", "6a",
        "7a", "8a", "9a", "10a", "11a", "12p", "1p",
        "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p",
        "10p", "11p",
    ]
    y_axis = [
        "Saturday",
        "Friday",
        "Thursday",
        "Wednesday",
        "Tuesday",
        "Monday",
        "Sunday",
    ]
    data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    heatmap = HeatMap("热力图示例")
    heatmap.add(
        "热力图直角坐标系",
        x_axis,
        y_axis,
        data,
        is_visualmap=True,
        visual_top="45%",
        visual_text_color="#000",
        visual_orient="horizontal",
    )
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图示例", title_top="52%")
    bar.add("商家A", attr, v1, is_stack=True)
    bar.add("商家B", attr, v2, is_stack=True, legend_top="50%")

    grid = Grid(height=700)
    grid.add(heatmap, grid_bottom="60%")
    grid.add(bar, grid_top="60%")
    return grid

def duotu4(request):
    template = loader.get_template('kxian/duotu4.html')
    tu = duotu4_fun()
    context = dict(
        myechart=tu.render_embed(),
        host=REMOTE_HOST,
        script_list=tu.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))

def duotu4_fun():
    from pyecharts import Bar, Grid

    title = "Height For Class"
    df = pd.DataFrame(pd.read_csv('mycharts/class.csv', encoding='gbk', header=0))

    df1 = pd.DataFrame(df['Height'])
    df2 = pd.DataFrame(df['Name'])

    dtvalue1 = [i[0] for i in df1.values]

    index1 = [i[0] for i in df2.values.tolist()]

    grid = Grid()

    bar = Bar(title, "Height For Class")
    bar.add('Height', index1, dtvalue1, is_datazoom_show=True, xaxis_interval=0, xaxis_rotate=30)
    grid.add(bar, grid_bottom="25%")
    return grid