import streamlit as st

def project():
    st.title("🐱‍🏍 Food Delivery Distance Prediction System")
    st.markdown("""
    <style>
        .main h1 {
            font-size: 3rem;
            color: #FF6F00;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
    """, unsafe_allow_html=True)

    st.divider()

    # Project description
    st.markdown("""
        ## 🧾 About This Application

        Welcome to the **Food Delivery Distance Prediction System**, the greatest tool to predict how far the distance based on
                
        some of features and the goal that we want to get is to get an optimal distance by determining which one of
                
        them is very potential to increase the distance of food delievry

        ### 🔍 Core Features

        The prediction is based on the following input parameters:

        - 📍 **Delivery Time Min**: The total delivery time in minutes.
        - ☁ **Weather Conditions**: Reflects the current climate such as *Clear*, *Rainy*, *Snowy*, *Foggy*, and *Windy*.
        - 🚦 **Traffic Level**: Represents congestion levels on the road - *Low*, *Medium*, or *High*.
        - 🛵 **Vehicle Type**: Type of vehicle used for delivery - *Bike*, *Scooter*, or *Car*.
        -  🍳 **Preparation Time**: The time required to prepare the food order, measured in minutes.
        - 👨‍✈️ **Courier Experience**: Indicates the delivery agent's years of experience in the field.

        ---

        ## 🎯 Purpose & Benefits

        This system was designed to get some of benefits:

        - 📈 Enhance delivery distance to get a really nearest location on it.
        - 🧠 Empower operations managers to make data-driven decisions.
        - ⏱️ Help reduce the time if the driver get short distance.

        ---

        ## 🛠️ Technology Stack

        - **Streamlit**: Frontend user interface
        - **Pandas**: Data manipulation
        - **plotly express**: Visualization tools
        - **Machine Learning**: Predictive model (integrated separately)
""")