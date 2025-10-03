from pathlib import Path

class NavigationBuilder:
    def __init__(self, templates_dir):
        self.templates_dir = Path(templates_dir)
    
    def build_navigation(self):
        nav = []
        
        for html_file in self.templates_dir.rglob('*.html'):
            relative_path = html_file.relative_to(self.templates_dir)
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
            
            # Add the HTML file
            # URL encode the path properly
            from urllib.parse import quote
            current_level.append({
                'name': html_file.stem,
                'type': 'file',
                'path': str(relative_path),
                'url': f"/view/{quote(str(relative_path))}"
            })
        
        return nav