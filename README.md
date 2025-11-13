# 🚀 PlagioSleuth – Text File Plagiarism Checker

PlagioSleuth is a **Streamlit-based plagiarism detection tool** that compares multiple text files and identifies similarity levels using **TF-IDF** and **Cosine Similarity**.  
With a clean and interactive UI, users can upload `.txt` documents and instantly receive plagiarism results.

---

## 📌 How It Works

PlagioSleuth uses two core techniques:

### 🔹 TF-IDF (Term Frequency–Inverse Document Frequency)
Converts each text file into a weighted numerical vector based on word importance.

### 🔹 Cosine Similarity
Measures similarity between document vectors.  
Higher score → greater similarity → higher chance of plagiarism.

---

## 📥 Getting Started
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Nikhil-Netha04/PlagioSleuth-Using-Cosine-Similarity
cd PlagioSleuth-Using-Cosine-Similarity
## Dependencies

Before running the application, ensure you have Python installed on your machine. You will need to install the required dependencies. To do this, navigate to the project directory and run the following command:
```bash
 pip install -r req.txt
```

## Running the App
To run PlagioSleuth, place your text documents (with the .txt extension) in the project directory. Then, execute the following command:

```bash
cd PlagioSleuth-Using-Cosine-Similarity
streamlit run app.py 
```

## Output Examples

```bash
All Plagiarism Results:
Files: b.txt and c.txt - Plagiarism Percentage: 28.20%
Files: a.txt and c.txt - Plagiarism Percentage: 37.86%
Files: a.txt and b.txt - Plagiarism Percentage: 41.71%

Most Plagiarized Files:
Files: a.txt and b.txt - Plagiarism Percentage: 41.71%

Least Plagiarized Files:
Files: b.txt and c.txt - Plagiarism Percentage: 28.20%
```

## Features
Detects plagiarism in multiple text documents.
Outputs plagiarism percentages for each document pair.
Highlights the most and least plagiarized files for easy identification.

## Explore It
Feel free to explore and modify PlagioSleuth to fit your specific use case. For any questions or suggestions, you can reach me at nikhilsa562@gmail.com.

## Issues
If you encounter any issues while using PlagioSleuth, please open an issue on the GitHub repository. Your feedback is valuable for improving the tool.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
