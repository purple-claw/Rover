"""
FastAPI backend for React application with automatic content detection
Watches the content folder and automatically updates navigation
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pathlib import Path
import json
from urllib.parse import quote
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
import time

app = FastAPI(title="Rover React Backend", version="2.0.0")

# Enable CORS for React development server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
CONTENT_DIR = Path("rover-react/src/content")
TEMPLATES_DIR = Path("templates")  # Keep for backward compatibility

# Global navigation cache
navigation_cache = {"navigation": [], "last_updated": None}
navigation_lock = threading.Lock()


class NavigationBuilder:
    """Builds navigation structure from file system"""
    
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
    
    def build_navigation(self):
        """Build navigation from both JSX and HTML files"""
        nav = []
        
        if not self.base_dir.exists():
            return nav
        
        # Scan for .jsx, .tsx, and .html files
        file_patterns = ['**/*.jsx', '**/*.tsx', '**/*.html', '**/*.js']
        all_files = []
        
        for pattern in file_patterns:
            all_files.extend(self.base_dir.rglob(pattern))
        
        # Filter out node_modules and build directories
        all_files = [
            f for f in all_files 
            if 'node_modules' not in str(f) and 'build' not in str(f)
        ]
        
        for file_path in all_files:
            relative_path = file_path.relative_to(self.base_dir)
            parts = relative_path.parts
            
            current_level = nav
            for i, part in enumerate(parts[:-1]):  # Exclude filename
                found = False
                for item in current_level:
                    if item['name'] == part and item['type'] == 'folder':
                        current_level = item['children']
                        found = True
                        break
                
                if not found:
                    new_folder = {
                        'name': part,
                        'type': 'folder',
                        'children': [],
                        'path': str(Path(*parts[:i+1]))
                    }
                    current_level.append(new_folder)
                    current_level = new_folder['children']
            
            # Add the file
            file_name = file_path.stem  # Remove extension
            current_level.append({
                'name': file_name,
                'type': 'file',
                'path': str(relative_path),
                'url': f"/content/{quote(str(relative_path))}"
            })
        
        return nav


class ContentWatcher(FileSystemEventHandler):
    """Watches for file system changes and updates navigation"""
    
    def __init__(self, content_builder):
        self.content_builder = content_builder
        self.debounce_timer = None
    
    def on_any_event(self, event):
        """Handle any file system event"""
        if event.is_directory:
            return
        
        # Debounce updates (wait 1 second before updating)
        if self.debounce_timer:
            self.debounce_timer.cancel()
        
        self.debounce_timer = threading.Timer(1.0, self.update_navigation)
        self.debounce_timer.start()
    
    def update_navigation(self):
        """Update the navigation cache"""
        with navigation_lock:
            navigation_cache["navigation"] = self.content_builder.build_navigation()
            navigation_cache["last_updated"] = time.time()
            print(f"✅ Navigation updated at {time.ctime()}")


# Initialize builders
content_builder = NavigationBuilder(CONTENT_DIR)
templates_builder = NavigationBuilder(TEMPLATES_DIR)

# Initialize navigation cache
with navigation_lock:
    # Combine navigation from both content and templates directories
    content_nav = content_builder.build_navigation()
    templates_nav = templates_builder.build_navigation()
    navigation_cache["navigation"] = content_nav + templates_nav
    navigation_cache["last_updated"] = time.time()

# Set up file watcher for content directory
if CONTENT_DIR.exists():
    event_handler = ContentWatcher(content_builder)
    observer = Observer()
    observer.schedule(event_handler, str(CONTENT_DIR), recursive=True)
    observer.start()
    print(f"👀 Watching {CONTENT_DIR} for changes...")
else:
    print(f"⚠️  Content directory not found: {CONTENT_DIR}")
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"✅ Created content directory: {CONTENT_DIR}")


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "Rover React Backend API",
        "version": "2.0.0"
    }


@app.get("/api/navigation")
async def get_navigation():
    """Get the current navigation structure"""
    with navigation_lock:
        return JSONResponse(content={
            "navigation": navigation_cache["navigation"],
            "last_updated": navigation_cache["last_updated"]
        })


@app.get("/api/refresh")
async def refresh_navigation():
    """Manually refresh the navigation structure"""
    with navigation_lock:
        content_nav = content_builder.build_navigation()
        templates_nav = templates_builder.build_navigation()
        navigation_cache["navigation"] = content_nav + templates_nav
        navigation_cache["last_updated"] = time.time()
    
    return JSONResponse(content={
        "status": "success",
        "message": "Navigation refreshed",
        "navigation": navigation_cache["navigation"]
    })


@app.get("/api/stats")
async def get_stats():
    """Get platform statistics"""
    with navigation_lock:
        nav = navigation_cache["navigation"]
    
    def count_files(items):
        count = 0
        for item in items:
            if item['type'] == 'file':
                count += 1
            elif item['type'] == 'folder' and 'children' in item:
                count += count_files(item['children'])
        return count
    
    total_categories = len(nav)
    total_resources = count_files(nav)
    
    return JSONResponse(content={
        "totalCategories": total_categories,
        "totalResources": total_resources,
        "status": "24/7",
        "platformType": "Free"
    })


@app.on_event("shutdown")
async def shutdown_event():
    """Clean up on shutdown"""
    if 'observer' in globals():
        observer.stop()
        observer.join()
        print("👋 File watcher stopped")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


