import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model/model.pkl')
features = joblib.load('model/features.pkl')

st.set_page_config(
    page_title="Employee Attrition Prediction", layout="centered")
st.title('Prediksi Employee Attrition at Jaya-Jaya Maju')
st.write("Masukkan data karyawan di bawah ini.")

# input field berdasarkan jenis data

def generate_input_fields():
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age', min_value=18, max_value=100)
        business_travel = st.selectbox(
            'Business Travel', ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'])
        daily_rate = st.number_input('Daily Rate', min_value=1, max_value=1500)
        department = st.selectbox(
            'Department', ['Research & Development', 'Sales', 'Human Resources'])
        distance_from_home = st.number_input(
            'Distance From Home', min_value=0, max_value=30)
        education = st.selectbox(
            'Education', ['Below College', 'College', 'Bachelor', 'Master', 'Doctor'])
        education_field = st.selectbox('Education Field', [
            'Medical', 'Life Sciences', 'Technical Degree', 'Human Resource', 'Other'])
        environment_satisfaction = st.selectbox(
            'Environment Satisfaction', ['Low', 'Medium', 'High', 'Very High'])
        gender = st.selectbox('Gender', ['Male', 'Female'])
        hourly_rate = st.number_input(
            'Hourly Rate', min_value=30, max_value=100)

    with col2:
        job_involvement = st.selectbox(
            'Job involvement', ['Low', 'Medium', 'High', 'Very High'])
        job_level = st.number_input('JobLevel', min_value=1, max_value=5)
        job_role = st.selectbox('Job Role', ['Sales Executive', 'Research Scientist', 'Laboratory Technician', 'Manufacturing Director',
                                'Healthcare Representative', 'Manager', 'Research Director', 'Sales Representative', 'Human Resources'])
        job_satisfaction = st.selectbox(
            'Job Satisfaction', ['Low', 'Medium', 'High', 'Very High'])
        marital_status = st.selectbox('Marital Status', [
            'Single', 'Married', 'Divorced'])
        monthly_income = st.number_input(
            'Monthly Income', min_value=1000, max_value=20000)
        monthly_rate = st.number_input(
            'Monthly Rate', min_value=2000, max_value=30000)
        num_companies_worked = st.number_input(
            'Num Companies Worked', min_value=0, max_value=10)
        overtime = st.selectbox('Over Time', ['Yes', 'No'])
        percent_salary_hike = st.number_input(
            'Percent Salary Hike', min_value=0, max_value=30)

    with col3:
        performance_rating = st.selectbox(
            'Performance Rating', ['Low', 'Good', 'Excellent', 'Outstanding'])
        relationship_satisfaction = st.selectbox(
            'Relationship Satisfaction', ['Low', 'Good', 'High', 'Very High'])
        stock_option_level = st.number_input(
            'Stock Option Level', min_value=0, max_value=3)
        total_working_years = st.number_input(
            'Total Working Years', min_value=0, max_value=40)
        training_times_last_year = st.number_input(
            'Training Times Last Year', min_value=0, max_value=10)
        work_life_balance = st.selectbox(
            'Work Life Balance', ['Low', 'Good', 'Excellent', 'Outstanding'])
        years_at_company = st.number_input(
            'Years at Company', min_value=0, max_value=40)
        years_in_current_role = st.number_input(
            'Years in Current Role', min_value=0, max_value=20)
        years_since_last_promotion = st.number_input(
            'Years Since Last Promotion', min_value=0, max_value=20)
        years_with_curr_manager = st.number_input(
            'Years with Current Manager', min_value=0, max_value=20)
    input_data = pd.DataFrame({
        'Age': [age],
        'BusinessTravel': [business_travel],
        'DailyRate': [daily_rate],
        'Department': [department],
        'DistanceFromHome': [distance_from_home],
        'Education': [education],
        'EducationField': [education_field],
        'EnvironmentSatisfaction': [environment_satisfaction],
        'Gender': [gender],
        'HourlyRate': [hourly_rate],
        'JobInvolvement': [job_involvement],
        'JobLevel': [job_level],
        'JobRole': [job_role],
        'JobSatisfaction': [job_satisfaction],
        'MaritalStatus': [marital_status],
        'MonthlyIncome': [monthly_income],
        'MonthlyRate': [monthly_rate],
        'NumCompaniesWorked': [num_companies_worked],
        'OverTime': [overtime],
        'PercentSalaryHike': [percent_salary_hike],
        'PerformanceRating': [performance_rating],
        'RelationshipSatisfaction': [relationship_satisfaction],
        'StockOptionLevel': [stock_option_level],
        'TotalWorkingYears': [total_working_years],
        'TrainingTimesLastYear': [training_times_last_year],
        'WorkLifeBalance': [work_life_balance],
        'YearsAtCompany': [years_at_company],
        'YearsInCurrentRole': [years_in_current_role],
        'YearsSinceLastPromotion': [years_since_last_promotion],
        'YearsWithCurrManager': [years_with_curr_manager]
    })
    return input_data


# Formulir input
with st.form("prediction_form"):
    input_df = generate_input_fields()
    submitted = st.form_submit_button("🔎 Prediksi Attrition")

# Prediksi jika tombol ditekan
if submitted:
    try:
        prediction = model.predict(input_df)[0]
        prediction_proba = model.predict_proba(input_df)[0]

        st.subheader("Hasil Prediksi")
        if prediction == "Yes":
            st.error(
                f"⚠️ Pegawai kemungkinan AKAN melakukan attrition. (Probabilitas: {prediction_proba[1]:.2f})")
        else:
            st.success(
                f"✅ Pegawai kemungkinan TIDAK akan melakukan attrition. (Probabilitas: {prediction_proba[0]:.2f})")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memproses input: {e}")
