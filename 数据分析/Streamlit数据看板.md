## Streamlit

### 简介

#### 什么是streamlit

Streamlit是一个免费的开源框架，用于快速构建和共享漂亮的数据科学Web应用程序。它是一个基于Python的库，专为机器学习工程师设计。数据分析工程师不是网络开发人员，他们对花几周时间学习使用这些框架来构建网络应用程序不感兴趣。相反，他们需要一个更容易学习和使用的工具，只要它可以显示数据并收集分析/建模所需的参数。Streamlit允许您仅用几行代码创建一个外观惊艳的应用程序。

#### 数据科学家为何要使用Streamlit？

Streamlit最大的好处是，您甚至不需要了解Web开发的基础知识就可以开始或创建您的第一个Web应用程序。因此，如果你是一个对数据科学感兴趣的人，你想轻松、快速地部署你的模型，并且只需要几行代码，Streamlit是一个很好的选择。

**优势：**

- 不需要具备前端知识即可应用streamlit。
- 学习成本极低
  - 你不需要花费几天或几个月的时间来创建一个Web应用，你可以在几个小时甚至几分钟内创建一个非常漂亮的机器学习或数据科学应用。
- 它兼容大多数Python库
  - 例如panda、matplotlib、seaborn、plotly、Keras、PyTorch等。

#### 环境安装

```python
pip install streamlit

#测试安装是否正常：
streamlit hello
```

#### 程序运行

```python
streamlit run xxx.py
```

### 具体操作

#### 1.write()函数

可以通过该函数向看板上输出显示指定内容

```python
import pandas as pd
import streamlit as st

st.write("1. write()函数基本操作")
st.write(pd.DataFrame({
    '第一列': [1,2,3,4,5],
    '第二列': [6,7,8,9,10]}
))
```

#### 2.滑块组件slider

"slider"的中文意思是"滑块"。它是一种用户界面元素，通常用于选择一个数值范围或从给定选项中选择一个值。滑块的外观通常是一个可拖动的滑块，用户可以通过移动滑块来选择所需的值。滑块可以在许多应用程序和网页中使用，例如调整音量、选择年龄范围或设置某个参数的值。

```python
import streamlit as st

st.write("st.slider()滑块")
#slider参数为滑块自定义名称，返回值为滑动到的数值
num = st.slider("num")
st.write(num, "squred is", num*num)
```

#### 3.文本框操作text_input

```python
import streamlit as st

st.write("文本框操作")
#文本框输入，回车结束
st.text_input("your name", key="name")
st.text_input("your age", key="age")

# 显示输入的值
st.write(st.session_state.name,st.session_state.age)
```

#### 4.多选框checkbox

```python
import streamlit as st
import pandas as pd
import numpy as np

st.write("checkbox()多选框")
# 点击checkbox后返回True，未点击为False
ex1 = st.checkbox('显示/不显示 表格')
if ex1:
    df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    st.write(df)

ex2 = st.checkbox('显示/不显示 滑块')
if ex2:
    x = st.slider('x')
```

#### 5.下拉框selectbox

```python
import streamlit as st

#返回值为选中的内容信息
option = st.selectbox(
    label='请选择省份信息：',
    options=['河北','山东','河南','吉林']
)

st.write("您选择的是: ", option)
```

#### 6.侧边栏sidebar

```python
import streamlit as st

#侧边栏下拉框
add_selectbox = st.sidebar.selectbox(
    label="通讯方式选项",
    options=('微信','QQ','手机','邮件')
)
#获取下拉选项
st.write("下拉选项: ", add_selectbox)

#侧边栏滑块
add_slider = st.sidebar.slider(
    label="选择一个范围的值",
    min_value=0.0, max_value=100.0, value=(25.0, 75.0)
)
#获取滑块的值
st.write("值的范围: ", add_slider)

```

#### 7.单选按钮radio

```python
import streamlit as st

#columns参数表示列数
left_column, right_column = st.columns(2)
# 左边列设置
with left_column:
    #返回值为选中的选项值
    chosen = st.radio(
        label='电脑品牌',
        options=('苹果','华为','小米')
    )
    st.write(f'你选择的品牌是: {chosen}')
    
# 右边列设置
with right_column:
    # 返回值为选中的选项值
    chosen = st.radio(
        label='手机品牌',
        options=('苹果','华为','小米')
    )
    st.write(f'你选择的品牌是: {chosen}')

```

