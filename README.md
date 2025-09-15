# End-to-End ML Deployment with Automated CI/CD  
**Project:** Iris Species Prediction Web App  

## 💡 Objective  
Build and deploy a scalable machine learning web application using **Flask** and **Docker**, with a fully automated CI/CD pipeline powered by **GitHub Actions** and hosted on **Heroku**.  

---

## 🔧 Tech Stack  
- **Model Training:** scikit-learn (K-Nearest Neighbors, KNN)  
- **Scaler:** StandardScaler (joblib serialization)  
- **Web App:** Flask  
- **Containerization:** Docker  
- **CI/CD:** GitHub Actions  
- **Hosting Platform:** Heroku  
- **Web Server:** Gunicorn  

---

# Software And Tools Requirements

1. [Github Account](https://github.com)
2. [Heroku Account](https://heroku.com)
3. [VS Code IDE](https://code.visualstudio.com/)
4. [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

---

## 🧠 Architecture Flow  
User → Flask frontend → Preprocessing (Scaler) → KNN Model → Prediction
→ Docker Container → GitHub → GitHub Actions → Heroku Deploy

---

## 📂 Key Components  

| File | Purpose |
|------|---------|
| `model.pkl` | Trained KNN model |
| `scaler.pkl` | StandardScaler object for preprocessing |
| `app.py` | Flask app backend |
| `templates/home.html` | Frontend UI |
| `Dockerfile` | Defines Docker image setup |
| `requirements.txt` | Python dependencies |
| `Procfile` | Heroku process type definition |
| `.github/workflows/deploy.yml` | GitHub Actions CI/CD pipeline |

---

## ⚡ CI/CD with GitHub Actions  
On every push/merge to `main`, GitHub Actions automatically:  
1. Built the Docker image  
2. Logged into Heroku’s container registry  
3. Pushed & released the Docker image to Heroku  

✅ No manual deployment → faster updates → safer workflows.  
(*Note: requires `HEROKU_API_KEY`)  

---

## 🚀 How to Run Locally  

1. Clone the repo:  
   ```bash
   git clone https://github.com/LogicLoom-hash/End-to-End-ML-implementation.git
   cd End-to-End-ML-implementation
   
Install dependencies:
pip install -r requirements.txt

Run Flask app:
python app.py

Or, build & run with Docker:
docker build -t iris-ml-app.
docker run -p 5000:5000 iris-ml-app
Open browser at: http://localhost:5000   
