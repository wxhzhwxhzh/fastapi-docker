from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# 读取环境变量，默认目录 /app/www
INDEX_DIR = os.getenv("INDEX_DIR", "/app/www")
INDEX_FILE = os.path.join(INDEX_DIR, "index.html")

@app.get("/")
def read_index():
    if os.path.exists(INDEX_FILE):
        return FileResponse(INDEX_FILE, media_type="text/html")
    return {"error": f"index.html not found in {INDEX_DIR}"}

# 挂载整个目录作为静态资源
if os.path.exists(INDEX_DIR):
    app.mount("/", StaticFiles(directory=INDEX_DIR), name="static")
