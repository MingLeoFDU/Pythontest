import pandas as pd
import streamlit as st
import pandas as pt
import requests
from pyecharts.charts import Line
from pyecharts import options as opts
from streamlit_echarts import st_pyecharts
from pyecharts.charts import Bar
from pyecharts.charts import Pie
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    'Cookie': 'RECOMMEND_TIP=true; user_trace_token=20231125101920-b3e43ec5-6d18-429e-9833-ec7179f02632; LGUID=20231125101920-754d1c9e-a760-4159-93ba-a7eb07a35049; _ga=GA1.2.189993909.1700878761; JSESSIONID=ABAACCCABABAABIB6A81002DCE62F76DA880FB3B9C81401; WEBTJ-ID=20240218174831-18dbb9e04b29cf-0beb2b502b9c5b-4c657b58-2073600-18dbb9e04b314f5; privacyPolicyPopup=false; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1708249714; sensorsdata2015session=%7B%7D; index_location_city=%E5%85%A8%E5%9B%BD; _gid=GA1.2.1951634943.1708249716; TG-TRACK-CODE=index_search; __lg_stoken__=481e6733ad98e30a281034315a319b9bf29196ccf9f2913f6119ece68a73b49dc142e50777a51e7da03994543c9f0fdef44864bf9617efd2a85a83aef66f80073f8a79ccc418; X_HTTP_TOKEN=edda805a1d49d4ef603752807194a642c9ae0d038b; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1708258053; LGRID=20240218200733-688f5059-8310-4105-b7d1-e2652d25de1f; _ga_DDLTLJDLHH=GS1.2.1708257309.5.1.1708258053.26.0.0; gate_login_token=v1####c6f20a4c1993acf99f389b5aab23710d4253bfed696db690bed9a8dcc4ed329f; LG_HAS_LOGIN=1; _putrc=DA1EB2389F889E3C123F89F2B170EADC; login=true; hasDeliver=0; unick=%E5%BE%90%E4%BF%8A%E8%B1%AA; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218c04463db36d1-01781f7ffccc1a-4c657b58-2073600-18c04463db583d%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22pc_search_right_jljx_1%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22121.0.0.0%22%7D%2C%22%24device_id%22%3A%2218c04463db36d1-01781f7ffccc1a-4c657b58-2073600-18c04463db583d%22%7D'
}


# 按钮点击事件-数据爬取+保存
def get_job_msg(job):
    fp = open('./job_msg.csv', 'w', encoding='utf-8')
    for page in range(2, 5):
        url = 'https://www.lagou.com/wn/jobs?pn={}&cl=false&fromSearch=true&labelWords=sug&suginput={}&kd={}'.format(
            page, job, job)
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        page_text = response.text
        tree = etree.HTML(page_text)
        div_list = tree.xpath('//*[@id="jobList"]/div[1]/div')
        for div in div_list:
            job_title_area = div.xpath('./div[1]/div[1]/div[1]/a//text()')
            salary_degree = div.xpath('./div[1]/div[1]/div[2]//text()')
            # 岗位名称
            job_title = job_title_area[0]
            # 地区area
            area = job_title_area[1]
            # 薪资
            salary = salary_degree[0]
            # 学历degree
            degree = div.xpath('./div[1]/div[1]//div[@class="p-bom__JlNur"]/text()')[0]
            # 公司名称company_title
            company_title = div.xpath('./div[1]/div[2]/div[1]/a/text()')[0]
            # 公司信息company_msg
            company_msg = div.xpath('./div[1]/div[2]/div[2]/text()')
            if company_msg:
                company_msg = company_msg[0]
            else:
                company_msg = "暂无信息"
            # 公司福利company_welfare
            company_welfare = div.xpath('./div[2]/div[2]/text()')[0]
            # 岗位要求job_require
            job_require = div.xpath('./div[2]/div[1]/span/text()')
            if job_require:
                job_require = job_require[0]
            else:
                job_require = "暂无信息"
            fp.write(
                job_title + '`' + salary + '`' + area + '`' + degree + '`' + company_title + '`' + company_msg + '`' + company_welfare + '`' + job_require + '\n')
    fp.close()
    st.success('数据抓取结束')


# 按钮点击事件-数据展示
def load_show():
    df = pd.read_csv('./job_msg.csv', sep='`',
                     names=['岗位名称', '薪资', '地区', '学历/经验要求', '公司名称', '公司信息', '福利', '岗位要求'],
                     encoding='utf-8')
    return df


if __name__ == '__main__':

    st.sidebar.title('拉勾网岗位信息')
    # 输入要爬取的岗位名称
    job = st.sidebar.text_input('请输入要爬取的岗位名称', key='job')
    isClick_btn1 = st.sidebar.button(label='爬取')
    if isClick_btn1:
        print(job)
        get_job_msg(job)
    # 侧边栏布局

    st.sidebar.text('数据加载+展示:')
    # 数据加载+展示
    isClick_btn2 = st.sidebar.button(label='Show')
    if isClick_btn2:
        df = load_show()
        # 折叠展示数据表格
        with st.expander("岗位信息", expanded=True):
            st.write(df)

    # 侧边栏下拉框
    add_selectbox = st.sidebar.selectbox(
        label="岗位分析:",
        options=('请选择', '不同城市岗位数量&平均薪资', '不同经验的岗位占比', '不同学历的岗位数量')
    )
    # 获取下拉选项
    if add_selectbox == '不同城市岗位数量&平均薪资':
        table = load_show()


        def get_city_name(x):
            return x.split('·')[0].split('[')[1]


        table['city'] = table['地区'].map(get_city_name)
        # 不同城市岗位数量
        city_job_count_s = table.groupby(by='city').size().sort_values(ascending=False)

        # 不同城市平均薪资
        # 求出salary每个元素表示薪资范围的均值:7k-10k
        ret = table['薪资'].str.extract(r'(\d+)k-(\d+)k')
        # 注意：正则返回结果为字符串类型,将其转成数字类型
        ret = ret.astype('int')
        table['mean_sal'] = ret.apply(lambda s: s.mean(), axis=1)
        table['mean_sal'] = table['mean_sal']
        mean_sal_city = table.groupby(by='city')['mean_sal'].mean().sort_values(ascending=False)
        mean_sal_city = mean_sal_city.map(lambda x: format(x, '.2f'))
        # 绘制柱状图
        b = (
            Bar()
            .add_xaxis(city_job_count_s.index.tolist())
            .add_yaxis(
                "岗位数量", city_job_count_s.values.tolist())
            .add_yaxis(
                "平均薪资", mean_sal_city.values.tolist())
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="岗位分析", subtitle="不同城市的岗位数量&平均薪资"
                ),  # 工具栏
                toolbox_opts=opts.ToolboxOpts(),
            )
        )
        st_pyecharts(b)

    if add_selectbox == '不同经验的岗位占比':
        table = load_show()
        # 学历
        table["degree"] = table['学历/经验要求'].str.extract('(.*)/(.*)')[0]
        ret = table.groupby(by='degree').size()
        # 饼图
        cate = ret.index.tolist()
        data = ret.values.tolist()
        pie = (Pie()
               .add('i am bobo', [list(z) for z in zip(cate, data)],
                    radius=["30%", "75%"],  # 设置半径（内外圈半径）
                    rosetype="radius"  # 半径形式的玫瑰型样式（经典）
                    )
               .set_global_opts(title_opts=opts.TitleOpts(title="数据分析", subtitle="经验占比"))
               .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
               )

        st_pyecharts(pie)

    if add_selectbox == '不同学历的岗位数量':
        table = load_show()
        # 学历
        table['degree'] = table['学历/经验要求'].str.extract('(.*)/(.*)')[0]
        ret = table.groupby(by='degree').size()
        # 折线图
        data1 = ret.index.tolist()
        data2 = ret.values.tolist()
        print(data1)
        print(data2)
        line = (Line()
        .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=True),
            xaxis_opts=opts.AxisOpts(type_="category"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        )
        .add_xaxis(xaxis_data=data1)
        .add_yaxis(
            series_name="学历岗位数量折线图",
            y_axis=data2,
            symbol="emptyCircle",
            is_symbol_show=True,
            label_opts=opts.LabelOpts(is_show=False),
        ))
        st_pyecharts(line)
