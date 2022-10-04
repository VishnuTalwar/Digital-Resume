import streamlit as st
from pathlib import Path
from PIL import Image

current_dir =Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/"styles"/"main.css"
resume_file = current_dir/"assets"/"CV.pdf"
profile_pic = current_dir/"assets"/"profile-pic (3).png"


PAGE_TITLE = "Digital CV | Vishnu Talwar"
PAGE_ICON = ":wave:"
NAME = "Hi, I am Vishnu :wave:"
DESCRIPTION = """
A Data Science Enthusiast and a Software Developer Engineer
"""
EMAIL = "vishnutalwar02@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/vishnu-talwar-176273168/",
    "GitHub": "https://github.com/VishnuTalwar",
    "Twitter": "https://twitter.com/VishnuTalwar7",
}
PROJECTS = {
    "🏆Data-Analysis-using-Tableau": "https://github.com/VishnuTalwar/Data-Analysis-using-Tableau",
    "🏆 Real Time Weather Data Monitoring App Using Dash/Plotly": "https://github.com/VishnuTalwar/Weather_Station_Dashboard",
    "🏆 Real_estate_price_predictor Using Machine Learning": "https://github.com/VishnuTalwar/Real_estate_price_predictor",
    
}

CERTIFICATES = {
    "👨‍🎓My Certificates link":"https://drive.google.com/drive/folders/1zl_9vQNJiHd-k3V3d1SMZIjQaJlpZYV0?usp=sharing"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")




# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Pursuing B.Tech in Computer Science from SRM Institute Of Science and Technology (2019-2023)
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles 
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, numPy), SQL, Flutter
- 📊 Data Visulization: PowerBi, MS Excel, Dash/Plotly, Tableau
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MySQL
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Intern | India Meteorological Department, New Delhi**")
st.write("06/2022 - 09/2022")
st.write(
    """
- ► Worked with vast sets of data and make an interactive, real-time dashboard using python, NumPy, dash/plotly
- ► The Dashboard is currently used by IMD officials 
- ► Worked Under MR. Rahul Saxena (F-level Scientist in Hydromet Division)
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


# --- Certificates---
st.write('\n')
st.subheader("Certificates")
st.write("---")
for project, link in CERTIFICATES.items():
    st.write(f"[{project}]({link})")



# st.set_page_config(page_title="my webpage", page_icon=":tada:", layout = "wide")

# st.subheader('Hi, I am Vishnu :wave:')
# st.title("A Data Science Enthusiast and a Software Developer Engineer")
# st.title("I am passionate about finding ways to use Python to be more efficient and effective in business settings")
