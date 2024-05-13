import streamlit as st
import pdfplumber
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from heapq import nlargest
import nltk

# Download NLTK resources (run only once)
nltk.download('punkt')
nltk.download('stopwords')

def read_pdf_with_pdfplumber(file_path):
    text = 'hellow world'
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def summarize_text(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text.lower())  # Tokenize words correctly

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words and word.isalnum()]  # Include only alphanumeric words

    # Calculate word frequency
    freq_dist = FreqDist(filtered_words)

    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Calculate sentence scores based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in freq_dist:
                if len(sentence.split(' ')) < 40:  # Limiting sentence length to 30 words
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = freq_dist[word]
                    else:
                        sentence_scores[sentence] += freq_dist[word]
    
    # Get top N sentences with highest scores
    summary_sentences = nlargest(10, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    
    return summary


st.title('PDF Summarizer using NLTK')

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Read text from the uploaded PDF file
    with st.spinner('Reading PDF...'):
        text = read_pdf_with_pdfplumber(uploaded_file)
        st.success('PDF reading complete!')
    
    # Summarize the extracted text using NLTK
    with st.spinner('Generating summary...'):
        summary_text = summarize_text(text)
        st.success('Summary generation complete!')
    
    st.subheader('Generated Summary')
    st.write(summary_text)

if __name__ == '__main__':
    st.write('\n\n')