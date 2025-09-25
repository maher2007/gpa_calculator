from PIL import Image
import streamlit as st

logo = Image.open("silver_shine_image_1.png")
col1, col2,  = st.columns([1,4])
with col1:
    st.image(logo, width=100 )
with col2:
    st.title("GPA Calculator")
    st.write("𝕸𝖆𝖉𝖊 𝖇𝖞: 𝕸𝖆𝖍𝖊𝖗 𝕯𝖆𝖌𝖊𝖘𝖙𝖆𝖓𝖎")

course_no = st.number_input("Enter the number of courses", min_value=1, max_value=20, step=1)
i = 0
cridits = []
grade = []
course_name = []
for i in range (course_no):
    course_name.append(st.text_input("Course name", key=(f"n{i}"))) 
    cridits.append(st.slider("enter Credit hours",0,4,1, key = (f"c{i}")))
    grade.append(st.selectbox("Choose a grade", ["A+","A","B+", "B","C+", "C","D+", "D", "F"], key = (f"ch{i}")))
    st.write("------------------------------------")
mark = {"A+": 4,"A": 3.75,"B+": 3.5, "B":3,"C+":2.5, "C":2,"D+":1.5, "D":1, "F":0}
i = 0
table = {}
total_score = 0
total_cridits = 0
if st.button("Calculate GPA"):
    for i in range (course_no):
        total_score += mark[grade[i]] * cridits[i]
        total_cridits += cridits[i]
    st.title(f"your gpa is: {total_score/total_cridits}")
