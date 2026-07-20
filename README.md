# ♻️ ClassifAI: Smart Waste Classification System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://classif-ai-a-garbage-classifier-app.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

> **"Turning Trash into Data for a Greener Planet."**

---

## Overview
**ClassifAI** is a state-of-the-art web application powered by **Deep Learning** designed to automate waste segregation. Built with **Streamlit** and **TensorFlow**, it accurately identifies garbage types from images and provides actionable insights on:
* **Material Classification:** (Glass, Plastic, Paper, Metal, Cardboard, Trash)
* **Environmental Impact:** Real-time Carbon Footprint estimates.
* **Sustainability:** Alignment with UN Sustainable Development Goals (SDGs).

Whether for educational purposes or smart recycling centers, ClassifAI makes sustainability smart and simple.

---

## Key Features
* **Real-Time Detection:** Upload images instantly to detect waste types.
* **Advanced AI:** Powered by a fine-tuned **MobileNetV2** (Keras) model for high accuracy.
* **Eco-Insights:** Displays the **Carbon Footprint** (CO₂ emission estimates) for every item detected.
* **SDG Integration:** Maps waste to specific United Nations Sustainable Development Goals.
* **Blazing Fast:** Optimized for low-latency performance on Streamlit Cloud.

---

## Interface Preview

| **Upload & Classify** | **Results & Insights** |
|:---------------------:|:----------------------:|
| ![Upload Screen](https://github.com/NithinGJ2005/CLassifAI/blob/main/assets/Screenshot%202026-01-31%20183621.png?raw=true) | ![Results Screen](https://github.com/NithinGJ2005/CLassifAI/blob/main/assets/Screenshot%202026-01-31%20183720.png?raw=true) |

---

## Tech Stack

| Component | Technology |
| :--- | :--- |
| **Frontend** | [Streamlit](https://streamlit.io/) |
| **Deep Learning** | [TensorFlow](https://www.tensorflow.org/) / [Keras](https://keras.io/) |
| **Image Processing** | [Pillow (PIL)](https://python-pillow.org/) & [NumPy](https://numpy.org/) |
| **Version Control** | Git & GitHub |
| **Deployment** | Streamlit Cloud |

---

## Installation & Local Setup

Follow these steps to run the app on your local machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
```

### 2. Create a Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch the App
```bash
streamlit run app.py
```
The app should open automatically in your browser at http://localhost:8501.

## Usage Guide
1. **Launch the App:** Open the link or run locally.

2. **Upload Image:** Click "Browse Files" to select an image of waste (JPG, PNG).

3. **Click Classify:** Hit the blue "Classify Waste" button.

4. **View Results:** See the predicted category (e.g., Plastic).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* Check the confidence score.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* Read the Carbon Footprint facts and SDG relevance.

## Project Structure
```bash
ClassifAI/
├── artifacts/
│   └── models/
│       └── garbage_classifier.h5  # Trained Deep Learning Model
├── assets/
│   └── sdg/                       # Icons for Sustainable Development Goals
├── data/
│   └── raw/                       # Raw Dataset Images
│       ├── cardboard/
│       ├── glass/
│       ├── metal/
│       ├── paper/
│       ├── plastic/
│       └── trash/
├── app.py                         # Main Application Logic
├── requirements.txt               # Project Dependencies
├── README.md                      # Project Documentation
└── .gitignore                     # Git Ignore File
```

## Contributing
Contributions are always welcome! If you have ideas for new features (like Camera support or Geolocation), feel free to fork the repo.

1. **Fork the repository.**

2. **Create a Branch:** git checkout -b feature/YourFeature

3. **Commit changes:** git commit -m 'Add some AmazingFeature'

4. **Push to branch:** git push origin feature/YourFeature

5. **Open a Pull Request.**

## License
This project is licensed under the MIT License. See the LICENSE file for details.

<div align="center"> <p>Made with ❤️ by <b>Nithin G J</b></p> <p> <a href="https://github.com/NithinGJ2005"> <img src="https://www.google.com/search?q=https://img.shields.io/badge/GitHub-Profile-black%3Fstyle%3Dfor-the-badge%26logo%3Dgithub" alt="GitHub Profile" /> </a> <a href="https://classif-ai-a-garbage-classifier-app.streamlit.app/"> <img src="https://www.google.com/search?q=https://img.shields.io/badge/Live-Demo-FF4B4B%3Fstyle%3Dfor-the-badge%26logo%3Dstreamlit" alt="Live Demo" /> </a> </p> </div>
