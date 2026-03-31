import streamlit as st
import requests

# Page config
st.set_page_config(page_title="Home Price Estimator", page_icon="🏡", layout="centered")

# Header
st.markdown("""
<h1 style='text-align: center;'>🏡 Home Price Estimator</h1>
<p style='text-align: center; color: grey;'>
Get a quick estimate of your property's value based on key details.
</p>
""", unsafe_allow_html=True)

st.divider()

# Input section
st.subheader("Property Details")

col1, col2 = st.columns(2)

with col1:
    bedrooms = st.slider("Bedrooms", 1, 10, 3)
    age = st.slider("Property Age (years)", 0, 100, 5)

with col2:
    sq_ft = st.number_input("Total Area (sq ft)", 500, 10000, 1500)

st.divider()

# Button
predict = st.button("Estimate Price")

# Prediction
if predict:
    with st.spinner("Calculating estimate..."):

        input_data = {
            "bedrooms": bedrooms,
            "sq_ft": sq_ft,
            "age": age
        }

        try:
            response = requests.post(
                "http://localhost:8000/predict",
                json=input_data,
                timeout=5
            )

            if response.status_code == 200:
                result = response.json()
                price = result["predicted_price"]

                st.success("Estimated Property Value")
                st.markdown(f"""
                <h2 style='color: #2E8B57;'>${price:,.0f}</h2>
                """, unsafe_allow_html=True)

                st.caption("This is an approximate estimate, not a final valuation.")

            else:
                st.error("Couldn't fetch prediction. Please try again.")

        except requests.exceptions.RequestException:
            st.error("Server not reachable. Is your API running?")