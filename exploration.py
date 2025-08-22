import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def eksplorasi_data():
    st.title("Explore Distance Food Delivery")

    df_food = pd.read_csv('Food_Delivery_Baru.csv')

    st.subheader('1. Average Distance Km with Time of Day based on Vehicle Type')
    df_customer = pd.pivot_table(
        data = df_food,
        index = ['Time_of_Day', 'Vehicle_Type'],
        values = 'Distance_km',
        aggfunc = 'mean'
    ).reset_index().sort_values(by='Distance_km', ascending = False)

    scatter1, scatter2= st.columns([2,1])
    with scatter1:
        fig = px.bar(df_customer, x = 'Time_of_Day', y = 'Distance_km', color = 'Vehicle_Type', text='Distance_km',
                     labels = {'Time_of_Day': 'Time of Day', 'Distance_km' : 'DIstance in Km'},
                     width = 1000, height= 500, barmode='group' 
                    )
        # Biar angkanya kelihatan rapi di atas batang
        fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')

        # Tambah jarak antar group bar (mirip bandPaddingInner di Altair)
        fig.update_layout(bargap=0.2)
        st.write(fig)

    with scatter2:
        st.subheader('\n')
        st.subheader('\n')
        st.subheader('\n')
        st.info('''
        Based on the day, The Morning is the most popular distance with the vehicle type

        is Car for 11 Km. For the lowest day is on Night with the scotter and car for 9.2 Km
        ''')

    #st.subheader('\n')

    st.subheader('2. Average Distance Km with Weather based on Traffic Level')
    df_delivery = pd.pivot_table(
        data = df_food,
        index = ['Weather', 'Traffic_Level'],
        values = 'Distance_km',
        aggfunc = 'mean'
    ).reset_index().sort_values(by='Distance_km', ascending = False)

    weather1, weather2= st.columns([2,1])
    with weather1:
        fig = px.bar(df_delivery, x = 'Weather', y = 'Distance_km', color = 'Traffic_Level', text='Distance_km',
                     labels = {'Weather': 'Weather', 'Distance_km' : 'Distance in Km'},
                     width = 650, height= 500, barmode='group' 
                    )
        # Biar angkanya kelihatan rapi di atas batang
        fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')

        # Tambah jarak antar group bar (mirip bandPaddingInner di Altair)
        fig.update_layout(bargap=0.2)
        st.write(fig)

    with weather2:
        st.subheader('\n')
        st.subheader('\n')
        st.subheader('\n')
        st.info('''
        Based on the weather, the Rainy day is the most distance with the traffic level of high in 12.9 Km.
        
        For the lowest weather is on Foggy for the traffic high in 8.5 Km
        ''')
    
    st.subheader('3. Average Distance Km with Courier_Experience_yrs')
    df_time = pd.pivot_table(
        data = df_food,
        index = 'Courier_Experience_yrs',
        values = 'Distance_km',
        aggfunc = 'mean'
    ).reset_index().sort_values(by = 'Courier_Experience_yrs')

    courier1, courier2= st.columns([2,1])
    with courier1:
        fig = px.bar(df_time, x = 'Courier_Experience_yrs', y = 'Distance_km', text='Distance_km',
                     labels = {'Courier_Experience_yrs': 'Courier Experience Years', 'Distance_km' : 'Distance in Km'},
                     width = 650, height= 500 #, barmode='group' 
                    )
        # Biar angkanya kelihatan rapi di atas batang
        fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')

        # Tambah jarak antar group bar (mirip bandPaddingInner di Altair)
        fig.update_layout(bargap=0.2)
        st.write(fig)

    with courier2:
        st.subheader('\n')
        st.subheader('\n')
        st.subheader('\n')
        st.info('''
        Based on their courier experience, the experience with 6 years is the most distance with 11 Km.
                
        The lowest experience with 4 and 9 years in 9.5 Km.
        ''')