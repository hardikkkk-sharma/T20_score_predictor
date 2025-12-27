🏏 T20 SCORE PREDICTOR

A machine learning web application that predicts the final score of a T20 cricket match based on the current match situation using historical ball-by-ball data.



📖 Overview

Predicting a T20 match’s final score in real time is a challenging problem due to rapidly changing match dynamics such as wickets, run rate, and overs remaining.
This project addresses that challenge by training a Random Forest regression model on historical T20 ball-by-ball data and deploying it through an interactive Streamlit web application.

The model uses the current state of the match to estimate the most likely final score.



🎯 Key Features

1) Real-time final score prediction for T20 matches
2) Machine learning model trained on ball-by-ball data
3) Feature engineering to capture match context
4) Interactive and easy-to-use Streamlit interface
5) Clean and reproducible ML workflow


🧠 Machine Learning Approach

Problem Type: Regression
Algorithm Used: Random Forest Regressor
Target Variable: Final match score
Input Features
1) Batting team
2) Bowling team
3) Match city (venue)
4) Current score
5) Balls remaining
6) Wickets remaining
7) Current Run Rate (CRR)

The model learns non-linear relationships between these features to make realistic score predictions.


🛠 Tech Stack
Python
Pandas & NumPy – data processing
Scikit-learn – model training and evaluation
Streamlit – web application


⚠️ Model File Notice

The trained model file (rf_score_model.pkl) is not included in the repository due to GitHub file size limitations.

To generate the model locally:
Run data-extraction.ipynb
Run feature-extraction.ipynb
Save the trained model as rf_score_model.pkl

▶️ How to Run the Application Locally
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Start the Streamlit app
python -m streamlit run app.py

3️⃣ Open in browser
http://localhost:8501



📊 Model Evaluation
The model was evaluated using standard regression metrics such as:
Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)

These metrics ensure the predictions remain realistic and consistent with real match outcomes.


📈 Learning Outcomes
Built an end-to-end machine learning pipeline
Performed feature engineering on sports data
Trained and evaluated a regression model
Deployed an ML model using Streamlit
Gained experience handling real-world data limitations


🔮 Future Improvements
Add confidence intervals to predictions
Support second-innings chase prediction
Improve UI with visualizations
Deploy the app publicly (Streamlit Cloud / Hugging Face)


👤 Author
Hardik Sharma
Linkedin - https://www.linkedin.com/in/hardik-sharma-732557334/
B.Tech – Computer Science & Engineering (AI & ML)
Manipal University jaipur
