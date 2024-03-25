import streamlit as st
import pandas as pd
import datafile as dfile
import krce

st.set_page_config(page_title="GPA Calculator", page_icon=":🖥️:")

with st.sidebar:
    st.title(":green[Calculations]")
    st.write(":gray[The calculation methods used to find the grade point average of a person]")
    st.header(":green[Grade point Table]")
    st.write(":gray[The grade point allocation table is shown here]")
    data = {
        'Grades': ['O', 'A+', 'A', 'B+', 'B', 'C', 'U'],
        'Grade Points': [10, 9, 8, 7, 6, 5, 0]
    }

    df=pd.DataFrame(data)

    st.dataframe(df,hide_index=True,use_container_width=True)

    st.header(":green[Formula]")
    st.write(":gray[The Formula used for the Grade point average Calculation ]")
    st.latex("\\displaystyle\\frac{\\sum^i {Grade Points}_i \\times {Credits}_i}{\\sum^i {Credits}_i }")

    st.title(":green[Developer]")
    st.write(":gray[Developed by :violet[Keerthivasan S J], this GPA calculator app offers a user-friendly interface for effortless grade point average computation.]")
    
def gpa(grade,credit):
    gradepoint=[]
    credits_lost=[]
    i=0
    for g in grade:
        if g in "oO":
            gradepoint.append(10)
        elif g in ("a+","A+"):
            gradepoint.append(9)
        elif g in "Aa":
            gradepoint.append(8)
        elif g in ("b+","B+"):
            gradepoint.append(7)
        elif g in "Bb":
            gradepoint.append(6)
        elif g in "Cc":
            gradepoint.append(5)
        elif g in "Uu":
            credits_lost.append(credit[i])
            gradepoint.append(0)
        i+=1

    total_credit=sum(credit)
    credits_obtained=total_credit-sum(credits_lost)
    gp_x_credit=[g*c for g,c in zip(gradepoint,credit)]
    try:
        gpa=sum(gp_x_credit)/total_credit
    except ZeroDivisionError:
        gpa=sum(gp_x_credit)

    return gpa,total_credit,credits_obtained

st.title(":green[GPA Calculator] :clipboard:")

grade_list=list()
credit_list=list()

col1,col2,col3=st.columns(3)

colleges = ["KRCT","KRCE"]

with col1:
    college = st.selectbox("College",colleges)
with col2:
    dept = st.empty()
with col3:
    sem = st.empty()

no_subject=0

if college == "KRCT":
    with col2:
        dept = st.selectbox("Department",dfile.department)
    with col3:
        sem = st.selectbox("Semenster",dfile.semester)
    if dept==dfile.department[1]:
        pass
        #no_subject=len(dfile.civil[sem]) if sem!=dfile.semester[0] and dept!=dfile.department[0] else 0
    elif dept==dfile.department[2]:
        if sem!=dfile.semester[0]:
            no_subject=len(dfile.cse[sem]) 
            subject = list(dfile.cse[sem].keys())
            credit_score = list(dfile.cse[sem].values())
    elif dept==dfile.department[3]:
        pass
        #no_subject=len(dfile.eee[sem]) if sem!=dfile.semester[0] and dept!=dfile.department[0] else 0
    elif dept==dfile.department[4]:
        pass
        #no_subject=len(dfile.ece[sem]) if sem!=dfile.semester[0] and dept!=dfile.department[0] else 0
    elif dept==dfile.department[5]:
        pass
        #no_subject=len(dfile.mech[sem]) if sem!=dfile.semester[0] and dept!=dfile.department[0] else 0
    elif dept==dfile.department[6]:
        if sem!=dfile.semester[0]:
            no_subject=len(dfile.ai[sem]) 
            subject = list(dfile.ai[sem].keys())
            credit_score = list(dfile.ai[sem].values())

elif college == "KRCE":
    with col2:
        dept = st.selectbox("Department",krce.departments)
    with col3:
        sem = st.selectbox("Semenster",krce.semester)
    if dept==krce.departments[1]:
        if sem!=krce.semester[0]:
            no_subject=len(krce.cse[sem]) 
            subject = list(krce.cse[sem].keys())
            credit_score = list(krce.cse[sem].values())
    elif dept==krce.departments[2]:
        if sem!=krce.semester[0]:
            no_subject=len(krce.eee[sem]) 
            subject = list(krce.eee[sem].keys())
            credit_score = list(krce.eee[sem].values())
    elif dept==krce.departments[3]:
        if sem!=krce.semester[0]:
            no_subject=len(krce.ece[sem]) 
            subject = list(krce.ece[sem].keys())
            credit_score = list(krce.ece[sem].values())
    elif dept==krce.departments[4]:
        if sem!=krce.semester[0]:
            no_subject=len(krce.mech[sem]) 
            subject = list(krce.mech[sem].keys())
            credit_score = list(krce.mech[sem].values())
    elif dept==krce.departments[5]:
        if sem!=krce.semester[0]:
            no_subject=len(krce.aids[sem]) 
            subject = list(krce.aids[sem].keys())
            credit_score = list(krce.aids[sem].values())
    elif dept==krce.departments[6]:
        if sem!=krce.semester[0]:
            no_subject=len(krce.csai[sem]) 
            subject = list(krce.csai[sem].keys())
            credit_score = list(krce.csai[sem].values())
    elif dept==krce.departments[7]:
        if sem!=krce.semester[0]:
            no_subject=len(krce.it[sem]) 
            subject = list(krce.it[sem].keys())
            credit_score = list(krce.it[sem].values())
    elif dept==krce.departments[8]:
        #no_subject=len(krce.csbs[sem]) if sem!=krce.semester[0] and dept!=krce.departments[0] else 0
        pass
if no_subject!=0:
    st.header(":green[Provide the Grades]")

for i in range(no_subject):
    grades=st.selectbox(f"{subject[i]}",['O','A+','A','B+','B','C','U'])
    grade_list.append(grades)
    credit_list=credit_score

if st.button(":orange[Calculate]"):
    Gpa,total_credits_awarded,credits_obtained=gpa(grade=grade_list,credit=credit_list)

    col1,col2=st.columns(2)
    with col1:
        st.header(":green[Total Credits Awarded]")
        st.subheader(total_credits_awarded)
        
    with col2:
        st.header(":green[Obtained Credits]")
        st.subheader(credits_obtained)

    st.title(":green[Your Gpa is] :red[{:.2f}] :medal:".format(Gpa))
    
    if st.button(":orange[Downlode]"):
        pass

    print(grade_list,credit_list,sep="\n")
