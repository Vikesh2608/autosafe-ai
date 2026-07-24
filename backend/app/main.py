from fastapi import FastAPI

app = FastAPI(
    title="AutoSafe AI",
    description="Open Source AI Vehicle Safety Platform",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "application": "AutoSafe AI",
        "status": "Running",
        "version": "0.1.0"
    }
@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }