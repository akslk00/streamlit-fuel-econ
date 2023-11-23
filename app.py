import streamlit as st


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb



def main():
    df=pd.read_csv('./data/fuel_econ.csv')
    
    if st.checkbox('데이터프레임 보기'):
        st.dataframe(df)

    else:
        st.text('')

    st.text('컬럼을 선택하면 중복 제거한 데이터의 갯수를 보여줍니다.')

    choice=st.selectbox('컬럼 선텍',df.columns)


    count=df[choice].nunique()
    st.text('{}컬럼의 중복 제거한 데이터의 갯수는 {}개 입니다.'.format(choice, count))

    seleced_list=st.multiselect('두개의 컬럼을 선택하세요',df.columns[8:])

    if len(seleced_list) == 2:
        fig=plt.figure()
        plt.scatter(data= df, x=seleced_list[0],y=seleced_list[1])
        plt.title(seleced_list[0]+' VS '+seleced_list[1])
        plt.xlabel(seleced_list[0])
        plt.ylabel(seleced_list[1])
        st.pyplot(fig)

        st.text('상관 계수')

        st.dataframe(df[seleced_list].corr())




if __name__ == '__main__':
    main()