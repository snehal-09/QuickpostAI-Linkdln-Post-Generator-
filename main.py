import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# ✅ Set page config only once at the start
st.set_page_config(page_title="QuickPost AI", page_icon="🚀", layout="wide")

# Options
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

# ---------------- Home Page ---------------- #
def home():
    # Gradient header
    st.markdown(
        """
       <div style="background: linear-gradient(to right, #6a11cb, #2575fc);
            padding: 15px 20px; border-radius: 12px; text-align: center;">
    <h1 style="color: white; margin: 0; font-size: 28px;">🚀 QuickPost AI</h1>
    <p style="color: #f1f1f1; font-size: 16px; margin-top: 3px;">
        Your intelligent assistant for creating impactful LinkedIn content in seconds
    </p>
</div>

        """,
        unsafe_allow_html=True,
    )

    st.write("")  # spacing

    # Load tags
    fs = FewShotPosts()
    tags = fs.get_tags()

    # Input cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 📌 Topic")
        selected_tag = st.selectbox("", options=tags, label_visibility="collapsed")

    with col2:
        st.markdown("### 📏 Post Length")
        selected_length = st.radio("", options=length_options, horizontal=True, label_visibility="collapsed")

    with col3:
        st.markdown("### 🌐 Language")
        selected_language = st.radio("", options=language_options, horizontal=True, label_visibility="collapsed")

    st.write("---")

    # Generate button (centered)
    col_empty1, col_center, col_empty2 = st.columns([2, 1, 2])
    with col_center:
        generate_btn = st.button("✨ Generate Post", use_container_width=True)

    st.write("")

    # Output area
    if generate_btn:
        with st.spinner("Crafting your post... ⏳"):
            post = generate_post(selected_length, selected_language, selected_tag)

        st.markdown("## 🎉 Your Generated Post")
        st.markdown(
            f"""
            <div style="background-color: #ffffff;
                        padding: 20px;
                        border-radius: 12px;
                        border: 1px solid rgba(230, 230, 230, 0.5);
                        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
                        font-size: 16px;
                        line-height: 1.6;
                        color: #000000;">
                {post}
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Download option
        st.download_button(
            label="📥 Download Post as .txt",
            data=post,
            file_name="linkedin_post.txt",
            mime="text/plain",
        )

# ---------------- About Page ---------------- #
def about():
    st.markdown(
        """
        <div style="background: linear-gradient(to right, #ff416c, #ff4b2b);
            padding: 15px; border-radius: 12px; text-align: center;">
            <h1 style="color: white; margin: 0; font-size: 28px;">👤 About Me</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.markdown(
        """
        ### Hi, I'm **Snehal** 👋  

        💡 I am currently pursuing **IT Engineering**, but my true passion lies in **Data Science and Artificial Intelligence**.  
        I am deeply interested in understanding patterns in data and building AI solutions that can make everyday tasks smarter and more efficient.  

        🚀 I enjoy creating **AI-powered applications** that solve real-world problems, automate processes, and provide meaningful insights.  
        Working on projects that combine creativity with technical skills excites me, and I continuously strive to apply my knowledge in practical ways.  

        ### 📬 Contact Details  
        - 📧 **Email:** snehalpsalve09@gmail.com  
        - 🔗 **LinkedIn:** [Snehal salve](https://www.linkedin.com/in/snehal-salve-b83a74293/)  
        - 📱 **Phone:** +91-7821881248  

        ### 🌟 About This Project  
        **QuickPost AI** is not just another LinkedIn post generator — it’s a reflection of my journey as a creator who believes technology should make life simpler and more meaningful.  

        I observed that many professionals, students, and entrepreneurs often hesitate to post on LinkedIn because of two common struggles:  

        1. **Finding the right words** to express their thoughts.  
        2. **Investing too much time** in polishing their content to look professional.  

        QuickPost AI was born to solve exactly this. Instead of staring at a blank screen, users can now convert an idea into a professional, well-structured LinkedIn post in just a few seconds. The tool understands **tone, style, and length preferences**, giving flexibility to create content that is either short and catchy, or long and insightful.  

        But beyond speed, the real purpose of QuickPost AI is to **empower voices**. Everyone has stories, insights, or knowledge worth sharing, but not everyone is confident in writing. With this tool, I aim to remove that barrier — enabling more people to express themselves, grow their network, and strengthen their personal brand without worrying about writing skills.  

        For me, QuickPost AI is more than a coding project — it’s a step toward making **AI a creative partner** rather than just a technical tool.
        """,
        unsafe_allow_html=True,
    )

# ---------------- Main Function ---------------- #
def main():
    # Sidebar Navigation
    st.sidebar.title("📍 Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About"])

    if page == "Home":
        home()
    elif page == "About":
        about()

# ---------------- Run App ---------------- #
if __name__ == "__main__":
    main()
