import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height / 100) ** 2

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "It's important to eat a balanced diet and maintain a healthy weight."
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "Great job! Keep maintaining a balanced diet and regular exercise."
    elif 25 <= bmi < 29.9:
        return "Overweight", "Consider adopting a healthier diet and increasing physical activity."
    else:
        return "Obesity", "It's recommended to consult with a healthcare provider for personalized advice."

def main():
    st.title("BMI Calculator")
    st.write("A simple app to calculate and understand your Body Mass Index (BMI).")

    st.header("Input your details:")
    
    weight = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, value=70.0)
    height = st.number_input("Height (cm)", min_value=0.0, max_value=250.0, value=170.0)

    if st.button("Calculate BMI"):
        if weight == 0.0 or height == 0.0:
            st.warning("Please enter valid weight and height values.")
        else:
            bmi = calculate_bmi(weight, height)
            category, advice = bmi_category(bmi)
            st.success(f"Your BMI is: {bmi:.2f}")
            st.info(f"Category: {category}")
            st.write(advice)

if __name__ == "__main__":
    main()
