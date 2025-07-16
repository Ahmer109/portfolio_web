import streamlit as st
import base64
import os
import requests
from io import BytesIO

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
# ASSET LOADING FUNCTIONS
# ---------------------------
def load_asset(asset_name, asset_type="image"):
    """Universal asset loader with multiple fallbacks"""
    # Local paths to try (relative to app directory)
    local_paths = [
        f"assets/{asset_name}",
        f"../assets/{asset_name}",
        asset_name
    ]
    
    # Try local files first
    for path in local_paths:
        if os.path.exists(path):
            return path
    
    # GitHub raw content URL fallback
    github_url = f"https://raw.githubusercontent.com/Ahmer109/portfolio_web/main/assets/{asset_name}"
    
    # Return based on asset type
    if asset_type == "image":
        return github_url  # Streamlit can display images directly from URL
    elif asset_type == "pdf":
        return github_url  # We'll handle PDFs differently
    
    return None

def load_pdf(asset_name):
    """Special handling for PDF files with multiple fallbacks"""
    # First try local files
    local_path = load_asset(asset_name, "pdf")
    if local_path and os.path.exists(local_path):
        return local_path
    
    # Try GitHub raw content
    github_url = f"https://raw.githubusercontent.com/Ahmer109/portfolio_web/main/assets/{asset_name}"
    
    # Return GitHub URL as fallback
    return github_url

# ---------------------------
# SIDEBAR
# ---------------------------
with st.sidebar:
    # Show debug info toggle
    # if st.checkbox("Show Debug Info"):
    #     debug_info()
    
    # Profile Image with multiple fallbacks
    try:
        img_path = load_asset("profile_img_.jpg")
        st.image(img_path, width=150, caption="Ahmer ALI")
    except Exception as e:
        st.error(f"Couldn't load profile image: {str(e)}")
        # Fallback to placeholder
        st.image("https://via.placeholder.com/150?text=Profile+Image", width=150)
    
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
        st.markdown('<div class="main-container">', unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 2], gap="large")
        
        with col1:
            try:
                img_path = load_asset("profile_img_.jpg")
                st.image(img_path, width=250)
            except Exception as e:
                st.error(f"Couldn't load profile image: {str(e)}")
                st.image("https://via.placeholder.com/250?text=Profile+Image", width=250)
            
        with col2:
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

# def resume_page():
#     with st.container():
#         st.title("📄 My Resume", anchor=False)
        
#         col1, col2 = st.columns([3, 1], gap="large")
        
#         with col1:
#             try:
#                 # Get PDF path from GitHub URL
#                 pdf_url = load_pdf("cv.pdf")
                
#                 # For GitHub URLs, we need to use a different approach
#                 if pdf_url.startswith("http"):
#                     # Download the PDF from GitHub
#                     response = requests.get(pdf_url)
#                     pdf_bytes = BytesIO(response.content)
                    
#                     # Display PDF
#                     base64_pdf = base64.b64encode(pdf_bytes.read()).decode('utf-8')
#                     pdf_display = f"""
#                     <div class="resume-viewer-container">
#                         <iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" type="application/pdf"></iframe>
#                     </div>
#                     """
#                     st.markdown(pdf_display, unsafe_allow_html=True)
                    
#                     # Reset pointer for download
#                     pdf_bytes.seek(0)
#                     resume_data = pdf_bytes.read()
#                 else:
#                     # Local file
#                     with open(pdf_url, "rb") as f:
#                         resume_data = f.read()
#                         base64_pdf = base64.b64encode(resume_data).decode('utf-8')
#                         pdf_display = f"""
#                         <div class="resume-viewer-container">
#                             <iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" type="application/pdf"></iframe>
#                         </div>
#                         """
#                         st.markdown(pdf_display, unsafe_allow_html=True)
                        
#             except Exception as e:
#                 st.error(f"Couldn't load resume: {str(e)}")
#                 st.markdown("""
#                 <div style="background: #ffebee; padding: 20px; border-radius: 10px;">
#                     <h3>Resume Preview Unavailable</h3>
#                     <p>Please download the resume using the button on the right.</p>
#                 </div>
#                 """, unsafe_allow_html=True)
#                 resume_data = None