#### 8.进度条progress

```python
import streamlit as st
import time
st.write("模拟长时间的计算...")

# 创建一个动态显示数据的容器，用于动态显示进度条的进度数值
value = st.empty()
#创建进度条，进度条初始值为0
bar = st.progress(0)
for i in range(100):
    #这是动态显示的数值
    value.text(f'Iteration {i+1}')
    # 更新进度条
    bar.progress(i+1)
    time.sleep(0.1)
st.write('运行结束!')
```

#### 9.文件上传

上传penguins.csv文件,然后选择不同的两个企鹅特征,用散点图观察其分布形式。

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.write('上传penguins.csv文件,然后选择不同的两个企鹅特征,用散点图观察其分布形式。')

#创建文件上传组件，如果上传失败则返回None
upload_file = st.file_uploader(
    label = "上传数据集CSV文件" #自定义文件上传提示信息
)

#判断上传文件是否成功
if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write('显示前5行数据：',df.head(5))
    st.success("上传文件成功！")
else:
    st.stop() # 退出

#制作下拉框，用于选择企鹅的不同特征
x_var = st.selectbox(
    label = "请选择:",
    options = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
)
#制作下拉框，用于选择企鹅的不同特征
y_var = st.selectbox(
    label = "请选择",
    options = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
)


fig, ax = plt.subplots() #返回值：画布、画布子图例
ax = sns.scatterplot(data=df,
                     x=x_var,
                     y=y_var,
                     hue='species'
                     )
plt.xlabel(x_var)
plt.ylabel(y_var)
plt.title('Penguins Scatter Plot')

#显示画布
st.pyplot(fig)
```

#### 10.图例显示

环境安装：

```python
pip install streamlit
pip install streamlit-echarts
```

- 折线图

```python
from pyecharts.charts import Line
from pyecharts import options as opts
from streamlit_echarts import st_pyecharts

# 示例数据
cate = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
data1 = [123, 153, 89, 107, 98, 23]
data2 = [56, 77, 93, 68, 45, 67]
#画图
line = (Line()
       .add_xaxis(cate)
       .add_yaxis('电商渠道', data1,
                  #均值标记线
                  markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]))
       .add_yaxis('门店', data2,
                  markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")])
                 )
       .set_global_opts(title_opts=opts.TitleOpts(title="Line-基本示例", subtitle="我是副标题"))
      )
#渲染到页面中
st_pyecharts(line)
```

- 柱状图

```python
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts

b = (
    Bar()
        .add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
        .add_yaxis(
        "2017-2018 Revenue in (billion $)", [21.2, 20.4, 10.3, 6.08, 4, 2.2]
    ).set_global_opts(
        title_opts=opts.TitleOpts(
            title="Top cloud providers 2018", subtitle="2017-2018 Revenue"
        ),#工具栏
        toolbox_opts=opts.ToolboxOpts(),
    )
)
st_pyecharts(b)
```

- 直方图

`np.histogram`是NumPy库中的一个函数，用于计算给定数据的直方图。

直方图是一种统计图表，用于表示数据的分布情况。它将数据划分为多个离散的区间（称为“bin”），并计算每个区间中数据点的频率。直方图的 x 轴表示数据的取值范围，y 轴表示该取值范围内数据点的数量或频率。

```python
from streamlit_echarts import st_pyecharts
from pyecharts.charts import Bar
from pyecharts import options as opts
import numpy as np
import pandas as pd

s = pd.Series(data=np.random.randint(0,10,size=(50)))

#返回值有两个，分别是频率和区间
y,x = np.histogram(s,bins=5)

x = x.tolist()
y = y.tolist()
x,y
c = (
    Bar()
    .add_xaxis(x)
    .add_yaxis("频数", y,
               category_gap=3, # 设置柱子之间的间距为0
               color='#ff8080')
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-直方图"))
)


st_pyecharts(c)
```

- 散点图

```python
from streamlit_echarts import st_pyecharts
from pyecharts.charts import Scatter
from pyecharts import options as opts
import numpy as np

# 示例数据
x = np.random.randint(0,50,size=(20,)).tolist()
y = np.random.randint(0,50,size=(20,)).tolist()


#sort_控制排序，默认降序；
#label_opts标签显示位置
scatter = (Scatter()
          .add_xaxis(x)
          .add_yaxis('散点图', y)
          .set_global_opts(title_opts=opts.TitleOpts(title="Scatter-基本示例", subtitle="我是副标题"))
         )


