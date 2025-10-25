import streamlit as st

# --- Page Configuration ---
# Sets the title and icon of your browser tab
st.set_page_config(
    page_title="Md. Atick Hassan's Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# --- Your Personal Information ---
# URLs and contact info
github_username = "mdatickhassan"
profile_pic_url = f"https://github.com/{github_username}.png"
linkedin_url = "https://www.linkedin.com/in/md-atickhassan"
github_url = "https://github.com/mdatickhassan"
phone_number = "01604176972"
# twityer_handle = "MdAtick57332" # You can add this back in the 'Connect' tab if you wish

# --- Header & Introduction Section ---
# Uses columns to put your picture next to your name
col1, col2 = st.columns([1, 2], gap="medium") # 1 part image, 2 parts text

with col1:
    st.image(profile_pic_url, width=230, caption="Md. Atick Hassan")

with col2:
    st.title("Md. Atick Hassan")
    st.subheader("Data Analyst & Tech Enthusiast") # Fixed typo "Aanyst"
    st.write("Welcome to my personal corner on the web. I turn data into insights. 🚀")
    st.write("Feel free to look around and connect!")

st.divider()

# --- Tabbed Navigation ---
# This makes the dashboard interactive instead of one long page
tab1, tab2, tab3, tab4 = st.tabs([
    "[ 👨‍💼 About Me ]", 
    "[ 🚀 My Projects ]", 
    "[ 💼 Experience ]", 
    "[ 🤝 Connect ]"
])


# --- Tab 1: About Me ---
with tab1:
    st.header("About Me")
    st.write("""
    Hello! I'm **Md. Atick Hassan**.
Hi, Dear Clients I am Md Atick Hassan And My role is Data Analyst.
         As a data analyst, my passion is to find insights for business,
          and other data-driven problems. I have worked in this industry for 1+ years. 
         I have experience in the following programming languages and statistical analysis software: 
         R, SPSS, Power BI, Python, SQL, Excel.
    """)
    
    st.divider()

    st.subheader("My Toolkit 🛠️")
    # Using columns for a cleaner skills layout
    skills_col1, skills_col2 = st.columns(2)
    
    with skills_col1:
        st.info("**Programming & Databases:**")
        st.markdown("""
        - **Python:** (Pandas, Scikit-learn, Matplotlib, Seaborn)
        - **R:** (dplyr, ggplot2)
        - **SQL**
        """)
        
    with skills_col2:
        st.info("**Tools & Platforms:**")
        st.markdown("""
        - **Power BI**
        - **SPSS**
        - **Excel:** (Pivot Tables, VLOOKUP, Charts)
        - **Streamlit** (for building apps like this one!)
        """)


# --- Tab 2: My Projects ---
with tab2:
    st.header("Projects 🚀")
    st.write("Here is a selection of my projects. Click the button to see the code.")
    
    # --- Using columns for a project gallery "card" layout ---
    proj_col1, proj_col2, proj_col3 = st.columns(3, gap="medium")

    with proj_col1:
        with st.container(border=True, height=350): # Set height for uniform cards
            st.subheader("Project 1: Wine Classification using SVM")
            st.write("""
            Developed a machine learning algorithm (SVM) to identify fraudulent, 
            low-quality wine samples based on chemical analysis. This helps a 
            premium wine distributor prevent costly scams.
            """)
            st.markdown("**Technologies Used:** `Python`, `Scikit-learn`, `Pandas`, `Matplotlib`")
            st.link_button("View on GitHub ↗️", "https://github.com/mdatickhassan/Retail-Sales-Dashboard/blob/e566cd702fba650ec4d7ca32a10aa3623ba46195/Wine%20Classification%20using%20SVM.ipynb")

    with proj_col2:
        with st.container(border=True, height=350):
            # --- !! Review This !! ---
            st.subheader("Project 2: Two sample T-Test Analysis on Titanic")
            
            st.write("""
            Performed a two-independent-sample t-test to compare the mean age of male vs. female passengers. 
            This included checking assumptions for normality (Shapiro-Wilk test) and equal variance (F-test).
            """)
            st.markdown("**Technologies Used:** `R`, `RStudio`, `dplyr`,`ggplot2`")
            
            # --- !! FIX THIS LINK !! ---
            # st.error("Link needs update! This link currently points to Project 1.")
            st.link_button("View on GitHub ↗️", "https://github.com/mdatickhassan/Retail-Sales-Dashboard/blob/e566cd702fba650ec4d7ca32a10aa3623ba46195/Wine%20Classification%20using%20SVM.ipynb")

    with proj_col3:
        with st.container(border=True, height=350):
            st.subheader("Project 3: Retail Sales Dashboard")
            st.write("""
            Created a dynamic Excel dashboard for an e-commerce company's annual report. 
            It provides an interactive view of KPIs, customer behavior, and channel performance.
            """)
            st.markdown("**Technologies Used:** `Excel`, `Pivot Tables`, `VLOOKUP`, `Charts`")
            
            # --- !! FIX THIS LINK !! ---
            # st.error("Link needs update! This link currently points to Project 1.")
            st.link_button("View on GitHub ↗️", "https://github.com/mdatickhassan/Retail-Sales-Dashboard/blob/e566cd702fba650ec4d7ca32a10aa3623ba46195/Wine%20Classification%20using%20SVM.ipynb")


# --- Tab 3: Experience ---
with tab3:
    st.header("My Experience 💼")
    st.write("Here is my professional background. Please expand to see details.")
    
    # --- Using your original expanders here ---
    with st.expander("Job Title at [Fiver] (05/2025 - 10/2025)"):
        st.write("""
        - **Role:** Data Analyst.
        - **Responsibilities:** Analyzed datasets to extract insights, created visualizations, and presented findings to stakeholders.
        - **Technologies:** [e.g., Python, SQL, power BI,Excel,Spss,R etc.]
        """)

    


# --- Tab 4: Connect ---
with tab4:
    st.header("Connect with Me 🤝")
    st.write("I'm always open to discussing new projects, creative ideas, or opportunities.")
    st.write("")

    # --- Using columns for large, clickable buttons ---
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("🔗 Connect on LinkedIn", linkedin_url, use_container_width=True)
    with col2:
        st.link_button("🐙 Browse my GitHub", github_url, use_container_width=True)
    
    st.divider()

    # --- Interactive Contact Form ---
    st.subheader("Send Me a Message")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your message", height=150)
        
        # Form submission button
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            st.success(f"Thank you, {name}! Your message has been sent.")
            # In a real app, you would add code here to send an email
            # using st.secrets and Python's smtplib.
            
    st.divider()
    
    st.write(f"**Or contact me directly:**")
    st.warning("Privacy Warning: Displaying your phone number publicly can lead to spam. You may want to remove this line.")
    st.write(f"📞 **Phone:** {phone_number}")