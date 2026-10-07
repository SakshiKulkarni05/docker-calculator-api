from fastapi import FastAPI, HTTPException, Query

# Create the FastAPI application instance
app = FastAPI(
    title="Calculator API",
    description="A simple REST Calculator API built with Python and FastAPI.",
    version="1.0.0",
)


@app.get("/")
def root():
    """Root endpoint — confirms the API is running."""
    return {"message": "Calculator API is running!"}


@app.get("/health")
def health():
    """Health check endpoint — used to verify the service is alive."""
    return {"status": "healthy"}


@app.get("/add")
def add(a: float = Query(..., description="First number"),
        b: float = Query(..., description="Second number")):
    """Add two numbers together."""
    return {"result": a + b}


@app.get("/subtract")
def subtract(a: float = Query(..., description="First number"),
             b: float = Query(..., description="Second number")):
    """Subtract b from a."""
    return {"result": a - b}


@app.get("/multiply")
def multiply(a: float = Query(..., description="First number"),
             b: float = Query(..., description="Second number")):
    """Multiply two numbers together."""
    return {"result": a * b}


@app.get("/divide")
def divide(a: float = Query(..., description="First number"),
           b: float = Query(..., description="Second number")):
    """Divide a by b. Returns an error if b is zero."""
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
    return {"result": a / b}