st_pyecharts(scatter)
```

- 饼图

```python
from streamlit_echarts import st_pyecharts
from pyecharts.charts import Pie
from pyecharts import options as opts

# 示例数据
cate = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
data = [153, 124, 107, 99, 89, 46]

pie = (Pie()
       .add('i am bobo', [list(z) for z in zip(cate, data)],
            radius=["30%", "75%"], #设置半径（内外圈半径）
            rosetype="radius" #半径形式的玫瑰型样式（经典）
           )
       .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例", subtitle="我是副标题"))
       .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
      )

st_pyecharts(pie)
```

- 漏斗图

```python
from streamlit_echarts import st_pyecharts
from pyecharts.charts import Funnel
from pyecharts import options as opts

# 示例数据
cate = ['访问', '注册', '加入购物车', '提交订单', '付款成功']
data = [30398, 15230, 10045, 8109, 5698]
#要想显示转化率需要手动计算存储到data列表中

#sort_控制排序，默认降序；
#label_opts标签显示位置
funnel = (Funnel()
          .add("用户数", [list(z) for z in zip(cate, data)],
               sort_='ascending',
               label_opts=opts.LabelOpts(position="inside"),
              )
          .set_global_opts(title_opts=opts.TitleOpts(title="Funnel-基本示例", subtitle="我是副标题"))
         )

st_pyecharts(funnel)
```

- 地图

```python
import pandas as pd
import streamlit as st
import numpy as np

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50,50] + [37.76,-122.4],
    columns=['lat', 'lon']
)
#注意：map的数据集中必须要有lat和lon固定列名的两列数据作为经纬度
st.map(map_data)

```

### 布局

#### 1.st.sidebar - 在侧边栏增添交互元素

```python
import streamlit as st

# 方式1：使用对象表示法添加选择框
add_selectbox = st.sidebar.selectbox(
    "您希望如何联系您？",
    ("电子邮件", "家庭电话", "移动电话")
)
# 方式2：使用“with”语法添加单选按钮
with st.sidebar:
    add_radio = st.radio(
        "选择一种运输方式",
        ("标准（5-15天）", "快递（2-5天）")
    )
```

#### 2.st.columns - 并排布局多元素容器

通过调用 st.columns，您可以插入多个多元素容器，并将它们布局为并排的形式。返回的是一个容器对象的列表，每个对象都可以用来添加元素。您可以选择使用“with”语法（更推荐）或者直接在容器对象上调用方法来添加元素。

```python
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
   st.header("一只猫")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("一只狗")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("一只猫头鹰")
   st.image("https://static.streamlit.io/examples/owl.jpg")
```

或者您也可以直接在容器对象上调用方法：

```python
import streamlit as st
import numpy as np

col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("一个宽容器，含有图表")
col1.line_chart(data)

col2.subheader("一个窄容器，含有数据")
col2.write(data)
```

#### 3.st.tabs - 以选项卡形式布局多元素容器

通过调用 st.tabs，您可以插入多个多元素容器作为选项卡。每个选项卡都代表一组相关内容。返回的是一个容器对象的列表，每个对象都可以用来添加元素。与之前一样，您可以选择使用“with”语法或者直接在容器对象上调用方法来添加元素。

需要注意的是，每个选项卡的所有内容都会被一次性发送并渲染在前端。

```python
import streamlit as st

tab1, tab2, tab3 = st.tabs(["猫", "狗", "猫头鹰"])

with tab1:
   st.header("一只猫")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("一只狗")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("一只猫头鹰")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

```

或者您也可以直接在容器对象上调用方法：

```python
import streamlit as st
import numpy as np

tab1, tab2 = st.tabs(["📈 图表", "🗃 数据"])
data = np.random.randn(10, 1)

tab1.subheader("一个带有图表的选项卡")
tab1.line_chart(data)

tab2.subheader("一个带有数据的选项卡")
tab2.write(data)

