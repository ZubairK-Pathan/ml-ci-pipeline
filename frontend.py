import streamlit as st
import requests


st.set_page_config(page_title="Property Valuation Tool", page_icon="🏢", layout="centered")


st.markdown("""
    <style>
    /* Hide the default Streamlit menu and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Style the primary button to look like a standard web button */
    .stButton>button {
        width: 100%;
        background-color: #0F52BA;
        color: white;
        border-radius: 6px;
        height: 3rem;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #08367B;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)


st.title("Property Valuation Tool")
st.markdown(
    "Enter the property details below to generate an Automated Valuation Model (AVM) estimate based on our deployed machine learning pipeline.")
st.divider()


col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("Property Details")

    bedrooms = st.selectbox("Number of Bedrooms", options=[1, 2, 3, 4, 5, 6], index=2)
    sq_ft = st.number_input("Square Footage", min_value=500, max_value=10000, value=1500, step=100)
    age = st.number_input("Property Age (Years)", min_value=0, max_value=150, value=10, step=1)

    st.markdown("<br>", unsafe_allow_html=True)  # Add a little spacing
    submit = st.button("Calculate Valuation")

with col2:
    st.subheader("Valuation Result")


    if submit:
        with st.spinner("Querying API Container..."):
            try:

                input_data = {"bedrooms": bedrooms, "sq_ft": sq_ft, "age": age}
                response = requests.post("http://localhost:8000/predict", json=input_data)


                if response.status_code == 200:
                    price = response.json()["predicted_price"]
                    st.success("Analysis Complete")
                    st.metric(label="Estimated Market Value", value=f"${price:,.2f}")
                else:
                    st.error(f"API Error: {response.status_code}")
            except Exception as e:
                st.error("Failed to connect to the backend API. Is the Docker container running?")
    else:
        # Default state before clicking
        st.info("Awaiting input parameters. Click calculate to generate a valuation.")