#         with col2:
#             st.markdown("""
#             <div class="resume-highlights">
#                 <h3>Key Highlights</h3>
#                 <div class="highlight-card">
#                     <div class="highlight-icon">🎓</div>
#                     <div class="highlight-content">
#                         <div class="highlight-title">BSc in Computer Science</div>
#                     </div>
#                 </div>
#                 <div class="highlight-card">
#                     <div class="highlight-icon">💻</div>
#                     <div class="highlight-content">
#                         <div class="highlight-title">12+ Projects Completed</div>
#                     </div>
#                 </div>
#                 <div class="highlight-card">
#                     <div class="highlight-icon">📊</div>
#                     <div class="highlight-content">
#                         <div class="highlight-title">Data Analysis Skills</div>
#                     </div>
#                 </div>
#                 <div class="highlight-card">
#                     <div class="highlight-icon">🤖</div>
#                     <div class="highlight-content">
#                         <div class="highlight-title">AI/ML Experience</div>
#                     </div>
#                 </div>
                
#                 <h3 class="skills-title">Technical Skills</h3>
#                 <div class="skill-card">
#                     <div class="skill-info">
#                         <span>Python</span>
#                         <span>90%</span>
#                     </div>
#                     <div class="skill-bar-container">
#                         <div class="skill-bar" style="width: 90%"></div>
#                     </div>
#                 </div>
#                 <div class="skill-card">
#                     <div class="skill-info">
#                         <span>Streamlit</span>
#                         <span>85%</span>
#                     </div>
#                     <div class="skill-bar-container">
#                         <div class="skill-bar" style="width: 85%"></div>
#                     </div>
#                 </div>
#                 <div class="skill-card">
#                     <div class="skill-info">
#                         <span>Pandas</span>
#                         <span>80%</span>
#                     </div>
#                     <div class="skill-bar-container">
#                         <div class="skill-bar" style="width: 80%"></div>
#                     </div>
#                 </div>
#                 <div class="skill-card">
#                     <div class="skill-info">
#                         <span>Flutter</span>
#                         <span>70%</span>
#                     </div>
#                     <div class="skill-bar-container">
#                         <div class="skill-bar" style="width: 70%"></div>
#                     </div>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)
            
#             # Download button
#             if resume_data:
#                 st.download_button(
#                     "⬇️ Download Resume", 
#                     resume_data, 
#                     file_name="Ahmer_ALI_Resume.pdf",
#                     mime="application/pdf",
#                     use_container_width=True,
#                     key="resume-download"
#                 )
#             else:
#                 st.markdown("""
#                 <div style="text-align: center; margin-top: 20px;">
#                     <a href="https://raw.githubusercontent.com/Ahmer109/portfolio_web/main/assets/cv.pdf" 
#                        class="github-button" 
#                        download="Ahmer_ALI_Resume.pdf">
#                        Download Resume
#                     </a>
#                 </div>
#                 """, unsafe_allow_html=True)

# ---------------------------
# PAGE ROUTING
# ---------------------------
if page == "Home / About Me":
    home_page()
elif page == "Projects":
    projects_page()
# elif page == "Resume":
#     resume_page()

# ---------------------------
# CUSTOM CSS (Embedded as fallback)
# ---------------------------
st.markdown("""
<style>
:root {
    --primary-color: #4b6cb7;
    --secondary-color: #3a56a0;
    --dark-bg: #0f0c29;
    --darker-bg: #0a081f;
    --card-bg: rgba(26, 26, 46, 0.8);
    --text-color: #ffffff;
    --text-secondary: #d1d1d1;
    --accent-color: #6a5acd;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: var(--text-color);
    margin: 0;
    padding: 0;
}

.stApp {
    background: linear-gradient(135deg, var(--dark-bg) 0%, #302b63 50%, #24243e 100%) !important;
    background-attachment: fixed !important;
}

.main-container {
    background: var(--card-bg) !important;
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    margin-bottom: 2rem;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, var(--darker-bg) 0%, #16213e 100%) !important;
    color: white;
    padding: 1.5rem !important;
}

/* ... (rest of your CSS) ... */
</style>
""", unsafe_allow_html=True)
