import streamlit as st 
import pandas as pd 
import numpy as np
import base64
import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False) 
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import plot
import altair as alt


st.markdown(
    """
    <style>
    .main {
    background-color: #FFFEF2;
    }
    </style>
    """,
    unsafe_allow_html=True
)

background_color= "#FFFEF2"

siteHeader = st.beta_container()
dataExploration1 = st.beta_container()
dataExploration2=st.beta_container()
dataExploration3=st.beta_container()
dataExploration4=st.beta_container()
dataExploration5=st.beta_container()
dataExploration6=st.beta_container()
dataExploration7=st.beta_container()

with siteHeader:
    st.title('Maya El Gharib')
    st.header('Healthcare Analytics-MSBA 385')
    st.header("Summer 2021")
    st.header("An Overview of World Mental Health and Suicide Rates: A Deeper Look into Lebanon")
    st.header("Presented to Dr. Samar Al Hajj")
    from PIL import Image
    image = Image.open('mental.jpg')
    st.image(image)

with dataExploration1:
    st.header('World Average Age-Standardized Suicide Rates per Region and Gender for 2019')
    st.text('This dataset is found in the Global Health Observatory database at WHO website.')
    
#let us load and read the csv file and visualize it through a dataframe and a vertical segmented bar chart 
    data3=pd.read_csv("Suicide Rates.csv")
    data3.reset_index()
#Renaming the columns to have proper and understandable names
    data3.rename(columns={"FactValueNumeric": "Suicide Rate", "Location": "Country", "ParentLocation": "Region", 'Gender ': "Gender"}, inplace=True)
    #st.write(data3)

#Grouping the dataframe by the Region and Gender columns and calculating the avergae suicide rate per region
    grouped_multiple = data3.groupby(['Region', "Gender"]).agg({'Suicide Rate': ['mean']})
    grouped_multiple.columns = ['Average Suicide Rate']
    grouped_multiple = grouped_multiple.reset_index()
    grouped_multiple["Average Suicide Rate"]= grouped_multiple["Average Suicide Rate"].round(decimals=2)
    #st.write(grouped_multiple)

#Creating a more interactive table
    table3=go.Figure(data=go.Table(
    header=dict(values=list(grouped_multiple.columns), 
        fill_color="#90dea5", 
        align="center"), 
    cells=dict(values= [grouped_multiple["Region"], grouped_multiple["Gender"], grouped_multiple["Average Suicide Rate"]],
        fill_color="#cfe8d5", 
        align="center")))

    table3.update_layout(margin=dict(l=5,r=5,b=10, t=10), paper_bgcolor=background_color)
    if st.checkbox('Show dataframe1'):
        st.write(table3)


#Plotting a vertical segmented bar chart 
    st.subheader("Average Suicide Rates (per 100 000 population) per Region and Gender for the year 2019")
    fig2=px.bar(grouped_multiple, x="Region", y="Average Suicide Rate", color="Gender", range_y=[0, 20])
    fig2.update_layout(xaxis_title="Region", yaxis_title="Average Suicide Rate (per 100 000 population)", margin=dict(l=4,r=4,b=15, t=15), paper_bgcolor=background_color, barmode='group')
    st.write(fig2)
   
#Interpretation 
    st.subheader("Western Pacific ranks first in terms of recording the highest suicide rates for both sexes and females, followed by Europe which records the highest suicidal rate for males across all regions. The region which witnesses the lowest suicidal rates is the Eastern Mediterranean.")
  
#World age-standardized suicide rates (per 100 000 population) for both sexes over the years
#Section2
with dataExploration2: #for both sexes 
    st.header("World Average Age-Standardized Suicide Rates per Region for both sexes from 2000 to 2019")
    st.text("This dataset is found in the Global Health Observatory database at WHO website.")

#Loading the csv file and reading it 
    data4=pd.read_csv("Age-Standardized Suicide Rate.csv")
    data4.reset_index()

#Renaming the columns into proper and understandable names 
    data4.rename(columns={'ParentLocation': 'Region', 'Period':'Year', 'FactValueNumeric': 'Age-Standardized Suicide Rate'}, inplace=True)
    #st.write(data4)  all correct for both sexes 

#Grouping the dataframe by Region   
    grouped_multiple1 = data4.groupby(['Region', "Year"]).agg({'Age-Standardized Suicide Rate': ['mean']})
    grouped_multiple1.columns = ['Average Age-Standardized Suicide Rate']
    grouped_multiple1 = grouped_multiple1.reset_index()
    grouped_multiple1["Average Age-Standardized Suicide Rate"]= grouped_multiple1["Average Age-Standardized Suicide Rate"].round(decimals=2)
    #st.write(grouped_multiple1) all correct for both sexes 

