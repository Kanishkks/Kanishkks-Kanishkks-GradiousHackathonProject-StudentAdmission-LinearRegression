import streamlit as st
import joblib
import numpy as np

model = joblib.load('model.pkl')

st.title("University Admission Tool")

portal = st.selectbox("Select Portal", ["Student Portal", "College Portal", "Counselling Portal"])

pre_term_test = st.slider("Pre Term Test",290, 340)
final_term_test = st.slider("Final Term Test", 90, 120)
university_rating = st.selectbox("University Rating", [1,2,3,4,5])
sop_strength = st.slider("Statement Of Purpose Strength", 1.0, 5.0, 1.0, 0.5)
lor_score = st.slider("Letter Of Recommandation Score", 1.0, 5.0, 1.0, 0.5)
cgpa = st.slider("Cumulative Grade Point Average", 6.00, 10.00, 6.00, 0.01)
has_research_exp = st.selectbox("Has Research Experience (0 - No / 1 - Yes)", [0,1])


# dt = np.dtype([('Pre Term Test', 'i4'), ('Final Term Test', 'i4'), ('University Rating', 'i4'),('Statement of Purpose', 'f8'),('Letter Of Reccomandation', 'f8'),('CGPA', 'f8'),('Research Experience', 'i4')])
inputdf = np.array([[pre_term_test, final_term_test, university_rating,sop_strength,lor_score,cgpa,has_research_exp]])


if st.button("Predict Admission"):
    prediction = model.predict(inputdf)[0]
    admission_perc = f"{100 if int(prediction*100)>100 else int(prediction*100)}%"

    if portal == "Student Portal":
        st.header("Student Portal")
        st.write("Your Data has been calculated and the prediction is as follows")
        st.success(f"Your chances of getting admission into the University is {admission_perc}" )
    elif portal == "College Portal":
        st.header("College Portal")
        st.write(f"The Chances of accepting the student to Your University is {admission_perc}")
        if prediction>=0.75:
            st.success("This student can be admissioned into our university")
        else:
            st.error("It would be better to reject this student from admissioning into our university")
    elif portal == 'Counselling Portal':
        st.header("Counselling Portal")
        st.write(f"The Probability of landing an admission to that univeristy is {admission_perc}")
        if prediction>=0.9:
            st.success("This candidate can crack the admissions of better Universities")
        elif prediction>=0.75:
            st.info("This University is suitable for this candidate")
        else: 
            st.error("It is better to apply for lower level Universities")