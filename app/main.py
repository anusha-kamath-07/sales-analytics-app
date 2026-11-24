from fastapi import FastAPI

# Create FastAPI app instance
app = FastAPI(
    title = "Sales Analytics API",
    description="API for analyzing sales data and generating business insights",
    version="1.0.0"
    )

@app.get("/")
def root():
    return {
        "message": "Welcome to Sales Analytics API", 
        "status": "success"
        }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


