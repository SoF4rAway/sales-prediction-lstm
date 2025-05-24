# 📈 Sales Prediction App using LSTM

This project was developed as part of the **Praktik Kerja Lapangan (PKL)** during my undergraduate studies. It is a time series forecasting application designed to predict product sales over a specified period using an **LSTM (Long Short-Term Memory)** model. The model and app are tailored specifically to the dataset provided by the company where the internship was conducted.

## 📌 Abstract

In the business world, forecasting sales demand is a critical component of decision-making. One effective method for predicting sales demand is time series forecasting. This project uses the **LSTM (Long Short-Term Memory)** method to build a predictive model based on historical sales data. The results show that the LSTM model can effectively forecast future sales demand, which can help decision-makers make more accurate and timely business decisions.

**Keywords**: LSTM, Time Series Forecasting, Sales Demand

## ⚙️ Features

- Predict future sales for selected products
- Based on historical sales data using LSTM neural network
- Visualizations of past and predicted sales

## 📉 Model

The model used in this project is an LSTM-based neural network trained on time series data. It is specifically designed for univariate forecasting using the number of units sold.

## 🔒 Application Constraints

There are several important limitations in this application that affect both prediction accuracy and overall app performance:

1. **⚠️Limited Product Scope**: Predictions are available only for **3 selected products**.
2. **⚠️Short Historical Window**: The model is trained on **5 months of sales data** from the year **2021**.
3. **⚠️Single-variable Input**: The model only considers **sales volume**; it does **not** account for factors such as price or promotions.

## 🏗️ Tech Stack

- **Python**
- **TensorFlow / Keras** (LSTM Model)
- **Pandas / NumPy** (Data Processing)
- **Matplotlib / Seaborn** (Visualization)
- **Plotly** (Visualization)
- **Flask** (Web-based dashboard)

## 🚀 How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/sales-prediction-lstm.git
   cd sales-prediction-lstm
   ```

2. Create Python Virtual Environment

   You can create a virtual environment using either **Python's built-in tools** or **Anaconda**. While using plain Python is possible, Anaconda is recommended for easier environment and dependency management, especially across multiple projects.

   - **Option 1 : Using Python (Not Recommended)**

     Make sure python is installed. Then create and activate the virtual environment

     ```bash
     python -m /path/to/new/virtual/environment
     source <venv>/bin/activate
     ```

     Install Required packages:

     ```bash
     pip install -r requirements.txt
     ```

     > 📌 Due to OS-specific differences, please refer to the [official python documentation](https://docs.python.org/3/library/venv.html) regarding VENV

   - **Option 2 : Using Anaconda (Recommended)**

     Make sure Anaconda is installed. Then run this from the project root directory

     ```bash
     conda env create -f environment.yml
     ```

     Then activate it:

     ```bash
     conda activate sales-pred
     ```

3. Run the APP

   To run the app:

   ```bash
   python main.py
   ```

   Then open your browser go to:

   `127.0.0.1:5000`

## 🐞 Known issue

- Prediction is result is unusable when used against other data
- Only supports univariate analysis

## 🔮 Future Improvement

- Train against larger datasets
- Use multivariate analysis for better result and performance
- Improve front-end UI/UX
- Add export feature
- Integrate it with real-time data

## Credits

- **Developed by** : [Muhammad Farid Rahman](https://www.linkedin.com/in/muhammad-farid-952795217/) ([SoF4rAway](github.com/sof4raway))
- **Internship hosted by** : `PT. Kimia Farma Tbk.`
- **Dataset provided by** : `PT. Kimia Farma Tbk. / Unit Umum dan IT (Divisi Big Data Management)`

> Special thanks to **mentors** and **supervisors** involved on the Internship program
