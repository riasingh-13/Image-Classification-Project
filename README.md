# **Image Classification API: Cats vs Dogs**

This repository contains an **API for identifying whether an image contains a cat or a dog**, powered by a pre-trained deep learning model.

---

## **Getting Started**

### **1. Clone the Repository**
```bash
git clone <repository-url>
cd <project-directory>
```

### **2. Set Up a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate   # For Windows
```

### **3. Install Required Packages**
```bash
pip install -r requirements.txt
```

### **4. Launch the API**
```bash
uvicorn app.main:app --reload
```

### **5. Test the API**
* Navigate to: `http://127.0.0.1:8000`
* Endpoint to use: `POST /predict`
* Functionality: Upload an image to the `/predict` endpoint to get a classification result.

---

## **Directory Overview**

```
project-root/
├── api/
│   ├── routes.py       # Defines API endpoints
│   └── schemas.py      # Data models for API responses
├── app/
│   └── main.py         # Main application file for FastAPI
├── core/
│   ├── config.py       # Configuration settings
│   ├── prediction.py   # Functions for image processing and predictions
│   └── training.py     # Script for training the model
├── data/
│   ├── cat/             # Folder for cat images
│   └── dog/             # Folder for dog images
├── models/
│   └── cat_dog_model.h5 # Pre-trained model file
├── uploads/          # Directory for storing uploaded images
├── requirements.txt  # List of dependencies
├── README.md         # Project documentation
└── venv/             # Virtual environment files
```

---

## **Model Information**

* **Library Used:** TensorFlow/Keras  
* **Input Dimensions:** 128x128 pixels  
* **Categories:** Cat, Dog  
* **Training Script Location:** `core/training.py`

### **To Train the Model**
```bash
python core/training.py
```

---

## **Using the API**

### **Making a Request (cURL Example)**
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "accept: application/json" \
-H "Content-Type: multipart/form-data" \
-F "file=@path_to_image.jpg"
```

### **Sample Response**
```json
{
  "file": "cat_2.jpg",
  "result": {
    "prediction": "Cat",
    "confidence": 0.98
  }
}
```

---

## **Contributions**

1. Fork this repository.  
2. Create a branch for your feature:  
   ```bash
   git checkout -b new-feature
   ```
3. Commit your changes:  
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your branch:  
   ```bash
   git push origin new-feature
   ```
5. Open a pull request to merge your changes.

---

## **License Information**

This project is distributed under the **MIT License**.

---