#Creating a more interactive table
    table4=go.Figure(data=go.Table(
    header=dict(values=list(grouped_multiple1.columns), 
        fill_color="#90dea5", 
        align="center"), 
    cells=dict(values= [grouped_multiple1["Region"], grouped_multiple1["Year"], grouped_multiple1["Average Age-Standardized Suicide Rate"]],
        fill_color="#cfe8d5", 
        align="center")))
    
    table4.update_layout(margin=dict(l=5,r=5,b=10, t=10), paper_bgcolor=background_color)
    
    if st.checkbox('Show dataframe2'):
        st.write(table4)

#Plotting a line chart
    st.subheader("World Average Age-Standardized Suicide Rates (per 100 000 population) per Region for both sexes from 2000 to 2019")
    fig1 = px.line(grouped_multiple1, x=grouped_multiple1["Year"], y=grouped_multiple1["Average Age-Standardized Suicide Rate"], color=grouped_multiple1["Region"], range_y=[0,20])
    fig1.update_layout(xaxis_title="Year", yaxis_title="Average Age-Standardized Suicide Rate per (100 000) population", margin=dict(l=4,r=4,b=15, t=15), paper_bgcolor=background_color)
    fig1.update_xaxes(tickvals=[2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018,  2019], tickangle=45)
    st.write(fig1)   #all correct for both sexes 

#Interpretation
    st.subheader('As shown by the line chart, there is a gradual decrease in the age-standardized suicide rates across all regions in the last 2 years.')

#how serious is suicide in lebanon MADE SURE OF THE TABLE 
with dataExploration3: 
    st.header("A deeper look into Lebanon's Suicide Rates")
    st.text("The original dataset is found in the Global Health Observatory database at WHO website.")
#Loading and reading the data  
    data5=pd.read_csv("Age-Standardized Suicide Rate LEB.csv") #age standardized Suicide Rate per 100 000 population for gender 
    data5.rename(columns={"Period": "Year", 'Dim1': "Gender", "FactValueNumeric": "Age-Standardized Suicide Rate"}, inplace=True)
    #st.write(data5)    #all correct 
    
#Creating a more interactive table 
    table5=go.Figure(data=go.Table(
    header=dict(values=list(data5.columns), 
        fill_color="#90dea5", 
        align="center"), 
    cells=dict(values= [data5["Year"], data5["Gender"], data5["Age-Standardized Suicide Rate"]],
        fill_color="#cfe8d5", 
        align="center")))

    table5.update_layout(margin=dict(l=5,r=5,b=10, t=10), paper_bgcolor=background_color)
    
    if st.checkbox('Show dataframe3'):
        st.write(table5)

    #st.write(table5) #all correct 

#Creating a line chart 
    st.subheader("Age-Standardized Suicide Rates (per 100 000 population) in Lebanon per Gender from 2000 to 2019")
    fig1 = px.line(data5, x=data5["Year"], y=data5["Age-Standardized Suicide Rate"], color=data5["Gender"], range_y=[0,5])
    fig1.update_layout(xaxis_title="Year", yaxis_title="Age-Standardized Suicide Rate (per 100 000 population)", margin=dict(l=4,r=4,b=15, t=15), paper_bgcolor=background_color)
    fig1.update_xaxes(tickvals=[2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018,  2019], tickangle=45)
    st.write(fig1) #all correct 

#Interpretation
    st.subheader("As shown by the line chart above, Lebeanon witnessed a sharp decrease in suicide rates between the years 2017 and 2018 for males, females, and both sexes. However, suicide rates took an upward slope beyond the year 2018.")
    st.subheader("It is clear that males have higher suicide rates (x2 or more) as compared to females.")
    st.subheader("According to the WHO, there were close to 800,000 suicide deaths worldwide in 2016 which indicates an annual global age-standardized suicide rate of 10.5 per 100 000 population. Given the previous statistical figures, Lebanon's suicide rates for the stated years were less than the global average. Yet, the suicide phenomenon remains alarming given the increase in suicidal rates in the year 2018 onwards. ")

with dataExploration4:
    st.header('World Mental Health Governance')
    st.text('This dataset is found in the Global Health Observatory database at WHO website.')
#Loading and reading the data
    data1=pd.read_csv('Mental_Health_Governance_Clean.csv')
    #st.write(data1)

