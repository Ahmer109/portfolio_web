import streamlit as st
import base64
import os
from pathlib import Path

# ---------------------------
# PAGE CONFIGURATION
# ---------------------------
st.set_page_config(
    page_title="Ahmer ALI | Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------
# FILE PATH HANDLING (Works for both local and Streamlit Cloud)
# ---------------------------
def get_file_path(filename):
    """Get absolute path to file for both local and Streamlit Cloud"""
    if "HOSTNAME" in os.environ:  # Detect if running on Streamlit Cloud
        return f"./{filename}"
    else:
        return os.path.join(os.path.dirname(__file__), filename)


# ---------------------------
# SIDEBAR
# ---------------------------
with st.sidebar:
    # Profile Image with error handling
    st.title("Ahmer ALI")
    st.markdown("""
    **Python Developer | Data Enthusiast**  
    Building solutions with code and creativity
    """)
    
    st.markdown("---")
    
    # Navigation
    st.subheader("Navigation")
    page = st.radio("", ["Home / About Me", "Projects", "Resume"], label_visibility="collapsed")
    
    st.markdown("---")
    
    # Contact Info
    st.subheader("Let's Connect")
    st.markdown("""
    <div class="contact-info">
        <div class="contact-item">
            <span class="contact-icon">📧</span>
            <a href="mailto:ahmeralishoukat.work@gmail.com">ahmeralishoukat.work@gmail.com</a>
        </div>
        <div class="contact-item">
            <span class="contact-icon">🔗</span>
            <a href="https://www.linkedin.com/in/ahmer-ali-3933a4309/" target="_blank">LinkedIn</a>
        </div>
        <div class="contact-item">
            <span class="contact-icon">💻</span>
            <a href="https://github.com/Ahmer109" target="_blank">GitHub</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------
# PAGE CONTENT
# ---------------------------
def home_page():
    with st.container():
            
        
        st.title("Hello, I'm Ahmer ALI 👋", anchor=False)
        st.markdown("""
        <div class="intro-text">
        I'm a passionate Python developer with expertise in building data-driven applications 
        and creative solutions. I love turning ideas into functional, user-friendly applications.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        with st.expander("📚 Education & Experience", expanded=True):
            st.markdown("""
            <div class="experience-item">
                <span class="exp-icon">🎓</span>
                <div class="exp-content">
                    <strong>BSc in Computer Science</strong>
                </div>
            </div>
            <div class="experience-item">
                <span class="exp-icon">💼</span>
                <div class="exp-content">
                    <strong>Python Developer Intern</strong> at Gexton Education
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with st.expander("🛠️ Technical Skills", expanded=True):
            cols = st.columns(3)
            with cols[0]:
                st.markdown("**Programming**")
                st.markdown("- Python")
                st.markdown("- Dart")
                
            with cols[1]:
                st.markdown("**Frameworks**")
                st.markdown("- Streamlit")
                st.markdown("- Flutter")
                st.markdown("- Pandas")
                
            with cols[2]:
                st.markdown("**Tools**")
                st.markdown("- Firebase")
                st.markdown("- Git")
                st.markdown("- VS Code")
        
        st.markdown('</div>', unsafe_allow_html=True)

def projects_page():
    with st.container():
        st.markdown('<div class="main-container">', unsafe_allow_html=True)
        
        st.title("🚀 My Projects", anchor=False)
        st.markdown("Here are some of my recent projects showcasing my skills and creativity.")
        
        projects = [
            {
                "title": "Contact Management System",
                "desc": "A Python console-based contact management system using Firebase Realtime Database to save, view, edit, and delete contacts.",
                "tech": "Python, Firebase",
                "github": "https://github.com/Ahmer109/internship_Task_1",
                "icon": "📱"
            },
            {
                "title": "File Handling Based Dictionary",
                "desc": "A stylish Streamlit-based word meaning dictionary app that allows users to search, add, and store words with their meanings.",
                "tech": "Python, Streamlit",
                "github": "https://github.com/Ahmer109/internship_Task_2",
                "icon": "📖"
            },
            {
                "title": "Dictionary with Audio Pronunciation",
                "desc": "An interactive Streamlit-based English-Urdu dictionary app with word search, add functionality, and text-to-speech audio playback using gTTS.",
                "tech": "Python, gTTS, Streamlit",
                "github": "https://github.com/Ahmer109/internship_Task_3",
                "icon": "🔊"
            },
            {
                "title": "Emotion Detection from Live Webcam",
                "desc": "A Streamlit-based real-time emotion detection app that uses DeepFace to analyze webcam input and play matching mood-based music.",
                "tech": "Python, DeepFace, Streamlit",
                "github": "https://github.com/Ahmer109/internship_Task_4",
                "icon": "😊"
            },
            {
                "title": "Currency Converter",
                "desc": "A simple and interactive Streamlit app to convert currencies and track conversion history using real-time exchange rates.",
                "tech": "Python, API Integration",
                "github": "https://github.com/Ahmer109/internship_Task_5",
                "icon": "💱"
            },
            {
                "title": "File Organization Script",
                "desc": "A Streamlit-based tool to automatically organize files in a directory by type into categorized folders.",
                "tech": "Python, File Handling",
                "github": "https://github.com/Ahmer109/internship_Task_6",
                "icon": "🗂️"
            },
            {
                "title": "2D Maze Game Development",
                "desc": "An interactive 2D maze game built with Streamlit and Pygame where you navigate to the goal while collecting a bonus tile.",
                "tech": "Python, Pygame",
                "github": "https://github.com/Ahmer109/internship_Task_7",
                "icon": "🎮"
            },
            {
                "title": "Sudoku Solver with Numpy",
                "desc": "A Streamlit-based Sudoku solver and checker that validates and completes user-input puzzles with color-coded feedback.",
                "tech": "Python, Numpy",
                "github": "https://github.com/Ahmer109/internship_Task_8",
                "icon": "🧩"
            },
            {
                "title": "Attendance Management System",
                "desc": "A secure Streamlit-based attendance system with PIN, barcode, and fingerprint simulation, supporting both student and teacher dashboards.",
                "tech": "Python, Streamlit",
                "github": "https://github.com/Ahmer109/internship_Task_9",
                "icon": "📝"
            },
            {
                "title": "Guess the Number Game",
                "desc": "A fun Streamlit-based number guessing game with difficulty levels, hints, scoring, and a leaderboard.",
                "tech": "Python, Game Development",
                "github": "https://github.com/Ahmer109/internship_Task_10",
                "icon": "🔢"
            },
            {
                "title": "Temperature Converter",
                "desc": "A simple Streamlit app to convert temperatures between Celsius, Fahrenheit, and Kelvin.",
                "tech": "Python, Streamlit",
                "github": "https://github.com/Ahmer109/internship_Task_11",
                "icon": "🌡️"
            },
            {
                "title": "AI-Based Resume Screening System",
                "desc": "An AI-powered Streamlit tool that compares resumes to a job description using TF-IDF to rank candidate matches.",
                "tech": "Python, NLP, TF-IDF",
                "github": "https://github.com/Ahmer109/internship_Task_12",
                "icon": "🤖"
            },
        ]

        for i in range(0, len(projects), 2):
            cols = st.columns(2)
            for j in range(2):
                if i + j < len(projects):
                    proj = projects[i + j]
                    with cols[j]:
                        with st.container():
                            st.markdown(f"### <span class='project-icon'>{proj['icon']}</span> {proj['title']}", unsafe_allow_html=True)
                            st.markdown(f"<div class='project-desc'>{proj['desc']}</div>", unsafe_allow_html=True)
                            st.markdown(f"<div class='project-tech'><strong>Technologies:</strong> {proj['tech']}</div>", unsafe_allow_html=True)
                            st.markdown(f"<a href='{proj['github']}' target='_blank' class='github-button'>View on GitHub</a>", unsafe_allow_html=True)
                            st.markdown("<div class='project-spacer'></div>", unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

def resume_page():
    with st.container():
        # st.markdown('<div class="main-container">', unsafe_allow_html=True)
        
        st.title("📄 My Resume", anchor=False)
        
        col1, col2 = st.columns([3, 1], gap="large")
        
        with col1:
            resume_path = get_file_path("assets/cv.pdf")
            try:
                with open(resume_path, "rb") as f:
                    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                    pdf_display = f"""
                    <div class="resume-viewer-container">
                        <iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" type="application/pdf"></iframe>
                    </div>
                    """
                    st.markdown(pdf_display, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Couldn't load resume: {str(e)}")

        with col2:
            st.markdown("""
            <div class="resume-highlights">
                <h3>Key Highlights</h3>
                <div class="highlight-card">
                    <div class="highlight-icon">🎓</div>
                    <div class="highlight-content">
                        <div class="highlight-title">BSc in Computer Science</div>
                    </div>
                </div>
                <!-- Rest of your highlights -->
            </div>
            """, unsafe_allow_html=True)
            
            try:
                with open(resume_path, "rb") as f:
                    st.download_button(
                        "⬇️ Download Resume", 
                        f, 
                        file_name="Ahmer_ALI_Resume.pdf",
                        use_container_width=True,
                        key="resume-download"
                    )
            except Exception as e:
                st.error(f"Couldn't prepare resume download: {str(e)}")

        st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# PAGE ROUTING
# ---------------------------
if page == "Home / About Me":
    home_page()
elif page == "Projects":
    projects_page()
elif page == "Resume":
    resume_page()
