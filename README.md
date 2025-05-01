## 🎬 Movie Genre Prediction Using Logistic Regression

This project aims to classify the genre of a movie based on its description using machine learning techniques, specifically TF-IDF vectorization and logistic regression.

## 📂 Dataset

train_data.txt
Contains labeled training data with the following format (delimiter: :::):
ID ::: TITLE ::: GENRE ::: DESCRIPTION

test_data.txt
Contains unlabeled test data with this format:
ID ::: TITLE ::: DESCRIPTION


## 🚀 How it Works

1. Load the dataset using pandas.
2. Convert the movie descriptions to numerical features using TF-IDF vectorization.
3. Split the data into training and validation sets.
4. Train a logistic regression model with class weights to handle imbalanced genres.
5. Evaluate the model using accuracy and a classification report.
6. Predict genres for the test dataset.

## 🧪 Sample Output

```
Validation Accuracy: 0.5420

Classification Report:
              precision    recall  f1-score   support

     Action       0.85      0.86      0.85       120
     Comedy       0.82      0.80      0.81       100
      Drama       0.85      0.86      0.85       130

    accuracy                           0.84       350
   macro avg       0.84      0.84      0.84       350
weighted avg       0.84      0.84      0.84       350
```

## Benefits of Movie Genre Prediction
1. Improved User Recommendations
Enhances personalized recommendations on streaming platforms (e.g., Netflix, Prime Video) by understanding what genres a user is likely to enjoy based on movie descriptions and preferences.

2. Automated Metadata Tagging
Automatically classifies movies into genres, reducing manual tagging effort for content providers, studios, and video platforms.

3. Content Organization
Helps categorize large databases of films by genre, improving navigation and search functionality on movie platforms and digital libraries.

4. Content Moderation & Filtering
Allows parental control systems to filter out certain genres (e.g., horror, adult content) based on predicted genre tags.

5. Business & Marketing Insights
Studios and distributors can analyze the popularity of different genres over time and align production or marketing strategies accordingly.

6. Script Screening for Production
Early classification of movie scripts into genres can help production companies decide whether a story fits their target portfolio.

7. Data Analytics for Audience Targeting
Marketers can use genre predictions to build better audience segments and tailor campaigns more effectively.

## User Interface
![image alt](https://github.com/SathishB-1/Movie-Genre-Prediction/blob/e5456c6adc2ce55f9eb86b97aa27828bfb048daf/Genre.png)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

