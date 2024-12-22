import pandas as pd
import streamlit as st

# write函数操作
st.write('1.write()函数基本操作')
st.write(pd.DataFrame({
    '第一列': [1, 2, 3, 4],
    '第二列': [10, 20, 30, 40]
}))

# 滑块组件
st.write('st.slider()函数')
# slider 参数为滑块自定义名称 返回值为挥动到的数值
num = st.slider('num')
st.write(num, 'squard is ', num * num)

# 文本框操作
st.write('文本框操作')
# 文本框操作 回车结束
st.text_input('your name', key='uname')
st.text_input('your password', key='pwd')
st.write(st.session_state.uname, st.session_state.pwd)

# 多选框checkbox
st.write('多选框操作')
# 点击checkbox后返回True 未点击未false
ex1 = st.checkbox('显示/不显示 表格')
if ex1:
    st.write(pd.DataFrame({
        '第一列': [1, 2, 3, 4],
        '第二列': [10, 20, 30, 40]
    }))
ex2 = st.checkbox('显示/不显示 滑块')
if ex2:
    st.slider('滑块')

# 下拉框操作
option = st.selectbox(
    label='请选择省份信息',
    options=['北京', '上海', '广州', '深圳']
)
st.write('您的选择是', option)

# 侧边栏sidebar
add_selection = st.sidebar.selectbox(
    label='请选择通讯方式',
    options=['微信', 'QQ', '手机', '邮箱']
)
# 获取下拉框选项
st.sidebar.write('下拉框选项:',add_selection)

# 侧边栏滑块
add_slider = st.sidebar.slider(
    label='请选择一个范围的值',
    min_value=0,max_value=100,value=(25,75)
)
# 获取滑块的值
st.sidebar.write('滑块的值:',add_slider)

# 单选按钮
add_radio = st.sidebar.radio(
    label='请选择一个选项',
    options=['选项1', '选项2', '选项3']
)