#Creating a more interactive and appealing table 
    table1=go.Figure(data=go.Table(
    header=dict(values=list(data1.columns), 
        fill_color="#90dea5", 
        align="center"), 
    cells=dict(values= [data1["Country"], data1["Year"], data1["Government expenditures on mental hospitals as a percentage of total government expenditures on mental health (%)"], data1["Stand-alone law for mental health"], data1["Year the law was enacted (latest revision)"], data1["Stand-alone policy or plan for mental health"], data1["Publication year of the policy or plan (latest revision)"]], 
        fill_color="#cfe8d5", 
        align="center")))

    table1.update_layout(margin=dict(l=5,r=5,b=10, t=10), paper_bgcolor=background_color)
    if st.checkbox('Show dataframe4'):
        st.write(table1)

    st.subheader("Government Expenditure on Mental Hospitals as a percenatge of Total Government Expenditure on Mental Health")

    country_options=data1["Country"].unique().tolist()
    country=st.multiselect("Which country would you like to see?", country_options, default=["Australia"])
    data1=data1[data1["Country"].isin(country)]

#Plotting a bar chart 
    fig1=px.bar(data1, x="Country", y="Government expenditures on mental hospitals as a percentage of total government expenditures on mental health (%)", color="Country", range_y=[0, 30])
    fig1.update_layout(xaxis_title="Country", yaxis_title="Government Expenditure on Mental Hospitals (%)", margin=dict(l=4,r=4,b=15, t=15), paper_bgcolor=background_color)
    st.write(fig1)

with dataExploration5:
    st.header('Human Resources in Mental Health')
    st.text('This dataset is found in the Global Health Observatory database at WHO website.')

#Loading and reading the data 
    data2=pd.read_csv('HR Mental Health.csv')
    #st.write(data2)
    
#Creating a more interactive table 
    table2=go.Figure(data=go.Table(
    header=dict(values=list(data2.columns), 
        fill_color="#90dea5", 
        align="center"), 
    cells=dict(values= [data2["Country"], data2["Year"], data2["Psychiatrists working in mental health sector (per 100 000 population)"], data2["Nurses working in mental health sector (per 100 000 population)"], data2["Social workers working in mental health sector (per 100 000 population)"], data2["Psychologists working in mental health sector (per 100 000 population)"]],
        fill_color="#cfe8d5", 
        align="center")))

    table2.update_layout(margin=dict(l=5,r=5,b=10, t=10), paper_bgcolor=background_color)
    if st.checkbox('Show dataframe5'):
        st.write(table2)


#Plotting a pie chart 
t2=pd.DataFrame(data={"Country": data2["Country"], 'Value': data2["Nurses working in mental health sector (per 100 000 population)"]}, 
                          ).sort_values('Value', ascending=False)

t3=pd.DataFrame(data={"Country": data2["Country"], 'Value': data2["Psychiatrists working in mental health sector (per 100 000 population)"]}, 
                          ).sort_values('Value', ascending=False)


#the top 15 countries with highest nurses
df2 = t2[:15].copy()
#st.write(df2)

#top 15 countries with highest psychiatrists
df3=t3[:15].copy()
#st.write(df3)

#Side by side piecharts 
fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "pie"}]])

st.subheader("The Top 15 Countries with the Highest Number of Nurses vs The Top 15 Countries with the Highest Number of Psychiatrists working in Mental Health Sector (per 100 000 population)")
trace1 = go.Pie(
values=df2["Value"],
labels=df2["Country"],
domain=dict(x=[0, 0.5]),
hoverinfo="label+percent+text+value", title="# of Nurses per 100 000 population")
    
trace2 = go.Pie(
values=df3["Value"],
labels=df3["Country"],
domain=dict(x=[0.5, 1]),
hoverinfo="label+percent+text+value", title="# of Psychiatrists per 100 000 population")
layout = go.Layout(paper_bgcolor=background_color)
data = [trace1, trace2]
fig = go.Figure(data=data, layout=layout)
st.write(fig)

st.header("Where does Lebanon stand in terms of Human Resources in Mental Health?")
st.subheader("For the year 2015, Lebanon had 1.213 psychiatrists and 3.145 nurses working in mental health sector (per 100 000 population). Obviously, Lebanon has a low number of pychiatrists and nurses as compared to the top 15 countries.")

st.header("Conclusion")
st.subheader("To conclude, one might say that although different regions have been witnessing a gradual decrease in suicide rates in recent years, Lebanon's suicide rates have witnessed an increase from the year 2018 onwards, making Suicide and Mental Health phenomena more alarming. Thus, it is highly important to address the topic of Mental Health and emphasize how important it is to look after your own mental health and thus reduce the risks of suicide attempts.")
