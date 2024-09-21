import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

port_stem = PorterStemmer()
vectorization = TfidfVectorizer()

vector_form = pickle.load(open('vector.pkl', 'rb'))
load_model = pickle.load(open('model.pkl', 'rb'))

def stemming(content):
    con = re.sub('[^a-zA-Z]', ' ', content)
    con = con.lower()
    con = con.split()
    con = [port_stem.stem(word) for word in con if not word in stopwords.words('english')]
    con = ' '.join(con)
    return con

def fake_news(news):
    news = stemming(news)
    input_data = [news]
    vector_form1 = vector_form.transform(input_data)
    prediction = load_model.predict(vector_form1)
    return prediction

st.set_page_config(page_title="Fake News Classification", page_icon="📰", layout="wide")

# Custom CSS for styling and background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('fake new copy.jpg');
        background-size: cover;
    }
    .sttitle {
        color: #93CE78;
    }
    .stTextArea label, .stButton button {
        font-weight: bold;
    }
    .stTextArea label, .stMarkdown h1, .stMarkdown h2 {
        color: green;
    }
    .stButton button {
        background-color: blue;
        color: white;
        border: none;
        border-radius: 5px;
        margin-top: 20px;
    }

    .stButton button:hover {
        background-color: #848ee0;
        border-radius: 5px;
        color: blue;
    }
  
    .stButton button:active {
        background-color: darkblue;
        color: white;
    }
    .stTextArea textarea {
        height: 200px;
        background-color: #f0f0f5;
        color: #000000;
    }
    .report-container {
        padding: 20px;
        border-radius: 10px;
        background-color: #f9f9f9;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .centered-button {
        display: flex;
        justify-content: center;
    }
    .text-area-container {
        margin-top: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('📰 Fake News Classification App')
st.subheader("Input the News Content Below")

# Input text area
st.markdown('<div class="text-area-container">', unsafe_allow_html=True)
sentence = st.text_area("Enter your news content here:")
st.markdown('</div>', unsafe_allow_html=True)

# Predict button centered
st.markdown('<div class="centered-button">', unsafe_allow_html=True)
predict_btt = st.button("Predict")
st.markdown('</div>', unsafe_allow_html=True)

if predict_btt:
    if sentence.strip() == "":
        st.warning("Please enter some text before predicting.")
    else:
        prediction_class = fake_news(sentence)
        if prediction_class == [0]:
            st.success('Reliable')
        elif prediction_class == [1]:
            st.error('Unreliable')
