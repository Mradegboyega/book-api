from fastapi import FastAPI

# Create a FastAPI app instance
app = FastAPI()

# Define a route for the root endpoint
@app.get("/")
def home():
    # Return a JSON response
    return {"message": "Hello, Server!"}
