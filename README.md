# **Cat vs Dog Image Classification API**  

This project provides an **API for classifying images of cats and dogs** using a trained deep-learning model.

---

## **Setup**

### **1. Clone Repository**  
```bash
git clone <repository-url>
cd <project-directory>
```

### **2. Create and Activate Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Run the API**  
```bash
uvicorn app.main:app --reload
```

### **5. Access the API**  
* Open your browser at: `http://127.0.0.1:8000`  
* API Endpoint: `POST /predict`  
* Example Request: Upload an image file to `/predict` to receive a prediction.

---

## **Project Structure**

```
project-root/
│
├── api/
│   ├── routes.py       # API route definitions
│   ├── schemas.py      # API response models
│
├── app/
│   ├── main.py         # Entry point for FastAPI application
│
├── core/
│   ├── config.py       # Configuration settings
│   ├── prediction.py   # Image preprocessing and prediction logic
│   ├── training.py     # Model training script
│
├── data/              # Dataset directory
│   ├── cat/
│   ├── dog/
│
├── models/
│   ├── cat_dog_model.h5 # Trained Keras model
│
├── uploads/           # Stores uploaded test images
│
├── requirements.txt   # Project dependencies
├── README.md          # Documentation
└── venv/              # Virtual environment
```

---

## **Model Details**

* **Framework:** TensorFlow/Keras  
* **Input Size:** 128x128  
* **Classes:** Cat, Dog  
* **Training Script:** `core/training.py`  

### **Run Training Script**  
```bash
python core/training.py
```

---

## **API Example**

### **Request Example (Using cURL)**  
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "accept: application/json" \
-H "Content-Type: multipart/form-data" \
-F "file=@path_to_image.jpg"
```

### **Response Example**  
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

## **Contributing**

* Fork the repository.  
* Create a new branch:  
  ```bash
  git checkout -b feature-branch
  ```
* Make your changes and commit:  
  ```bash
  git commit -m "Your changes"
  ```
* Push to the branch:  
  ```bash
  git push origin feature-branch
  ```
* Create a pull request.

---

## **License**

This project is licensed under the **MIT License**.

---

