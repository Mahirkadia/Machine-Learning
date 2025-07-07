import streamlit as st
import pickle
import numpy as np

# Page config
st.set_page_config(
    page_title="EV Range Predictor",
    page_icon="⚡",
    layout="centered"
)

# Load model
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #00cc88;
        text-align: center;
        margin-bottom: 2rem;
    }
    .range-result {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        font-size: 1.8rem;
        margin: 2rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .input-section {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">⚡ Electric Vehicle Range Predictor</h1>', unsafe_allow_html=True)
st.markdown("### Predict your EV's range with just a few details!")

# Default values for all 36 features
default_features = [1.0, 2020.0, 35000.0, 150.0, 5.0, 1.0, 0.0, 1.0, 0.0, 0.0, 
                   1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0,
                   0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0,
                   0.0, 1.0, 0.0, 0.0, 1.0, 0.0]

# Input section
st.markdown('<div class="input-section">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    model_year = st.selectbox("🗓️ Model Year", 
                             options=list(range(2024, 2009, -1)), 
                             index=4)  # Default 2020
    
    vehicle_make = st.selectbox("🚗 Vehicle Make", 
                               ["TESLA", "NISSAN", "CHEVROLET", "BMW", "AUDI", "FORD", "KIA", "TOYOTA"])

with col2:
    vehicle_type = st.selectbox("🔋 Vehicle Type", 
                               ["Battery Electric Vehicle (BEV)", 
                                "Plug-in Hybrid Electric Vehicle (PHEV)"])
    
    price_range = st.selectbox("💰 Price Range", 
                              ["Under $30K", "$30K-$50K", "$50K-$80K", "Over $80K"])

st.markdown('</div>', unsafe_allow_html=True)

# Map inputs to feature values
features = default_features.copy()
features[1] = model_year

# Vehicle type encoding
if vehicle_type == "Battery Electric Vehicle (BEV)":
    features[5] = 1.0
    features[6] = 0.0
else:
    features[5] = 0.0
    features[6] = 1.0

# Price encoding
price_map = {"Under $30K": 25000, "$30K-$50K": 40000, "$50K-$80K": 65000, "Over $80K": 100000}
features[2] = price_map[price_range]

# Make encoding (simplified)
make_map = {"TESLA": [1,0,0,0,0,0,0,0], "NISSAN": [0,1,0,0,0,0,0,0], 
           "CHEVROLET": [0,0,1,0,0,0,0,0], "BMW": [0,0,0,1,0,0,0,0],
           "AUDI": [0,0,0,0,1,0,0,0], "FORD": [0,0,0,0,0,1,0,0],
           "KIA": [0,0,0,0,0,0,1,0], "TOYOTA": [0,0,0,0,0,0,0,1]}

make_encoding = make_map[vehicle_make]
for i, val in enumerate(make_encoding):
    features[10+i] = val

# Predict button
if st.button("🚀 Predict Range", type="primary", use_container_width=True):
    try:
        features_array = np.array(features).reshape(1, -1)
        predicted_range = model.predict(features_array)[0]
        
        # Display result
        st.markdown(f'''
        <div class="range-result">
            <h3>🔋 Predicted Electric Range</h3>
            <h1>{predicted_range:.0f} miles</h1>
        </div>
        ''', unsafe_allow_html=True)
        
        # Additional info
        if predicted_range > 200:
            st.success("🌟 Excellent range! Perfect for long trips.")
        elif predicted_range > 100:
            st.info("✅ Good range for daily commuting.")
        else:
            st.warning("⚠️ Limited range - best for city driving.")
            
        # Summary
        st.markdown(f"""
        **📊 Your Vehicle Profile:**
        - **Year:** {model_year}
        - **Make:** {vehicle_make}
        - **Type:** {vehicle_type.split('(')[1].replace(')', '')}
        - **Price Range:** {price_range}
        """)
        
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown("💡 **Note:** Predictions based on historical EV data and may vary with actual vehicle specifications.")