import streamlit as st

# WHO Standard Ranges for vitals
WHO_RANGES = {
    "Glucose": {"range": (70, 100), "unit": "mg/dL"},
    "SpO2": {"range": (95, 100), "unit": "%"},
    "Blood Pressure (Systolic)": {"range": (90, 120), "unit": "mmHg"},
    "Blood Pressure (Diastolic)": {"range": (60, 80), "unit": "mmHg"},
    "Weight (BMI)": {"range": (18.5, 24.9), "unit": "kg/m²"},
    "Temperature": {"range": (36.5, 37.5), "unit": "°C"},
    "ECG (Heart Rate)": {"range": (60, 100), "unit": "BPM"},
    "Malaria": {"range": "Negative", "unit": "Binary"},
    "Widal Test": {"range": "Negative", "unit": "Binary"},
    "Hepatitis B": {"range": "Negative", "unit": "Binary"},
    "Voluntary Serology": {"range": "Negative", "unit": "Binary"},
}

# Function to calculate score for numerical vitals
def calculate_vital_score(observed_value, ideal_range, deviation_factor=0.5):
    if isinstance(ideal_range, tuple):  # For numerical vitals
        ideal_min, ideal_max = ideal_range
        ideal_value = (ideal_min + ideal_max) / 2
        
        if ideal_min <= observed_value <= ideal_max:
            return 100  # Perfect score
        else:
            deviation = abs(observed_value - ideal_value)
            return max(0, 100 - deviation_factor * deviation)
    
    elif isinstance(ideal_range, str):  # For binary vitals
        return 100 if observed_value == ideal_range else 0

# Function to calculate total health score
def calculate_total_health_score(user_data):
    scores = []
    for vital, value in user_data.items():
        if vital in WHO_RANGES:
            vital_score = calculate_vital_score(value, WHO_RANGES[vital]["range"])
            scores.append(vital_score)
    return sum(scores) / len(scores) if scores else 0

# Function to classify health status
def categorize_health(total_score):
    if total_score >= 90:
        return "Excellent"
    elif total_score >= 70:
        return "Good"
    elif total_score >= 50:
        return "Average"
    else:
        return "Poor"

# Streamlit UI
st.title("🩺 Health Score Evaluation System")
st.write("Enter your health vitals to calculate your health score based on WHO standards.")

user_data = {}

# Collect user inputs
def get_user_input():
    for vital, details in WHO_RANGES.items():
        if isinstance(details["range"], tuple):  # Numerical input
            user_data[vital] = st.number_input(f"{vital} ({details['unit']})", min_value=0.0, step=0.1)
        else:  # Binary input
            user_data[vital] = st.selectbox(f"{vital} ({details['unit']})", ["Negative", "Positive"])
get_user_input()

# Button to calculate health score
if st.button("Calculate Health Score"):
    total_score = calculate_total_health_score(user_data)
    category = categorize_health(total_score)
    
    st.subheader("Results")
    st.write(f"**Total Health Score:** {total_score:.2f}")
    st.write(f"**Health Category:** {category}")
    
    # Display category with color indication
    if category == "Excellent":
        st.success("You are in excellent health! Keep it up! ✅")
    elif category == "Good":
        st.info("Your health is good, but there's room for improvement! 🟡")
    elif category == "Average":
        st.warning("Your health is average. Consider making some healthy changes. 🟠")
    else:
        st.error("Your health is poor. Please seek medical advice. 🔴")







# Set-ExecutionPolicy Unrestricted -Scope Process
# Create a virtual environment 'python -m venv my_project_env'
# Activate the virtual environment using 'my_project_env\Scripts\activate'
# Install streamlit Application using 'pip install streamlit'
# Run the streamlit App using 'streamlit run Health_score_system.py'


