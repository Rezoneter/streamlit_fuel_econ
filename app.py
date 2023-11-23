import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


def main():
    df = pd.read_csv('./data/fuel_econ.csv')
    print(df)
    st.header('Analyzing Car Data')
    if st.checkbox('Show DataFrame'):
        st.dataframe(df)
    else : 
        pass
    st.text('When select column, show duplicated data count')

    choice = st.selectbox('Select Column', df.columns)

    count = df[choice].nunique()

    st.text('Excepted duplicate data counts of {} column = {}'.format(choice, count))

    selected_list = st.multiselect('Selcet two columns', df.columns[8:], max_selections= 2)
    # set selected count of column 

    if len(selected_list) == 2:
        fig = plt.figure()
        plt.scatter(data = df, x= selected_list[0], y= selected_list[1])
        plt.title(selected_list[0]+' Vs '+selected_list[1])
        plt.xlabel(selected_list[0])
        plt.ylabel(selected_list[1])
        plt.show()
        st.pyplot(fig)

        st.text(f'Correlation coefficient')

        st.dataframe(df[selected_list].corr())
    else:
        pass









if __name__ == '__main__':
    main()