from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.auth_routes import auth_router
from .routes.leave_routes import leave_router

app = FastAPI()

origins = [
    "http://localhost:4200", 
    "http://127.0.0.1:4200",
    "*"
]



# Routes
app.include_router(auth_router)
app.include_router(leave_router)

# ✅ Add CORS middleware BEFORE routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  # Required for custom headers like 'Authorization'
)

@app.get('/')
def root():
    return {"message": "Welcome to the Leave Management API"}
