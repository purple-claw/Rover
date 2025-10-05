from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import json

from content_parser import ContentParser
from navigation_builder import NavigationBuilder

app = FastAPI(title="Rover - Digital DSA Instructor", version="1.0.0")

# Configuration
TEMPLATES_DIR = "templates"  
# Initialize components
content_parser = ContentParser(TEMPLATES_DIR)
nav_builder = NavigationBuilder(TEMPLATES_DIR)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Landing Page - Main Entry Point
@app.get("/", response_class=HTMLResponse)
async def landing_page():
    """Serve the modern landing page as the main entry point"""
    with open("static/landingPage.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

# Dashboard/Templates Navigation page
@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Serve the modern dashboard page"""
    with open("static/dashboard.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

# View specific content
@app.get("/view/{path:path}", response_class=HTMLResponse)
async def view_content(path: str):
    # URL decode the path (handles spaces and special characters)
    from urllib.parse import unquote
    file_path = unquote(path)
    
    content = content_parser.getRawContent(file_path)
    if content is None:
        return HTMLResponse(content="""
        <html>
            <head>
                <title>Content Not Found</title>
                <style>
                    body { background: #0a0a0a; color: white; text-align: center; padding: 2rem; }
                    a { color: #ff8c00; text-decoration: none; }
                </style>
            </head>
            <body>
                <h1>404 - Content Not Found</h1>
                <p>The requested content does not exist.</p>
                <a href="/dashboard">← Back to Dashboard</a>
            </body>
        </html>
        """)
    
    # Add navigation back button
    nav_back = '''
    <div style="position:fixed; top:10px; left:10px; z-index:1000; background:#ff8c00; padding:10px 15px; border-radius:5px;">
        <a href="/dashboard" style="color:white; text-decoration:none; font-weight:bold;">← Back to Dashboard</a>
    </div>
    '''
    
    # Insert navigation back button after <body> tag
    content_with_nav = content.replace('<body>', f'<body>{nav_back}')
    
    return HTMLResponse(content=content_with_nav)

# API endpoint to get navigation (for future automation)
@app.get("/api/navigation")
async def get_navigation():
    nav = nav_builder.build_navigation()
    return JSONResponse(content={"navigation": nav})

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)