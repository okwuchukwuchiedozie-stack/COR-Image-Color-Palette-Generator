# 🎨 COR_CARES Palette Engine

An optimized, production-ready **Flask Web Application** that leverages **NumPy vector mathematics** and the **Pillow (PIL)** library to process images and instantly extract their top 10 dominant color profiles. It includes a responsive modern UI styled with **Bootstrap 5** and a secure, fully functional contact inquiry dispatch system built for seamless cloud scalability.

---

## ✨ Features

- **🚀 Lightning-Fast Analysis:** Utilizes vectorized NumPy matrix operations to process dense pixel fields swiftly.
- **🎛️ Quantization Tolerance Slider:** Dynamically groups matching color gradients together or isolates granular variations using an interactive threshold control.
- **📊 Detailed Matrix Layout:** Displays hex values, raw RGB tuples, and exact pixel distribution percentage ratios in a clean, filterable data grid.
- **✉️ Automated Mail Pipeline:** Includes a professional contact dashboard powered by **Flask-WTF** form validations, environment variables, and **Flask-Mailman** SMTP infrastructure.
- **🌐 Cloud Deployment Ready:** Out-of-the-box support for WSGI production environments with custom multi-threaded **Gunicorn** clustering rules.

---

## 🏗️ Project Architecture

```text
Day-92-Image-Color-Palette-Generator/
│
├── main.py                  # Core Application Factory & Route Blueprint Processing
├── gunicorn.conf.py         # Production WSGI Server Worker & Thread Clustering Profile
├── Procfile                 # Cloud Deployment Orchestration Routine Mapping
├── .env                     # Local Environment Secret Variables Matrix (Do Not Commit!)
├── .gitignore               # Excludes Virtual Environments and Sensitive Files
├── requirements.txt         # Package Dependency Blueprint Matrix
│
└── templates/               # Modular Jinja2 Render Layout Blocks
    ├── base.html            # Core Framework Scaffolding & Shared Head Assets
    ├── header.html          # Global Navigation Bar Dashboard Element
    ├── footer.html          # Global Context-Aware Footer Frame
    ├── index.html           # Main Studio Palette Upload Workspace Controls
    └── contact.html         # Secure Validation Contact Form Interface
```

---

## 🛠️ Installation & Setup

Follow these steps to configure your workspace environment locally:

### 1. Clone the Workspace Matrix
```bash
git clone https://github.com
cd Day-92-Image-Color-Palette-Generator
```

### 2. Isolate with a Virtual Environment
```bash
# Create the environment block
python -m venv .venv

# Activate it (Windows)
.venv\Scripts\activate

# Activate it (macOS/Linux)
source .venv/bin/activate
```

### 3. Install Module Dependencies
Install the specific distribution-level packages required to link up the code hooks perfectly:
```bash
pip install flask bootstrap-flask flask-wtf email-validator numpy Pillow flask-mailman python-dotenv gunicorn
```

---

## 🔐 Environment Configuration

The application extracts its secure keys natively through a hidden local configuration file. 

Create a file named **`.env`** in the root folder of your project (next to `main.py`) and fill it out using your personal Gmail and Google App Password credentials:

```env
SECRET_KEY=your-custom-production-hash-key-987654321
MAIL_USERNAME=your_actual_gmail_address@gmail.com
MAIL_PASSWORD=your_16_character_app_password_no_spaces
```

*Note: Ensure `load_dotenv()` is actively declared at the top of your `main.py` asset matrix to automatically ingest these values.*

---

## 🚀 Usage & Deployment

### Local Development Runtime
Launch your application server directly from your terminal or PyCharm:
```bash
python main.py
```
Open your web browser and navigate to `http://127.0.0.1:5000`.

### Production WSGI Simulation
To test the production orchestration environment locally before deploying to the cloud, use **Gunicorn** to host the runtime processing matrix:
```bash
gunicorn main:application --config gunicorn.conf.py
```

---

## 📄 License

Distributed cleanly under the custom **COR_CARES** Development Framework. Copyright &copy; 2026. All rights reserved.
