from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# Define a route to serve HTML pages dynamically from the 'templates' directory
@app.get("/{page_name}", response_class=HTMLResponse)
def serve_page(page_name: str):
    # Check if the requested page exists in the 'templates' directory
    page_path = os.path.join('templates', f"{page_name}.html")

    if os.path.exists(page_path):
        with open(page_path, "r", encoding="utf-8") as file:
            page_content = file.read()
        return HTMLResponse(content=page_content)
    else:
        raise HTTPException(status_code=404, detail="Page not found")

# Define a route for the root path to serve 'index.html' as the default landing page
@app.get("/", response_class=HTMLResponse)
def serve_default_page():
    return serve_page("index")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7890)
