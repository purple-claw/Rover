import os
from pathlib import Path
from bs4 import BeautifulSoup

class ContentParser:
    def __init__(self, templates_dir):
        self.templates_dir = Path(templates_dir)

    def extract_metadata(self, html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')
        if soup.title:
            title = soup.title
        else:
            Path(html_path).stem
        
        return {
            'title' : title.strip(),
            'path' : str(html_path),
            'relative_path' : str(Path(html_path).relative_to(self.templates_dir))     
        }
    
    def getAllTemplates(self):
        temps = []
        for hfile in self.templates_dir.rglob('*.html'):
            meta = self.extract_metadata(hfile)
            temps.append(meta)
        return temps
    
    def getRawContent(self, relative_path):
        fpath = self.templates_dir / relative_path
        if not fpath.exists():
            return None
        with open(fpath, 'r', encoding='utf-8') as f:
            return f.read()