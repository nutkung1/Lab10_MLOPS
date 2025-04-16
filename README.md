🏠 Housing Price Predictor API
A simple Flask-based machine learning API that predicts housing prices using a regression model trained on a housing dataset.

📦 Project Description
This project demonstrates how to:

Train a regression model to predict housing prices

Serve the model using a Flask API

Dockerize the API for easy deployment

Validate and handle inputs

Return prediction results in JSON format

⚙️ Setup Instructions
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/yourusername/housing-price-predictor.git
cd housing-app
2. Prepare your environment
Install Python packages:

bash
Copy
Edit
pip install -r requirements.txt
3. Run the app locally
bash
Copy
Edit
python house_app.py
4. Or use Docker
bash
Copy
Edit
docker build -t housing-app .
docker run -p 9000:9000 housing-app
🚀 API Usage
🔹 POST /predict
Request:

json
Copy
Edit
{
  "features": [
    [7420, 3, 2, 3, 1, 1, 0, 1, 0, 1, 2, 0, 1],
    [8960, 4, 2, 2, 1, 0, 0, 0, 0, 1, 1, 1, 2]
  ]
}
Note: The feature array corresponds to:
[area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, parking, prefarea, furnishingstatus]

Response:

json
Copy
Edit
{
  "predictions": [4750000.0, 3850000.0]
}
📁 File Structure
bash
Copy
Edit
housing-app/
├── house_app.py           # Flask app
├── model.pkl              # Trained regression model
├── Dockerfile             # Docker config
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
