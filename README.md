# 🎮 Movie Genre Prediction

This project predicts the genre of a movie based on its description using machine learning techniques like TF-IDF vectorization and logistic regression.

## 📁 Dataset Structure

Located in:

```
Downloads/Mahaan_Crystal_Clear_320kbps_isaimini.one/MovieGenrePrediction/Genre Classification Dataset/
```

Files used:
- `train_data.txt`: Contains `ID`, `TITLE`, `GENRE`, `DESCRIPTION`
- `test_data.txt`: Contains `ID`, `TITLE`, `DESCRIPTION`

Delimiter used: `:::`

## 🛠️ Requirements

Install dependencies with:

```bash
pip install pandas scikit-learn
```

## 🚀 How it Works

1. Load the dataset using pandas.
2. Convert the movie descriptions to numerical features using TF-IDF vectorization.
3. Split the data into training and validation sets.
4. Train a logistic regression model with class weights to handle imbalanced genres.
5. Evaluate the model using accuracy and a classification report.
6. Predict genres for the test dataset.

## 🧪 Sample Output

```
Validation Accuracy: 0.8420

Classification Report:
              precision    recall  f1-score   support

     Action       0.85      0.86      0.85       120
     Comedy       0.82      0.80      0.81       100
      Drama       0.85      0.86      0.85       130

    accuracy                           0.84       350
   macro avg       0.84      0.84      0.84       350
weighted avg       0.84      0.84      0.84       350
```

## 📦 Prediction Output Format

```
ID     | TITLE                         | PREDICTED_GENRE
----------------------------------------------------------
101    | The Last Stand                | Action
102    | Funny Side of Life            | Comedy
103    | Through the Fog               | Drama
...
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

