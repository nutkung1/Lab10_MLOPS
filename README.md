# 🏠 Housing Price Predictor API

A simple Flask-based machine learning API that predicts housing prices based on various features like area, number of bedrooms, bathrooms, and more. The model is trained using a dataset of housing properties and deployed via Docker.

---

## 🚀 Features

- Predict house price using regression
- Supports multiple input requests
- Input validation with helpful error messages
- Dockerized for easy deployment

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/housing-price-predictor.git
cd housing-price-predictor
```

### 2. Train the Model (if not already trained)
```bash
python train_model.py
```
This will generate a model.pkl file.

### 3. Run the Flask App
```bash
python house_app.py
```
Or run using Docker:

```bash
docker build -t housing-price-predictor .
docker run -p 9000:9000 housing-price-predictor
```
