import streamlit as st

st.title("About Me 👩‍❤️‍")



st.title("🖼️Self Portrait")


image_paths = ["pictures/kyla.jpg"]


cols = st.columns(len(image_paths))

for col, image_path in zip(cols, image_paths):
    col.image(image_path)


st.header(" ♀👸 Broñola , Kyla May Guevarra")

st.markdown("""
#####  ♡∞  Family Members ♡∞ 

* 👩‍👦 Mother's Name: Elaine G. Broñola
* 👨‍👧‍👧 Father's Name: Roland G. Broñola
* 👭🏻 Sister's Name: Katrina G. Broñola
* 💪 Sister's Name: Justin G. Broñola           

### 🔎 Overview
""", unsafe_allow_html=True)

# Personal Information
st.header("Personal Information")
st.write("**Name:** Kyla May G. Broñola")
st.write("**Age:** 21 years old")
st.write("**Education:** Currently studying at CARLOS HILADO MEMORIAL STATE UNIVERSITY")
st.write("**Year:** 3rd year Bachelor of Science in Information Systems Student")
st.write("**Location:** Purok Cabay Bodega Brgy. 5, Silay City, Negros Occidental")

with st.expander("Who am I 10 years From now??"):
    st.markdown("""
    
    #
                 "Envisioning 2034: My Journey of Growth and Fulfillment"
In 10 years, I see myself as a successful professional in Information Systems, using what I learned in my college years. I want to lead teams and projects at a well-respected company, 
                where I can help shape the future of tech solutions. I'm interested in areas like cybersecurity, building software, or data analysis, using new technologies to solve big problems.
                 As a leader, I want to create a team environment that encourages new ideas and working together, driving important plans that keep the company ahead of the competition. 
                I'm committed to always learning new things, staying up-to-date on the latest tech trends and best practices, so I can make a real difference to the company's success and contribute to the tech world as a whole.

I want to be a leader in the field of information technology (IT). But I also want to give back by helping others learn and grow. I've learned a lot in my own journey, and I want to inspire and guide new people, 
                especially those from groups not well-represented in tech, to join the industry. I also want to keep learning beyond my bachelor's degree, maybe by getting a master's degree or special training in specific IT areas. 
                Whether it's analyzing data or figuring out how to use technology to change things for the better, I'm committed to staying up-to-date and adapting as the tech world changes.

Finally, I want to find a healthy balance between my work goals, personal interests, and supporting my family, especially my parents. Outside of work, I want to stay active and involved in things that make me feel good, like fitness, travel, and helping others. 
                By taking care of myself in all these ways, I can stay creative, bounce back from challenges, and keep making a positive difference, both at work, in my personal life, and for my family, for the next ten years and beyond.
    """, unsafe_allow_html=True)

# Quotes
st.header("Favorite Quotes")
st.write("1. *\"Place your trust in God, remain steadfast in your faith, believe in His divine plan, and stay loyal to His teachings with unwavering devotion.\"*")
st.write("2. *\"Passion is the fuel that drives success.\"*")
st.write("3. *\"Family is not an important thing, it's everything.\"*")
st.write("4. *\"Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.\"*")
st.write("5. *\"There are no secrets to success. It is the result of preparation, hard work, and learning from failure.\"*")






# images = [
#     {"path": "./pic/us1.jpg", "caption": "Academic years are often described as some of the most formative and challenging times in a person's life. The journey through education is filled with hurdles, demanding tasks, and moments of self-doubt. However, amidst the pressures of exams, projects, and deadlines, the presence of supportive friends and classmates plays an important role in not only making the experience bearable but also enriching and enjoyable.From the very first day of school, friendships begin to form. These bonds, initially built on shared classes and common interests, soon evolve into deeper relationships that provide a reliable support system. Friends and classmates become a source of encouragement, helping each other navigate through the hardship of academic life. Whether it's offering a listening ear after a tough day, sharing notes for a missed lecture, or providing motivation before a big exam, their presence is invaluable."},
#     {"path": "./pic/us2.jpg", "caption": "Having close friends around you is incredibly valuable. They offer emotional support, understanding, and companionship through life's challenges and joys. These relationships give you a sense of belonging and help you feel stable and secure. Close friends listen to you without judging, comfort you in tough times, and celebrate your successes, making life more enjoyable and meaningful. Their constant presence and empathy help you face difficulties with confidence, ensuring you never feel alone."},
#     {"path": "./pic/us3.jpg", "caption": "Having supportive friends and classmates during my academic years has been essential for my success and enjoyment in school. Their encouragement, inspiration, and companionship have turned what could have been daunting challenges into opportunities for personal growth and fun. As I navigate through my studies, the bonds I've formed with my peers give me the strength, motivation, and joy I need to keep pushing forward and excel. These relationships are not just crucial for my academic achievements; they also help shape me into a more well-rounded, resilient, and compassionate individual ready to contribute to society."}
# ]


# st.title("🖼️Gallery")


# for image in images:
#     st.image(image["path"], caption=image["caption"])



st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        padding: 2em;
    }
    h1, h2 {
        color: #9A3B3B;
    }
    .stText {
        font-size: 1.5em;
        color: #072227;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer or additional sections (optional)
st.write("### Thank you for visiting my profile!")
st.write("Feel free to connect and reach out if you share similar interests or have any questions.")