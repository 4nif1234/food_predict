import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

def predict():
    # Load model and preprocessor
    @st.cache_resource
    def load_models():
        model_path = Path("model_deploy\catboost_model.joblib")
        preprocessor_path = Path("model_deploy\preprocessor.joblib")
        return {
            "model": joblib.load(model_path),
            "preprocessor": joblib.load(preprocessor_path)
        }

    models = load_models()

    # Title and intro
    st.title("🚗 Food Delivery Distance Prediction")
    st.markdown("Predict the delivery Distance with using Catboost Model as Machine Learning. Here's the requirement to support them :")
    st.divider()

    # Input Form
    with st.form("prediction_form"):
        st.subheader("📝 Order Details")
    
        col1, col2 = st.columns(2)

        with col1:
            delivery_time = st.number_input(
                "🧭 Delivery Time (min)",
                min_value=1.0,
                max_value=200.0,
                value=5.0,
                step=0.1,
                help="Delivery distance in kilometers"
            )

            weather = st.selectbox(
                "☁️ Weather Condition",
                options=["Clear", "Rainy", "Snowy", "Foggy", "Windy"],
                index=0
            )

            time_of_day = st.selectbox(
                "🧾 Day Time",
                options=["Morning", "Afternoon", "Evening", "Night"],
                index=2
            )

        with col2:
            traffic = st.selectbox(
                "🚦 Traffic Level",
                options=["Low", "Medium", "High"],
                index=1
            )

            vehicle = st.selectbox(
                "🚚 Vehicle Type",
                options=["Bike", "Scooter", "Car"],
                index=0
            )

            prep_time = st.number_input(
                "⏲️ Preparation Time (minutes)",
                min_value=1,
                max_value=120,
                value=15,
                step=1
            )

            experience = st.number_input(
                "👤 Courier Experience (years)",
                min_value=0,
                max_value=20,
                value=3,
                step=1
            )

        submitted_1 = st.form_submit_button("🚴‍♂️ Predict Distance")
    
    # Prediction Logic
    if submitted_1:
        try:
            with st.spinner("Making prediction..."):
                input_data = pd.DataFrame([{
                    "Delivery_Time_min": delivery_time,
                    "Weather": weather,
                    "Traffic_Level": traffic,
                    "Time_of_Day": time_of_day,
                    "Vehicle_Type": vehicle,
                    "Preparation_Time_min": prep_time,
                    "Courier_Experience_yrs": experience
                }])

            # Gunakan preprocessor dan model
            X = models["preprocessor"].transform(input_data)
            prediction = models["model"].predict(X)

            # Output
            st.success("✅ Prediction completed successfully!")

            with st.container():
                st.subheader("Prediction Result")
                col_r1, col_r2 = st.columns(2)

            with col_r1:
                st.metric(
                    label="🎇 Estimated Distance ",
                    value=f"{prediction[0]:.1f} km",
                    help="Predicted time from order acceptance to delivery completion"
                )

            with col_r2:
                total_distance = prediction[0] + prep_time
                st.metric(
                    label="🕰️ Total Distance",
                    value=f"{total_distance:.1f} km",
                    help="Includes preparation and delivery time"
                )

            # Input Summary
            st.divider()
            st.subheader("📋 Input Summary")
            st.dataframe(input_data, use_container_width=True, hide_index=True)

        except  Exception as e:
            st.error("❌ An error occurred during prediction.")
            st.exception(e)