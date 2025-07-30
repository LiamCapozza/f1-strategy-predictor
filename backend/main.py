from fastapi import FastAPI
import requests

app = FastAPI(title="F1 Strategy Predictor API")

@app.get("/")
def read_root():
    return {"message": "F1 Strategy Predictor API is running!"}

@app.get("/test-openf1")
def test_openf1():
    # Test OpenF1 API connection
    response = requests.get("https://api.openf1.org/v1/sessions?year=2023&session_name=Race")
    return response.json()[:5]  # First 5 sessions

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)