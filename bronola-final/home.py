import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [   
        Page("home.py", "Quality Management Multiple Machine Learning Techniques", "👩‍💻"),
        Section("Application Development of Different Machine Learning Techniques",),
        Page("pages/aboutme.py", "ALL ABOUT MYSELF", "1️⃣", in_section=True),
        Page("pages/discription.py", "APPLICATION DETAILS", "2️⃣", in_section=True),
        Page("pages/learnings.py", "MY LEARNINGS FROM THE SUBJECT", "3️⃣", in_section=True),
    
  
        Section("PROJECTS", "💾"),
        Page("pages/predict.py", "PREDICTION OF DENGUE", "1️⃣", in_section=True),
        Page("pages/sentiment.py", "EMOTION ANALYZER", "2️⃣", in_section=True),
        Page("pages/image.py", "🦋IMAGE CLASSIFICATION OF BUTTERFLY AND MOTH 🐝", "3️⃣", in_section=True),


         Section("SOURCE CODE", "💾"),
        Page("pages/predict_src.py", "PREDICTION", "1️⃣", in_section=True),
        Page("pages/sentiment_src.py", "SENTIMENT ANALYZER", "2️⃣", in_section=True),
        Page("pages/image_src.py", "IMAGE CLASSIFICATION", "3️⃣", in_section=True),
    

    ]
)

hide_pages(["Thank you"])

st.markdown("### 👨‍🔧 ML Learning by BRONOLA, KYLA MAY ")

st.image("./p1.jpg")
st.markdown("""<a href="Kyla.jpg">""",unsafe_allow_html=True,)

st.info("Visit the project [Github](https://github.com/koalatech/streamlit_web_app)")
st.info("⚙️🤖This application showcases various machine learning techniques for quality management. Each section provides insights into different aspects of the projects and methodologies used.") 
st.markdown("---")

with st.expander("WHAT IS QUANTITATIVE METHOD?"):
    st.markdown("""
    
    Quantitative methods are research techniques that focus on quantifying the collection and analysis of data. These methods emphasize objective measurements and the statistical, mathematical, or numerical analysis of data collected through polls, questionnaires, surveys, or by manipulating pre-existing statistical data using computational techniques. 
    
* Objective Measurement: Quantitative methods aim to produce quantifiable and reproducible data, focusing on objectivity and minimizing subjectivity.

* Statistical Analysis: The data collected is typically analyzed using statistical methods to identify patterns, correlations, and causal relationships.

* Structured Data Collection: Methods such as surveys and questionnaires are structured and standardized to ensure consistency and comparability.

* Large Sample Sizes: These methods often involve large sample sizes to ensure that the results are generalizable to the broader population.

* Hypothesis Testing: Quantitative research often begins with a hypothesis that is tested through data collection and analysis to determine whether it can be supported or refuted.

* Use of Tools and Software: Advanced tools and software are frequently used for data analysis, including SPSS, SAS, R, and Excel.


    #""", unsafe_allow_html=True)

st.markdown("""
### 👨‍🎓 QUANTITAIVE METHODS



##### 👨‍🔧 More Content

   HISTORY, PURPOSE AND USAGE
The Streamlit Web App is a dynamic platform designed to explore and apply machine learning techniques within the realm of quality management. Its primary goal is to showcase the transformative capabilities of machine learning across various industries, emphasizing their practical applications in enhancing product quality and optimizing operational efficiency. 
            The app encompasses a wide array of machine learning methodologies tailored specifically for quality management. These include supervised learning techniques such as regression and classification, which enable predictive modeling for quality assurance processes. Additionally, it features unsupervised learning methods like clustering and anomaly detection,
             invaluable for uncovering hidden patterns and anomalies within manufacturing data. Reinforcement learning principles are also employed to refine decision-making processes through continuous learning and adaptive feedback mechanisms.

Each machine learning technique showcased within the Streamlit Web App is accompanied by real-world use cases, illustrating their impact on reducing defects, optimizing production processes, and ensuring compliance with industry standards. Through interactive visualizations and data-driven insights, users can explore model outputs and analytics,
             gaining deeper understanding into complex relationships and actionable trends. Beyond its practical applications, the app serves as an educational resource hub, offering tutorials, explanatory articles, and best practices tailored for quality management professionals. These resources empower users to not only implement machine learning 
            solutions effectively but also deepen their understanding of the underlying principles driving quality assurance strategies.

### 🔎 Overview""", unsafe_allow_html=True)


st.image("./p3.jpg")


st.markdown("""
Machine learning has led to significant advancements across different fields, transforming how businesses tackle complex problems. By using machine learning algorithms, organizations can quickly and accurately analyze large amounts of data to uncover valuable insights. This technology has empowered industries like healthcare, finance, and manufacturing to improve their processes,
             cut costs, and enhance customer satisfaction. Techniques such as deep learning and natural language processing continue to expand what's possible. The ongoing development of machine learning tools has made advanced data analysis more accessible, driving innovation and digital transformation worldwide. As more businesses adopt machine learning, 
            it reshapes technology and business strategies, moving towards a future where smart automation and data-driven decisions are key to success.
            
### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
