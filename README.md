# 🚀 SpeedType Pro — Typing Speed Test with Persistent History

A sleek, full-stack typing speed test web app built with **Flask + SQLite + Vanilla JS**.
Test your typing skills in real-time, track your progress, and improve with persistent history.

---

## ✨ Features

* ⚡ Real-time typing speed (WPM) calculation
* 🎯 Accuracy tracking with visual feedback
* ⏱️ 60-second timed tests
* 🧠 Difficulty levels: Easy / Medium / Hard
* 📊 Persistent test history (stored in SQLite)
* 🎨 Modern responsive UI with smooth animations
* 🔄 Dynamic text generation for continuous practice

---

## 🖥️ Demo Preview

* Live typing feedback:

  * ✅ Correct characters → Green
  * ❌ Incorrect characters → Red
* Real-time stats:

  * WPM
  * Accuracy
  * Timer

---

## 🏗️ Tech Stack

**Frontend**

* HTML5 + CSS3
* Vanilla JavaScript
* Font Awesome icons

**Backend**

* Python (Flask)
* SQLite database

---

## 📂 Project Structure

```
.
├── main.py              # Flask backend
├── typing_history.db   # SQLite database (auto-created)
├── templates/
│   └── index.html      # Frontend UI
```

> Backend routes and DB logic are defined in 
> Frontend UI and logic are in 

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/speedtype-pro.git
cd speedtype-pro
```

### 2. Install dependencies

```bash
pip install flask
```

### 3. Run the app

```bash
python main.py
```

### 4. Open in browser

```
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

### Backend (Flask)

* Stores typing results (`wpm`, `accuracy`, `difficulty`)
* Provides APIs:

  * `POST /save_result` → Save test result
  * `GET /get_history` → Fetch last 5 results

### Database Schema

```sql
history (
    id INTEGER PRIMARY KEY,
    wpm INTEGER,
    accuracy INTEGER,
    difficulty TEXT,
    timestamp DATETIME
)
```

### Frontend Logic

* Tracks keystrokes in real-time
* Calculates:

  * Words per minute = `(characters / 5) / minutes`
  * Accuracy = `(correct / total) * 100`
* Sends results to backend using `fetch()`

---

## 🎮 Usage

1. Select difficulty level
2. Click **Start Test**
3. Begin typing the displayed text
4. View real-time stats
5. Check your results after 60 seconds
6. See your past performance in **History**

---

## 📈 Typing Levels

| WPM Range | Level        |
| --------- | ------------ |
| < 30      | Beginner     |
| 30–44     | Intermediate |
| 45–64     | Advanced     |
| 65+       | Expert       |

---

## 🔥 Future Improvements

* 🏆 Leaderboard system
* 👤 User authentication
* 📊 Detailed analytics dashboard
* 🌙 Dark mode toggle
* 📱 Mobile optimization improvements
* 🎯 Custom test duration

---

## 🤝 Contributing

Contributions are welcome!

```bash
fork → create branch → commit → pull request
```

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 💡 Final Note

This project is a great example of:

* Full-stack development with minimal dependencies
* Clean UI + real-time interaction
* Practical use of Flask + SQLite

---