```

#### 4.st.expander - 可展开/折叠的多元素容器

调用 st.expander，您可以插入一个可展开或折叠的容器，用于包含多个元素。容器的初始状态是折叠的，只显示提供的标签。用户可以点击标签来展开容器，查看其中的内容。

```python
import streamlit as st

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("查看说明"):
    st.write("""
        上面的图表展示了我为您选择的一些数字。
        这些数字是通过真实的骰子摇出来的，所以它们*保证*是随机的。
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg")

```

或者您也可以直接在容器对象上调用方法：

```python
import streamlit as st

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

expander = st.expander("查看说明")
expander.write("""
    上面的图表展示了我为您选择的一些数字。
    这些数字是通过真实的骰子摇出来的，所以它们*保证*是随机的。
""")
expander.image("https://static.streamlit.io/examples/dice.jpg")
```

### 实现案例

url：https://www.lagou.com/wn/jobs?pn=2&cl=false&fromSearch=true&labelWords=sug&suginput=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&kd=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90

```python
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
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Cookie':'index_location_city=%E5%85%A8%E5%9B%BD; X_HTTP_TOKEN=42daf4b72327b2814174117071bf5e71415983ed09; __lg_stoken__=f5d6a338ef01c0b03752a269aef3dac648f09261bee2e5d346978743dbefe928ccd07098b9e8a24856599329ef50480429d5897bbfa2fe1b9a23dd0d0846293896c9d7175922; WEBTJ-ID=20240205143154-18d77f7571f17-003bd9bf635325-1e525637-2073600-18d77f757202249; JSESSIONID=ABAABJAABEBACFD8DBE1126E45048CB6551E23D5F6E8F37; sajssdk_2015_cross_new_user=1; sensorsdata2015session=%7B%7D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218d77f757976e4-09280a12810d6e-1e525637-2073600-18d77f757982776%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22MacOS%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22121.0.0.0%22%7D%2C%22%24device_id%22%3A%2218d77f757976e4-09280a12810d6e-1e525637-2073600-18d77f757982776%22%7D'
}
#按钮点击事件-数据爬取+保存
def get_job_msg():
    fp = open('./job_msg.csv', 'a')
    for page in range(2,5):
        url = 'https://www.lagou.com/wn/jobs?pn={}&cl=false&fromSearch=true&labelWords=sug&suginput=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&kd=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90'.format(page)
        page_text = requests.get(url, headers=headers).text
        tree = etree.HTML(page_text)
        div_list = tree.xpath('//*[@id="jobList"]/div[1]/div')
        for div in div_list:
            job_title_area = div.xpath('./div[1]/div[1]/div[1]/a//text()')
            salary_degree = div.xpath('./div[1]/div[1]/div[2]//text()')
            #岗位名称
            job_title = job_title_area[0]
            # 地区area
            area = job_title_area[1]
            #薪资
            salary = salary_degree[0]
            #学历degree
            degree = div.xpath('./div[1]/div[1]//div[@class="p-bom__JlNur"]/text()')[0]
            #公司名称company_title
            company_title = div.xpath('./div[1]/div[2]/div[1]/a/text()')[0]
            #公司信息company_msg
            company_msg = div.xpath('./div[1]/div[2]/div[2]/text()')
            if company_msg:
                company_msg = company_msg[0]
            else:
                company_msg = "暂无信息"
            #公司福利company_welfare
            company_welfare =  div.xpath('./div[2]/div[2]/text()')[0]
            #岗位要求job_require
            job_require = div.xpath('./div[2]/div[1]/span/text()')
            if job_require:
                job_require = job_require[0]
            else:
                job_require = "暂无信息"
            fp.write(job_title+'#'+salary+'#'+area+'#'+degree+'#'+company_title+'#'+company_msg+'#'+company_welfare+'#'+job_require+'\n')
    fp.close()
    st.write('数据抓取结束')

#按钮点击事件-数据展示
def load_show():
    df = pd.read_csv('./job_msg.csv',sep='#',
                     names=['岗位名称','薪资','地区','学历/经验要求','公司名称','公司信息','福利','岗位要求'])
    return df

if __name__ == '__main__':
    #侧边栏布局
    st.sidebar.text('数据爬取+存储:')
    #数据爬取+保存
    isClick_btn1 = st.sidebar.button(label='开始吧')
    if isClick_btn1:
        get_job_msg()

    st.sidebar.text('数据加载+展示:')
    #数据加载+展示
    isClick_btn2 = st.sidebar.button(label='一键启动')
    if isClick_btn2:
        df = load_show()
        # 折叠展示数据表格
        with st.expander("岗位信息", expanded=True):
            st.write(df)

    #侧边栏下拉框
    add_selectbox = st.sidebar.selectbox(
        label="数据分析:",
        options=('请选择','不同城市岗位数量&平均薪资','不同经验的岗位占比','不同学历的岗位数量')
    )
    #获取下拉选项
    if add_selectbox == '不同城市岗位数量&平均薪资':
        table = load_show()
        def get_city_name(x):
            return x.split('·')[0].split('[')[1]
        table['city'] = table['地区'].map(get_city_name)
        #不同城市岗位数量
        city_job_count_s = table.groupby(by='city').size().sort_values(ascending=False)

        #不同城市平均薪资
        # 求出salary每个元素表示薪资范围的均值:7k-10k
        ret = table['薪资'].str.extract(r'(\d+)k-(\d+)k')
        # 注意：正则返回结果为字符串类型,将其转成数字类型
        ret = ret.astype('int')
        table['mean_sal'] = ret.apply(lambda s:s.mean(), axis=1)
        table['mean_sal'] = table['mean_sal']
        mean_sal_city = table.groupby(by='city')['mean_sal'].mean().sort_values(ascending=False)
        mean_sal_city = mean_sal_city.map(lambda x:format(x,'.2f'))
        #绘制柱状图
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
        #学历
        table["degree"] = table['学历/经验要求'].str.extract('(.*)/(.*)')[0]
        ret = table.groupby(by='degree').size()
        #饼图
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
        st.write('兄弟们，自己玩起来吧！')


```



### 实现案例

```python
import pandas as pd
import numpy as np
import streamlit as st
from pyecharts.charts import Pie,Scatter,Funnel,Page,Line,Bar
from pyecharts import options as opts
from pyecharts.options import TextStyleOpts
from streamlit_echarts import st_pyecharts

# st.set_page_config(layout='wide')

@st.cache_data
def load_data():
    data = pd.read_excel('./data/Phone.xlsx')
    #缺失值处理
    data['年'] = data['订单日期'].dt.year
    data['月'] = data['订单日期'].dt.month
    #数据分箱：
    data['年龄段'] = pd.cut(data['年龄'],bins=[16,30,40,50],labels=['16-30','30-40','40-50'],right=False)
    #手机号脱敏处理
    def func(x):
        return str(x).replace(str(x)[3:7],'****')
    data['手机号'] = data['手机号'].map(func)
    return data


data = load_data() #加载数据
#侧边栏布局年份选择
with st.sidebar:
    # 不同年份
    years = data['年'].unique().tolist()
    #下拉选中的年份值
    select_value = st.selectbox(label='请选择年份',options=years)
    #计算对应年份的总销量和总销售额
    year_data = data.loc[data['年']==select_value]
    #总销售额
    year_total_amount = year_data['销售额'].sum()
    st.markdown('### 总销售额 : '+str(year_total_amount))
    #总销量
    year_total_product = year_data['数量'].sum()
    st.markdown('### 总共销量 : ' + str(year_total_product))
    #总订单数
    year_total_count = year_data.shape[0]
    st.markdown('### 总订单量 : ' + str(year_total_count))

st.subheader('销量相关数据展示')
#月份和销售额
month_data = year_data.groupby(by='月')['数量'].sum()
indexs = month_data.index.tolist()
values = month_data.values.tolist()
#画图
line = (Line()
       .add_xaxis(indexs)
       .add_yaxis('不同月份销量', values)
       .set_global_opts(title_opts=opts.TitleOpts('不同月份销量'))
      )
#渲染到页面中
st_pyecharts(line,height=400)


#不同品牌与销量
good_data = year_data.groupby(by='品牌')['数量'].sum()
indexs = good_data.index.tolist()
values = good_data.values.tolist()
b = (
    Bar()
        .add_xaxis(indexs)
        .add_yaxis(
        "销量:", values
    ).set_global_opts(
        title_opts=opts.TitleOpts(
            title="不同品牌的销量"
        )
    )
)
st_pyecharts(b)

#年龄段和销售额
age_data = year_data.groupby(by='年龄段')['数量'].sum()
indexs = age_data.index.tolist()
values = age_data.values.tolist()
pie = (Pie()
       .add('销量', [list(item) for item in zip(indexs,values)],
            radius=["40%", "60%"], #设置半径（内外圈半径）
            rosetype="radius", #半径形式的玫瑰型样式（经典）
            label_opts=opts.LabelOpts(is_show=False, position="center")
           )
       .set_global_opts(title_opts=opts.TitleOpts(title="不同年龄段销量"))
       .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))

      )
st_pyecharts(pie)
```



