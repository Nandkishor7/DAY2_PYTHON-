import pandas
import numpy
import matplotlib.pyplot as plt
import streamlit as st

from services.apply_ttest import apply_ttest
from services.apply_chisquare import apply_chisquare

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Komal Statistical Tester')

uploaded_file = st.file_uploader('Upload CSV file', type=['csv'])

if uploaded_file is not None:

    df = pandas.read_csv(uploaded_file)


    columns_names = df.columns.tolist()

    selected_col = st.selectbox

    selected_col = st.selectbox('Select a column', columns_names)

    if pandas.api.types.is_numeric_dtype(df[selected_col]):

        apply_ttest(df[selected_col])

    else:
        
        apply_chisquare(df[selected_col])