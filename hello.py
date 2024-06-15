import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image


def process_main_page():
    show_main_page()
    df = prepare_df()
    process_side_bar_inputs(df)

def show_main_page():
    st.set_page_config(
        layout="wide",
        initial_sidebar_state="auto",
        page_title="Life satisfation",

        # page_icon=image,

    )
    st.title("Life satisfation")    

def process_side_bar_inputs(df):
    st.sidebar.title('Фильтрация')
    selected1 = st.sidebar.checkbox("Включить фильтр №1")
    filtr_priznak = st.sidebar.selectbox("Признак", tuple(df.columns[1:]))
    bolse_menshe1 = st.sidebar.selectbox("", ('Больше','Меньше'))
    # Number input
    choice = st.sidebar.number_input(f"Choose a number (min = {min(df[filtr_priznak])}, max = {max(df[filtr_priznak])})", min(df[filtr_priznak]), max(df[filtr_priznak]))
    if selected1:
        if str(bolse_menshe1) == 'Больше':
            df1 = df[ df[str(filtr_priznak)] >= choice] 
        else:
            df1 = df[ df[str(filtr_priznak)] < choice]
    else:
        df1 = df
    selected2 = st.sidebar.checkbox("Включить фильтр №2")
    appointment = st.sidebar.slider(f'{filtr_priznak} не меньше', min(df[filtr_priznak]), max(df[filtr_priznak]))
    if selected2:
        df2 = df1[ df1[str(filtr_priznak)] >= appointment]
    else:
        df2 = df1
    text = st.sidebar.text_area("Какая страна имеет самый большой Life satisfation?")
    if text.lower().strip() == 'finland' or text.lower().strip() == 'финляндия':
        st.balloons()
        st.write('Верно, самый высокий уровень жизни в  Финляндии!')
        image = Image.open('fin.jpg')
        st.image(image, caption='Finland', width=400)
    else:
        st.dataframe(df2)

def prepare_df():
    df = pd.read_csv("better-life-index-2024.csv", delimiter=',')
    # убираем пробелы в заголовке
    df = df.rename(columns=lambda x: x.strip())
    return df







# st.dataframe(df)
# # st.text(df.sort_values(by='life_satisfaction', ascending=False).iloc[0][0])
# st.text(f"Страна с самым высоким уровнем жизни - {df.sort_values(by='Life satisfaction', ascending=False).iloc[0][0]}!")
# age = st.sidebar.slider("Возраст", min_value=1, max_value=80, value=20,
#                             step=1)
# if age > 50:
#     st.write('DA')


# json
# st.json(df.to_dict())
# st.metric("KPI", 56, 3)
# static table
# st.table(df)

if __name__ == "__main__":    
    process_main_page()