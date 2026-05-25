# University Management System using Streamlit

# pip install streamlit
import streamlit as st

st.set_page_config(
    page_title = "University System",
    layout = "wide"
)

st.title("University Management System")

# creating a session variable for list of colleges
if "colleges" not in st.session_state:
    st.session_state.colleges = []

# Side bar
menu_choice = st.sidebar.radio(
    "Select Action",
    (
    "Create College",
    "Add Student",
    "Add Teacher",
    "Display Students",
    "Display Teachers",
    "List Colleges"
    )
)

class college:
    def __init__(self, cname):
        self.cname = cname
        self.students = []  # list of student objects
        self.teachers = []  # list of teacher objects
    
    def add_student(self, s ):
        self.students.append(s)
    
    def add_teacher(self, t):
        self.teachers.append(t)

class person:
    def __init__(self, branch, name):
        self.branch = branch
        self.name = name

class student(person):
    def __init__(self, rollno, name, branch):
        super().__init__(branch,name)
        self.rollno = rollno


class teacher(person):
    def __init__(self, branch, name, subject):
        super().__init__(branch,name)
        self.subject = subject

# finding college out of all available colleges
def find_college(cname):
    return next((c for c in st.session_state.colleges if c.cname == cname), None)

# create a new college
if menu_choice == "Create College":
    cname = st.text_input("Enter new college name")
    if st.button("Create"):
        st.session_state.colleges.append(college(cname))   # storing the object
        st.success(f"{cname} created successfully")

# Add student
elif menu_choice == "Add Student":
    if not st.session_state.colleges:
        st.info("Please insert a college first")
    else:
        clgname = st.selectbox("Choose College", [c.cname for c in st.session_state.colleges])
        roll = st.text_input("Enter your Roll number")
        sname = st.text_input("Enter Student name")
        branch = st.text_input("Enter the branch")
        if st.button("Add Student"):
            if not(roll and sname and branch and clgname):
                st.error("Please Enter all the require info")
            else:
                 clg = find_college(clgname)
                 clg.add_student(student(roll,sname,branch))
                 st.success("Student added successfully")
