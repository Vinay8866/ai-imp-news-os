"""
AI IMP NEWS OS
FastAPI Server Entry Point
Version: 2.0
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.config.settings import APP_PORT, MEDIA_DIR
from app.api.routes import router


app = FastAPI(
    title="AI IMP NEWS OS API",
    description="Free Autonomous Multi-Agent Content Operating System",
    version="2.0"
)

# CORS Policy for Frontend Access (Port 5500 / file://)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Mount Static Media Directory (Images Preview)
if MEDIA_DIR.exists():
    app.mount("/media", StaticFiles(directory=str(MEDIA_DIR)), name="media")

# Include Routes
app.include_router(router)


@app.get("/")
def root():
    return {
        "system": "AI IMP NEWS OS",
        "version": "2.0",
        "status": "online",
        "docs_url": "http://127.0.0.1:8000/docs"
    }


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("🚀 AI IMP NEWS OS - FASTAPI SERVER STARTING")
    print(f"📡 API Base URL : http://127.0.0.1:{APP_PORT}")
    print(f"📖 Swagger Docs : http://127.0.0.1:{APP_PORT}/docs")
    print("=" * 60 + "\n")

    uvicorn.run("app.server:app", host="127.0.0.1", port=APP_PORT, reload=True)