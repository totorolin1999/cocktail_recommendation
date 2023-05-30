import streamlit as st
import pickle
import pandas as pd

def recommand(cocktail, number):
    input_cocktail = cocktail
    number = number + 1
    recommendations = pd.DataFrame(similarity.nlargest(number,input_cocktail)['Chinese_Name'])
    recommendations = recommendations[recommendations['Chinese_Name']!=input_cocktail]
    cocktailList = []
    for index, row in recommendations.iterrows():
        cocktailList.append(row['Chinese_Name'])
    return cocktailList
    

cocktails_dict = pickle.load(open('cocktail_dict.pkl', 'rb'))
cocktails = pd.DataFrame(cocktails_dict)

similarity = pickle.load(open('cocktail_similarity.pkl','rb'))

st.title('調酒推薦系統')

selected_cocktail = st.selectbox('選擇您感興趣的調酒', cocktails['Chinese_Name'].values)

selected_number = st.slider('選擇您希望系統推薦的調酒數量', 1, 15, 5)

if st.button('查看您可能會喜歡的調酒'):
    cocktailList = recommand(selected_cocktail, selected_number)

    for cocktail in cocktailList:
        st.write(cocktail)