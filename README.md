# Enchanted-Wings-Marvels-Of-Butterfly-Species


# 🦋 Butterfly Species Classifier

A Flask web application that uses a trained VGG16 deep learning model to classify butterfly species from uploaded images.

---

## 📁 Project Structure

```

project/
│
├── static/           # Static files (CSS, JS, Images)
├── templates/        # HTML templates
├── vgg16\_butterfly\_model.h5  # ⚠️ NOT INCLUDED – download below
├── app.py            # Flask application
├── requirements.txt  # Python dependencies
└── README.md         # Project description

````

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/mujeebshaik04/butterfly-classifier.git
cd butterfly-classifier
````

### 2. Install requirements

```bash
pip install -r requirements.txt
```

### 3. Download the Trained Model (VGG16)

⚠️ The `.h5` model file is too large to be stored on GitHub.

📥 **Download from Google Drive**:
[Download vgg16\_butterfly\_model.h5](https://drive.google.com/file/d/1UMMDZsszA46wbrMah8b4otEAbgjr-K3M/view?usp=sharing)

📌 Place the downloaded file in the **root of the project folder**.

---

## 🖼️ How It Works

1. User uploads an image of a butterfly.
2. The image is preprocessed and passed to a **VGG16-based model**.
3. The model predicts the butterfly species.
4. The prediction is displayed on the results page.

---

## ▶️ Running the App

```bash
python app.py
```

Then open your browser and go to:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🧠 Model Info

* **Architecture:** VGG16
* **Framework:** TensorFlow / Keras
* **Input size:** 224x224
* **Classes:** Multiple butterfly species
* **Accuracy:** \~90% (test set)

---

## 👩‍💻 Team Information

* **Team ID:** LTVIP2025TMID42176
* **Team Size:** 3
* **Team Leader:** Vanipenta Vidya Reddy
* **Team Members:**

  * Syed Mohammed Siddiq
  * S Supraja

Google Drive Link For Model:
(https://drive.google.com/file/d/1UMMDZsszA46wbrMah8b4otEAbgjr-K3M/view?usp=sharing) 

