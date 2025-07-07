import streamlit as st
import pickle
import numpy as np

# Page config
st.set_page_config(
    page_title="IPL 2025 Predictor",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    font-size: 3rem;
    color: #FF6B35;
    text-align: center;
    margin-bottom: 2rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}
.metric-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 1rem;
    border-radius: 10px;
    color: white;
    text-align: center;
    margin: 0.5rem 0;
}
.prediction-box {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    color: white;
    font-size: 1.5rem;
    margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)

# Load models
@st.cache_resource
def load_models():
    try:
        bat_model = pickle.load(open('best_rf_bat.pkl', 'rb'))
    except:
        bat_model = None
    try:
        bowl_model = pickle.load(open('best_rf_bowl.pkl', 'rb'))
    except:
        bowl_model = None
    return bat_model, bowl_model

bat_model, bowl_model = load_models()

# Header
st.markdown('<h1 class="main-header">🏏 IPL 2025 Performance Predictor</h1>', unsafe_allow_html=True)

# Sidebar with cool cricket logo
st.sidebar.markdown("""
<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #FF6B35, #F7931E); border-radius: 15px; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
    <div style="font-size: 4rem; margin-bottom: 10px;">🏏</div>
    <h2 style="color: white; margin: 0; font-weight: bold;">IPL 2025</h2>
    <p style="color: #FFE4B5; margin: 5px 0; font-size: 0.9rem;">⚡ Performance Predictor ⚡</p>
</div>
""", unsafe_allow_html=True)

model_type = st.sidebar.selectbox(
    "🎯 Select Prediction Type",
    ["🏏 Batting Performance", "⚡ Bowling Performance"],
    index=0
)

if "Batting" in model_type:
    if bat_model is None:
        st.error("❌ Batting model not found. Please train the model first.")
        st.stop()
    
    st.markdown("### 🏏 Batting Performance Predictor")
    
    # Input section with tabs
    tab1, tab2 = st.tabs(["📊 Player Stats", "📈 Advanced Metrics"])
    
    with tab1:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**🎮 Match Statistics**")
            matches = st.slider('Matches Played', 1, 20, 15)
            innings = st.slider('Innings Batted', 1, 20, 14)
            not_outs = st.slider('Not Outs', 0, 10, 2)
        
        with col2:
            st.markdown("**🏆 Milestones**")
            hundreds = st.slider('Centuries (100s)', 0, 5, 1)
            fifties = st.slider('Half Centuries (50s)', 0, 10, 5)
        
        with col3:
            st.markdown("**💥 Boundary Stats**")
            fours = st.slider('Fours (4s)', 0, 100, 60)
            sixes = st.slider('Sixes (6s)', 0, 50, 25)
    
    with tab2:
        # Display calculated metrics
        avg_per_match = (fours * 4 + sixes * 6) / matches if matches > 0 else 0
        boundary_rate = (fours + sixes) / innings if innings > 0 else 0
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Avg Boundary Runs/Match", f"{avg_per_match:.1f}")
        with col2:
            st.metric("Boundary Rate/Innings", f"{boundary_rate:.1f}")
        with col3:
            st.metric("Strike Rate Indicator", f"{(sixes/fours*100) if fours > 0 else 0:.0f}%")
    
    # Prediction button
    if st.button('🎯 Predict Runs', type='primary', use_container_width=True):
        features = np.array([[matches, innings, not_outs, hundreds, fifties, fours, sixes]])
        prediction = bat_model.predict(features)
        
        st.markdown(f'<div class="prediction-box">🎯 Predicted Runs: {prediction[0]:.0f}</div>', unsafe_allow_html=True)
        
        # Performance category based on IPL averages
        if prediction[0] >= 500:
            st.success("🌟 Elite Performance Expected!")
        elif prediction[0] >= 300:
            st.info("⭐ Good Performance Expected!")
        elif prediction[0] >= 150:
            st.warning("📊 Average Performance Expected!")
        else:
            st.error("📈 Below Average - Room for Improvement!")

else:
    if bowl_model is None:
        st.error("❌ Bowling model not found. Please train the model first.")
        st.stop()
    
    st.markdown("### ⚡ Bowling Performance Predictor")
    
    tab1, tab2 = st.tabs(["📊 Bowling Stats", "📈 Performance Metrics"])
    
    with tab1:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**🎮 Match Statistics**")
            matches = st.slider('Matches Played', 1, 20, 15)
            innings = st.slider('Innings Bowled', 1, 20, 14)
            overs = st.slider('Overs Bowled', 1.0, 80.0, 50.0, 0.1)
        
        with col2:
            st.markdown("**📊 Economy Stats**")
            runs = st.slider('Runs Conceded', 0, 600, 400)
        
        with col3:
            st.markdown("**🏆 Wicket Hauls**")
            four_wickets = st.slider('4 Wicket Hauls', 0, 5, 1)
            five_wickets = st.slider('5 Wicket Hauls', 0, 3, 0)
    
    with tab2:
        economy = runs / overs if overs > 0 else 0
        wicket_rate = (four_wickets + five_wickets) / matches if matches > 0 else 0
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Economy Rate", f"{economy:.2f}")
        with col2:
            st.metric("Wicket Hauls/Match", f"{wicket_rate:.2f}")
        with col3:
            st.metric("Overs/Match", f"{overs/matches:.1f}")
    
    if st.button('⚡ Predict Wickets', type='primary', use_container_width=True):
        features = np.array([[matches, innings, overs, runs, four_wickets, five_wickets]])
        prediction = bowl_model.predict(features)
        
        st.markdown(f'<div class="prediction-box">⚡ Predicted Wickets: {prediction[0]:.0f}</div>', unsafe_allow_html=True)
        
        if prediction[0] >= 20:
            st.success("🌟 Excellent Bowling Performance Expected!")
        elif prediction[0] >= 12:
            st.info("⭐ Good Bowling Performance Expected!")
        elif prediction[0] >= 6:
            st.warning("📊 Average Bowling Performance Expected!")
        else:
            st.error("📈 Below Average - Room for Improvement!")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #666;'>🏏 IPL 2025 Performance Predictor | Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)