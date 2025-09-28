# streamlit_app.py starter

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Load dataset
df = pd.read_csv("metadata.csv")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

# Interactive year slider
year_range = st.slider("Select year range", 2019, 2022, (2020, 2021))
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]
st.write(f"Papers in selected years: {len(filtered_df)}")

# Show a sample of the data
st.dataframe(filtered_df.head())

# Publications per year plot
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax)
ax.set_title("Publications per Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# Word cloud
text = " ".join(title for title in filtered_df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
fig_wc, ax_wc = plt.subplots(figsize=(15,7))
ax_wc.imshow(wordcloud, interpolation='bilinear')
ax_wc.axis('off')
st.pyplot(fig_wc)
