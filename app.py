import streamlit as st
import pickle
import re
import nltk

nltk.download('punkt')
nltk.download('stopwords')

# Load pre-trained model and TF-IDF vectorizer (ensure these are saved earlier)
clf = pickle.load(open('clf.pkl', 'rb'))  # Example file name, adjust as needed
tfidf = pickle.load(open('tfidf.pkl', 'rb'))  # Example file name, adjust as needed
#le = pickle.load(open('encoder.pkl', 'rb'))  # Example file name, adjust as needed


def cleanResume(text):
    text = re.sub(r'http\S+', '', text)                            # Remove URLs
    text = re.sub(r'RT|cc', '', text)                              # Remove RT and cc
    text = re.sub(r'#\S+', '', text)                               # Remove hashtags
    text = re.sub(r'@\S+', '', text)                               # Remove mentions
    text = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', text)  # Remove punctuation
    text = re.sub(r'[^\x00-\x7f]', '', text)                       # Remove non-ASCII characters
    text = re.sub(r'\s+', ' ', text)                               # Collapse multiple spaces/newlines/tabs
    text = text.strip()                                            # Remove leading/trailing whitespace
    return text


#web app
def main():
    st.title("Resume Screening App")
    upload_file = st.file_uploader('Upload Resume',type=['txt','pdf'])

    if upload_file is not None:
        try:
            resume_bytes = upload_file.read()
            resume_text = resume_bytes.decode('utf-8')

        except UnicodeDecodeError:

            resume_text = resume_bytes.decode('latin-1')

        cleaned_resume = cleanResume(resume_text)
        input_features = tfidf.transform([cleaned_resume])
        prediction_id = clf.predict(input_features)[0]



        category_mapping = {
            6: 'Data Science',
            12: 'HR',
            0: 'Advocate',
            1: 'Arts',
            24: 'Web Designing',
            16: 'Mechanical Engineer',
            22: 'Sales',
            14: 'Health and fitness',
            5: 'Civil Engineer',
            15: 'Java Developer',
            4: 'Business Analyst',
            21: 'SAP Developer',
            2: 'Automation Testing',
            11: 'Electrical Engineering',
            18: 'Operations Manager',
            20: 'Python Developer',
            8: 'DevOps Engineer',
            17: 'Network Security Engineer',
            19: 'PMO',
            7: 'Database',
            13: 'Hadoop',
            10: 'ETL Developer',
            9: 'DotNet Developer',
            3: 'Blockchain',
            23: 'Testing'
        }

        predicted_category = category_mapping.get(prediction_id, 'Unknown')

        st.write("Predicted Catagory: ",predicted_category)







if __name__ == "__main__":
    main()