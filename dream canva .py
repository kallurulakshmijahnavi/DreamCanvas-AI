import streamlit as st
import base64

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="DreamCanvas AI",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# BACKGROUND IMAGE
# ---------------------------------------------------

def set_background(image_file):

    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    background = f"""
    <style>

    .stApp {{
        background-image:
        linear-gradient(
            rgba(255, 240, 248, 0.88),
            rgba(235, 225, 255, 0.88)
        ),
        url("data:image/jpeg;base64,{encoded}");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    </style>
    """

    st.markdown(background, unsafe_allow_html=True)


try:
    set_background("images/painting.jpg")
except:
    pass


# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

    /* Main page */

    .main {
        padding-top: 1rem;
    }

    /* Title */

    .main-title {
        text-align: center;
        font-size: 52px;
        font-weight: 800;
        margin-bottom: 0px;

        background: linear-gradient(
            90deg,
            #8e44ad,
            #e84393,
            #6c5ce7,
            #0984e3
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #5d536b;
        margin-bottom: 25px;
    }


    /* Welcome card */

    .welcome-card {

        padding: 30px;
        border-radius: 25px;

        background: rgba(255,255,255,0.72);

        box-shadow:
            0px 10px 35px rgba(90,60,120,0.18);

        backdrop-filter: blur(12px);

        text-align: center;

        margin-bottom: 25px;
    }


    .welcome-card h2 {
        color: #6c3483;
    }

    .welcome-card p {
        color: #5f5368;
        font-size: 17px;
    }


    /* Feature cards */

    .feature-card {

        padding: 20px;

        border-radius: 20px;

        background: rgba(255,255,255,0.75);

        box-shadow:
        0px 5px 20px rgba(80,50,100,0.15);

        text-align: center;

        min-height: 145px;
    }

    .feature-card h3 {
        color: #7d3c98;
    }

    .feature-card p {
        color: #62566b;
    }


    /* Chat container */

    .chat-box {

        padding: 20px;

        border-radius: 20px;

        background: rgba(255,255,255,0.70);

        box-shadow:
        0px 5px 25px rgba(80,50,100,0.15);

        margin-top: 20px;
    }


    /* Sidebar */

    [data-testid="stSidebar"] {

        background:
        linear-gradient(
            180deg,
            #eadcff,
            #ffe1ef,
            #e2f0ff
        );

    }


    /* Buttons */

    .stButton > button {

        border-radius: 15px;

        border: none;

        background:
        linear-gradient(
            90deg,
            #a569bd,
            #e84393
        );

        color: white;

        font-weight: 600;

        padding: 10px 18px;

        transition: 0.3s;
    }

    .stButton > button:hover {

        transform: scale(1.04);

        box-shadow:
        0px 5px 15px rgba(200,80,150,0.3);
    }


    /* Chat input */

    .stChatInput {

        border-radius: 20px;
    }


    /* Footer */

    .footer {

        text-align: center;

        color: #716579;

        margin-top: 40px;

        padding: 20px;
    }

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:

    st.markdown("## 🎨 DreamCanvas AI")

    st.write("Your creative AI companion ✨")

    st.divider()

    st.markdown("### 🧩 Choose Mode")

    mode = st.selectbox(
        "Select what you want to do",
        [
            "🤖 General AI",
            "📚 Study Mode",
            "💻 Coding Mode",
            "✍️ Writing Mode",
            "🧠 Quiz Mode",
            "🎨 Creative Mode"
        ]
    )

    st.divider()

    st.markdown("### ⚡ Quick Actions")

    if st.button("📚 Explain a Topic"):
        st.session_state.messages.append({
            "role": "user",
            "content": "Explain a difficult topic in simple words."
        })

    if st.button("💡 Give me an Idea"):
        st.session_state.messages.append({
            "role": "user",
            "content": "Give me a unique project idea."
        })

    if st.button("💻 Help with Code"):
        st.session_state.messages.append({
            "role": "user",
            "content": "Help me understand Python code."
        })

    if st.button("🧠 Start Quiz"):
        st.session_state.messages.append({
            "role": "user",
            "content": "Start a simple quiz for me."
        })

    st.divider()

    uploaded_file = st.file_uploader(
        "📎 Upload an image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:

        st.image(
            uploaded_file,
            caption="Your uploaded image"
        )

    st.divider()

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()


# ---------------------------------------------------
# MAIN TITLE
# ---------------------------------------------------

st.markdown(
    '<div class="main-title">🎨 DreamCanvas AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Learn • Create • Explore • Imagine ✨'
    '</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------
# WELCOME CARD
# ---------------------------------------------------

st.markdown("""
<div class="welcome-card">

<h2>✨ Welcome to your AI Canvas</h2>

<p>
Turn your questions, ideas and imagination into something amazing.
Choose a mode and start creating!
</p>

</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# FEATURE CARDS
# ---------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown("""
    <div class="feature-card">

    <h3>📚 Learn</h3>

    <p>
    Understand difficult topics
    with simple explanations.
    </p>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="feature-card">

    <h3>💻 Code</h3>

    <p>
    Learn programming and
    solve coding problems.
    </p>

    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown("""
    <div class="feature-card">

    <h3>✍️ Create</h3>

    <p>
    Generate ideas, stories,
    projects and content.
    </p>

    </div>
    """, unsafe_allow_html=True)


with col4:

    st.markdown("""
    <div class="feature-card">

    <h3>🧠 Explore</h3>

    <p>
    Ask questions and discover
    new possibilities.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------
# CURRENT MODE
# ---------------------------------------------------

st.markdown("### 🌟 Current Mode")

st.info(
    f"You are currently using **{mode}**"
)


# ---------------------------------------------------
# CHAT HISTORY
# ---------------------------------------------------

st.markdown(
    '<div class="chat-box">',
    unsafe_allow_html=True
)

if len(st.session_state.messages) == 0:

    st.markdown("""
    ### 👋 Hello!

    I'm **DreamCanvas AI**.

    Try asking me something like:

    - 📚 Explain machine learning
    - 💻 Write a Python program
    - 💡 Give me an AI project idea
    - ✍️ Write a short story
    - 🧠 Start a quiz
    """)


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------
# CHAT INPUT
# ---------------------------------------------------

question = st.chat_input(
    "💬 Ask DreamCanvas AI anything..."
)


if question:

    # Add user message

    st.session_state.messages.append({

        "role": "user",

        "content": question

    })


    # Display user message

    with st.chat_message("user"):

        st.markdown(question)


    # Simple demo response

    response = f"""
### ✨ DreamCanvas AI

You selected **{mode}**.

You asked:

> {question}

This is the **demo version** of DreamCanvas AI.

You can connect this interface to:

- 🤖 Ollama
- 🧠 Llama
- 🔥 Gemini
- 🌐 OpenAI API
- ⚡ Other AI APIs

to generate real AI responses.
"""


    st.session_state.messages.append({

        "role": "assistant",

        "content": response

    })


    with st.chat_message("assistant"):

        st.markdown(response)


# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
<div class="footer">

🎨 <b>DreamCanvas AI</b>

<br>

Built with Python + Streamlit

<br>

✨ Your ideas are the beginning of something amazing.

</div>
""", unsafe_allow_html=True)