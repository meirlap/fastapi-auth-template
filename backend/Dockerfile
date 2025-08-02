# התחל מאימג' רשמי של פייתון
FROM python:3.11-slim

# הגדר את תיקיית העבודה בתוך הקונטיינר
WORKDIR /app

# העתק את קובץ הדרישות והתקן אותן
# זה נעשה בנפרד כדי לנצל את ה-cache של דוקר
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# העתק את כל קוד האפליקציה לתיקיית העבודה
# בזמן פיתוח, ה-volume שהגדרנו יחליף את זה, אבל זה חיוני לבנייה לפרודקשן
COPY . .

# הפקודה שתרוץ כשהקונטיינר יעלה
# Uvicorn הוא שרת שיריץ את אפליקציית ה-FastAPI שלנו
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
