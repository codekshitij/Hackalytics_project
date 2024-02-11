import streamlit as st
import pickle

# Load the trained model
@st.cache(allow_output_mutation=True)
def load_model():
    with open('trained_model.pkl', 'rb') as file:
        return pickle.load(file)  # Load the trained model from trained_model.pkl file

# Function to make predictions
def predict_stress_level(model, input_data):
    predicted_stress_level = model.predict(input_data)
    return predicted_stress_level[0]

# Home page
def home_page():
    gradient_css = """
    <style>
        body {
            background: linear-gradient(135deg, #8e2de2, #4a00e0);
            color: #ffffff;
        }
    </style>
    """

    st.write(gradient_css, unsafe_allow_html=True)
    st.image('app_image.png', use_column_width=True)
    st.button("About Us")
    
    st.title("Welcome to [Team Name]")
    st.write("""
    In today’s fast-paced world, a good night’s sleep is more than a luxury; it’s a cornerstone of health and happiness. [Team Name] is designed to be your companion in the quest for restful nights and energized mornings.

    Our app doesn’t just track your sleep; it transforms it. By harnessing the power of advanced analytics and personalized insights, [Team Name] offers a comprehensive overview of your sleep patterns. Understand the phases of your slumber, identify disturbances, and receive tailored advice to enhance the quality of your rest.
    """)

# Streamlit app
def main():
    home_page()  # Display the homepage content
    
    # Load the trained model
    model = load_model()
    
    # User input form
    st.sidebar.header('User Input')
    snoring_rate = st.sidebar.slider('Snoring Rate', min_value=0.0, max_value=100.0, value=50.0, step=1.0)
    respiration_rate = st.sidebar.slider('Respiration Rate', min_value=0.0, max_value=100.0, value=50.0, step=1.0)
    body_temperature = st.sidebar.slider('Body Temperature', min_value=0.0, max_value=100.0, value=50.0, step=1.0)
    limb_movement = st.sidebar.slider('Limb Movement', min_value=0.0, max_value=100.0, value=50.0, step=1.0)
    blood_oxygen = st.sidebar.slider('Blood Oxygen', min_value=0.0, max_value=100.0, value=50.0, step=1.0)
    rapid_eye_movement = st.sidebar.slider('Rapid Eye Movement', min_value=0.0, max_value=100.0, value=50.0, step=1.0)
    sleeping_hours = st.sidebar.slider('Sleeping Hours', min_value=0.0, max_value=100.0, value=50.0, step=1.0)
    heart_rate = st.sidebar.slider('Heart Rate', min_value=0.0, max_value=100.0, value=50.0, step=1.0)
    
    # Prepare user input for prediction
    input_data = [[snoring_rate, respiration_rate, body_temperature, limb_movement, blood_oxygen, rapid_eye_movement, sleeping_hours, heart_rate]]
    
    # Make prediction
    if st.sidebar.button('Predict'):
        predicted_stress_level = predict_stress_level(model, input_data)
        st.write(f'Predicted Stress Level: {predicted_stress_level}')

if __name__ == '__main__':
    main()
