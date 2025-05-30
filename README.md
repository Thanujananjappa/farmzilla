# 🌾 Smart Agri Farming App

A multilingual Smart Agriculture web application that empowers farmers with crop insights, disease detection, AI chatbot support, fertilizer advice, government schemes, and much more.

---
🔗 Live Demo
🌐 Check it out live: [https://your-vercel-link.vercel.app](https://farmzilla.vercel.app/)

## 🧰 Tech Stack

### 👨‍🌾 Frontend
- React + TypeScript
- Tailwind CSS
- Vite
- `react-i18next` for localization

### ⚙️ Backend
- Flask (Python): Disease detection, crop recommendation, chatbot
- Node.js + Express: API gateway / additional routes
- Ollama: LLM-based chatbot (local model like LLaMA 3)

---

## 📁 Project Structure

smart-agri-farming/
├── backend/ # Node + Express server (API gateway or extra logic)
├── chatbot-backend/ # Flask chatbot with Ollama integration
├── crop_recommendation/ # Flask crop recommendation service
├── smartfarm-backend/ # Flask disease detection model
├── src/ # React frontend app
│ ├── locales/ # i18n translation files
│ ├── components/ # All UI components
│ └── ...
├── public/
├── .env # Environment variables
├── index.html
├── index.tsx
├── package.json
├── vite.config.ts

yaml
Copy
Edit

---

## 🌍 Features

- 🗣️ **Multilingual Support** (English, Hindi, Kannada, Tamil, Telugu, Malayalam)
- 🌱 **Crop Recommendation** using soil type and region
- 🦠 **Plant Disease Detection** via image upload (TensorFlow model)
- 🤖 **Chatbot with Ollama LLM**
- 🧪 **Fertilizer Suggestions** for crop-soil combos
- 📈 **Crop Demand Forecast** for local markets
- 💸 **Government Schemes & Loans** information
- 🧑‍🌾 Simple, farmer-friendly UI

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/smart-agri-farming.git
cd smart-agri-farming
🌐 Frontend Setup (React + Vite)
bash
Copy
Edit
# Install dependencies
npm install

# Start the dev server
npm run dev
Make sure you have a .env file in the root:

env
Copy
Edit
VITE_CHATBOT_API_URL=http://localhost:5002
VITE_CROP_RECOMMENDATION_API=http://localhost:5001
VITE_DISEASE_API=http://localhost:5000
🧠 Chatbot Backend (Flask + Ollama)
Prerequisites
Python 3.8+

Ollama installed from https://ollama.com/

Setup
bash
Copy
Edit
cd chatbot-backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Run Ollama model locally (e.g., llama3)
ollama run llama3

# Start Flask server
python app.py  # Runs on http://localhost:5002
🌾 Crop Recommendation Backend (Flask)
bash
Copy
Edit
cd crop_recommendation
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py  # Runs on http://localhost:5001
🧬 Disease Detection Backend (Flask + TensorFlow)
bash
Copy
Edit
cd smartfarm-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py  # Runs on http://localhost:5000
🌐 Node + Express Backend (Optional)
bash
Copy
Edit
cd backend
npm install
node index.js  # Customize your port or middleware if needed
🌍 Multilingual Setup
react-i18next is used for localization.

Supported Languages
English

Hindi

Kannada

Tamil

Telugu

Malayalam

Switch Languages
In the UI, use language buttons or a dropdown. Translations are stored in:

pgsql
Copy
Edit
src/locales/
  ├── en.json
  ├── hi.json
  ├── kn.json
  ├── ta.json
  ├── te.json
  └── ml.json
🧪 Image Upload – Disease Detection
Upload a plant leaf photo → the TensorFlow model predicts the disease.

API: http://localhost:5000/predict

🤖 Chatbot with Ollama
Local LLMs (e.g., LLaMA3, Mistral) are run via Ollama.

Questions can be asked in regional languages.

Translations handled via frontend and processed by Ollama.

📊 Crop Demand Forecast
On the "Market" page:

Uses local crop trends to suggest what to plant next season.

Mock data or future ML integration planned.

📋 To Do / Enhancements
 Add real-time weather integration

 Vector DB for smarter chatbot memory

 Firebase or Supabase for auth & user data

 Offline access (PWA mode)

🧠 Acknowledgements
Ollama

TensorFlow

react-i18next

Indian Government Agri Schemes

📜 License
MIT License © 2025 Thanuja

🙋‍♀️ Author
Thanuja
Smart Agri Farming Developer





