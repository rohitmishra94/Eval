from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.model_openai import router as openai_router


app = FastAPI()

# Allow CORS for all domains (you can customize it later)
origins = [
    "*",  # Allow all origins (you can specify specific domains if needed)
]

# Add CORS middleware globally
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows all origins, you can restrict this to specific domains
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Include routers from the sub-servers
app.include_router(openai_router, prefix="/api/openai")

# Routes in the main server
@app.get("/")
async def root():
    return {"message": "Welcome to the main server!"}

@app.get("/health")
async def health_check():
    return {"status": "Main server is healthy."}
