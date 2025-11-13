import streamlit as st
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tempfile

st.title("📄 Text File Plagiarism Checker")
st.write("Upload two or more .txt files to check similarity using TF-IDF + Cosine Similarity.")

uploaded_files = st.file_uploader(
    "Upload TXT files",
    type=['txt'],
    accept_multiple_files=True
)

if uploaded_files:
    student_files = []
    student_notes = []

    # Save uploaded files to temp directory
    for file in uploaded_files:
        tpath = os.path.join(tempfile.gettempdir(), file.name)
        with open(tpath, "wb") as f:
            f.write(file.getbuffer())
        student_files.append(file.name)
        student_notes.append(open(tpath, "r", encoding="utf-8").read())

    def vectorize(text):
        return TfidfVectorizer().fit_transform(text).toarray()

    def similarity(doc1, doc2): 
        return cosine_similarity([doc1, doc2])

    # Create vectors
    vectors = vectorize(student_notes)
    s_vectors = list(zip(student_files, vectors))
    plagiarism_results = []

    def check_plagiarism():
        results = []
        for i in range(len(s_vectors)):
            student_a, text_vector_a = s_vectors[i]
            for j in range(i + 1, len(s_vectors)):
                student_b, text_vector_b = s_vectors[j]
                sim_score = similarity(text_vector_a, text_vector_b)[0][1]
                results.append((student_a, student_b, sim_score))
        return results

    plagiarism_results = check_plagiarism()

    if len(plagiarism_results) == 0:
        st.warning("Upload at least 2 text files.")
    else:
        plagiarism_results.sort(key=lambda x: x[2])

        st.subheader("📊 All Plagiarism Results")
        for result in plagiarism_results:
            st.write(
                f"**{result[0]}** ↔ **{result[1]}** — "
                f"Similarity: **{result[2]*100:.2f}%**"
            )

        # Most & Least
        most = plagiarism_results[-1]
        least = plagiarism_results[0]

        st.subheader("🔥 Most Similar Files")
        st.success(
            f"**{most[0]}** ↔ **{most[1]}** — {most[2]*100:.2f}% Plagiarism"
        )

        st.subheader("🧊 Least Similar Files")
        st.info(
            f"**{least[0]}** ↔ **{least[1]}** — {least[2]*100:.2f}% Plagiarism"
        )

        # -----------------------------
        # NEW: Show Plagiarized & Original File
        # -----------------------------
        st.subheader("🏆 Final Result")

        plagiarised_file = most[0]
        original_file = most[1]

        st.write(f"**Most Plagiarised File:** `{plagiarised_file}`")
        st.write(f"**Original File:** `{original_file}`")
