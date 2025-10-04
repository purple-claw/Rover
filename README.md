# Rover - Digital DSA Instructor

A modern, interactive web-based platform for learning Data Structures and Algorithms (DSA) with comprehensive tutorials, pattern recognition training, and complexity analysis.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Overview

Rover is an educational platform designed to transform how students learn DSA concepts. The platform provides structured learning paths, interactive code examples, and real-world applications of algorithmic patterns. Built with modern web technologies, it offers a responsive, pitch-black themed interface with McLaren Orange accents for optimal readability and professional aesthetics.

### Key Learning Areas

- **Pattern Recognition**: Master the 5 universal problem-solving patterns (Counter/Tracker, Two Pointers, Divide & Conquer, Builder/Accumulator, Optimizer)
- **Complexity Analysis**: Understand time and space complexity with systematic frameworks
- **Optimization Techniques**: Learn precomputation, early termination, space-time tradeoffs, and data structure selection
- **Mental Models**: Apply UMPIRE method and systematic problem decomposition
- **Sliding Window**: Fixed and variable window patterns with practical implementations
- **Time & Space Complexity**: Comprehensive analysis frameworks and trade-off understanding

## Features

### Content Delivery

- **Interactive HTML Templates**: Rich, collapsible sections with code examples and copy functionality
- **Real-time Search**: Live search with highlighting across all content sections
- **Progress Tracking**: Visual progress indicators showing learning advancement
- **Code Examples**: 40+ interactive code blocks with syntax highlighting and one-click copying
- **Responsive Design**: Three-tier responsive breakpoints (1024px, 768px, 480px) for optimal viewing on all devices

### User Interface

- **Modern Landing Page**: Professional introduction to the platform with smooth navigation
- **Dashboard Navigation**: Organized content hierarchy with visual category cards
- **Theme Toggle**: Switch between dark and light modes for comfortable reading
- **Keyboard Shortcuts**: Quick access to search (Ctrl+F) and navigation (Esc)
- **Back Navigation**: Consistent navigation patterns across all content pages

### Educational Content

- **Elaborated Explanations**: Deep-dive philosophical explanations connecting concepts to cognitive thinking
- **Real-world Applications**: Industry examples from Google, GPS systems, MP3 compression, React, and more
- **Insight Boxes**: Special highlighted sections with key concepts and mental models
- **Step-by-step Walkthroughs**: Detailed execution traces for algorithm understanding
- **Optimization Comparisons**: Side-by-side analysis of naive vs optimized approaches

## Technology Stack

### Backend

- **FastAPI**: Modern, high-performance Python web framework
- **Uvicorn**: Lightning-fast ASGI server
- **Jinja2**: Template engine for dynamic content rendering
- **BeautifulSoup4**: HTML parsing and content manipulation
- **Python 3.11+**: Latest Python features and performance improvements

### Frontend

- **HTML5**: Semantic markup with accessibility considerations
- **CSS3**: Custom styling with CSS variables, flexbox, and grid layouts
- **Vanilla JavaScript**: No framework dependencies for lightweight performance
- **Responsive Design**: Mobile-first approach with progressive enhancement

### Development Tools

- **Git**: Version control with GitHub integration
- **Virtual Environment**: Isolated Python dependencies

## Project Structure

```
Rover/
├── app.py                      # Main FastAPI application entry point
├── content_parser.py           # HTML content parsing and processing
├── navigation_builder.py       # Dynamic navigation structure generation
├── requirements.txt            # Python dependencies
├── theme-config.js            # Theme configuration and styling constants
│
├── static/                     # Static assets
│   ├── landingPage.html       # Main landing page
│   ├── dashboard.html         # Content navigation dashboard
│   ├── main.css              # Global styles and CSS variables
│   └── index.js              # Client-side JavaScript
│
├── templates/                  # Educational content templates
│   ├── Complexity/
│   │   └── timeNspace.html   # Time and space complexity analysis
│   ├── Problem Solving/
│   │   └── Pattern_Recognition.html  # Core pattern recognition training
│   └── Sliding Window/
│       ├── Fixed Window/
│       │   └── fixedWindow.html
│       └── Variable Window/
│           └── template.html
│
└── docs/                       # Documentation templates
    ├── HTML_TEMPLATE.md       # HTML structure guidelines
    ├── CSS_STYLES_TEMPLATE.md # CSS styling conventions
    └── CSS_QUICK_REFERENCE.md # Quick CSS reference guide
```

## Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git
- Virtual environment tool (venv or virtualenv)

### Step-by-Step Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/purple-claw/Rover.git
   cd Rover
   ```

2. **Create a virtual environment**

   ```bash
   # On Linux/Mac
   python3 -m venv .venv
   source .venv/bin/activate

   # On Windows
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation**

   ```bash
   python -c "import fastapi; import uvicorn; print('Dependencies installed successfully')"
   ```

## Usage

### Running the Development Server

1. **Start the application**

   ```bash
   python app.py
   ```

   Alternative using uvicorn directly:

   ```bash
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Access the application**

   Open your web browser and navigate to:
   - Landing Page: `http://localhost:8000/`
   - Dashboard: `http://localhost:8000/dashboard`
   - Health Check: `http://localhost:8000/health`

3. **Navigate content**

   - Click category cards on the dashboard to explore topics
   - Use the search functionality (Ctrl+F) to find specific content
   - Toggle themes using the theme switcher in the top navigation
   - Copy code examples with one-click copy buttons

### Viewing Specific Content

Access content directly via URL patterns:

```
http://localhost:8000/view/Problem%20Solving/Pattern_Recognition.html
http://localhost:8000/view/Complexity/timeNspace.html
http://localhost:8000/view/Sliding%20Window/Fixed%20Window/fixedWindow.html
```

### API Endpoints

The application exposes several endpoints:

- `GET /` - Landing page
- `GET /dashboard` - Content navigation dashboard
- `GET /view/{path:path}` - View specific content by path
- `GET /api/navigation` - JSON API for navigation structure
- `GET /health` - Health check endpoint

## Development

### Adding New Content

1. **Create HTML file in appropriate template directory**

   ```bash
   # Example: Adding a new sorting algorithms page
   mkdir -p templates/Sorting
   touch templates/Sorting/sorting_algorithms.html
   ```

2. **Follow the HTML template structure**

   Reference `docs/HTML_TEMPLATE.md` for standardized structure:
   - Include proper meta tags and title
   - Use semantic HTML5 elements
   - Apply consistent CSS classes
   - Add collapsible sections for better organization
   - Include code blocks with copy functionality

3. **Use CSS variables for consistent styling**

   Reference `docs/CSS_STYLES_TEMPLATE.md`:
   - `--bg-primary`: #000000 (pitch black)
   - `--mclaren-orange`: #FF8000
   - `--text-primary`: #ffffff
   - Standard spacing: --spacing-sm, --spacing-md, --spacing-lg

4. **Test the new content**

   ```bash
   # Restart the server to detect new files
   python app.py

   # Access via browser
   http://localhost:8000/view/Sorting/sorting_algorithms.html
   ```

### Code Style Guidelines

**Python:**
- Follow PEP 8 style guidelines
- Use type hints where applicable
- Document functions with docstrings
- Maximum line length: 100 characters

**HTML:**
- Use semantic HTML5 elements
- Proper indentation (4 spaces)
- Include ARIA labels for accessibility
- Validate with W3C validator

**CSS:**
- Use CSS variables for theme values
- Mobile-first responsive design
- BEM naming convention for components
- Comment complex selectors

**JavaScript:**
- Use ES6+ features
- Descriptive variable names
- Add comments for complex logic
- Avoid global namespace pollution

### Testing

1. **Manual testing checklist**

   - [ ] All routes return 200 status
   - [ ] Static files load correctly
   - [ ] Navigation works across all pages
   - [ ] Search functionality highlights matches
   - [ ] Code copy buttons function properly
   - [ ] Responsive design works on mobile/tablet/desktop
   - [ ] Theme toggle switches correctly
   - [ ] Collapsible sections expand/collapse

2. **Health check endpoint**

   ```bash
   curl http://localhost:8000/health
   # Expected: {"status":"healthy"}
   ```

3. **Navigation API test**

   ```bash
   curl http://localhost:8000/api/navigation
   # Expected: JSON structure of all content
   ```

## API Documentation

### GET /

**Description:** Serves the landing page

**Response:** HTML content

**Example:**
```bash
curl http://localhost:8000/
```

### GET /dashboard

**Description:** Serves the dashboard with content navigation

**Response:** HTML content with category cards

**Example:**
```bash
curl http://localhost:8000/dashboard
```

### GET /view/{path:path}

**Description:** Serves specific content by file path

**Parameters:**
- `path` (string): Relative path to content file (URL-encoded)

**Response:** HTML content with navigation back button

**Example:**
```bash
curl http://localhost:8000/view/Problem%20Solving/Pattern_Recognition.html
```

### GET /api/navigation

**Description:** Returns navigation structure as JSON

**Response:** JSON object with hierarchical navigation tree

**Example:**
```bash
curl http://localhost:8000/api/navigation
```

**Response Format:**
```json
{
  "navigation": {
    "Complexity": ["timeNspace.html"],
    "Problem Solving": ["Pattern_Recognition.html"],
    "Sliding Window": {
      "Fixed Window": ["fixedWindow.html"],
      "Variable Window": ["template.html"]
    }
  }
}
```

### GET /health

**Description:** Health check endpoint for monitoring

**Response:** JSON status object

**Example:**
```bash
curl http://localhost:8000/health
```

**Response:**
```json
{
  "status": "healthy"
}
```

## Contributing

We welcome contributions from the community! Whether you're fixing bugs, improving documentation, or adding new features, your help is appreciated.

### How to Contribute

1. **Fork the repository**

   Click the "Fork" button on the GitHub repository page to create your own copy.

2. **Clone your fork**

   ```bash
   git clone https://github.com/your-username/Rover.git
   cd Rover
   ```

3. **Create a feature branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

   Branch naming conventions:
   - `feature/` - New features or enhancements
   - `bugfix/` - Bug fixes
   - `docs/` - Documentation updates
   - `refactor/` - Code refactoring

4. **Make your changes**

   - Write clear, descriptive commit messages
   - Follow the code style guidelines
   - Add comments for complex logic
   - Update documentation if needed

5. **Test your changes**

   ```bash
   # Ensure the application runs without errors
   python app.py

   # Test all affected routes and functionality
   # Verify responsive design on different screen sizes
   ```

6. **Commit your changes**

   ```bash
   git add .
   git commit -m "Add: Brief description of your changes"
   ```

   Commit message format:
   - `Add:` - New features or files
   - `Fix:` - Bug fixes
   - `Update:` - Changes to existing features
   - `Refactor:` - Code restructuring
   - `Docs:` - Documentation changes

7. **Push to your fork**

   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request**

   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your fork and branch
   - Provide a clear description of your changes
   - Reference any related issues

### Contribution Guidelines

**Code Quality:**
- Write clean, readable, and maintainable code
- Follow existing code structure and patterns
- Remove debugging code and console logs
- Ensure no breaking changes to existing functionality

**Documentation:**
- Update README.md if adding new features
- Document new functions and classes
- Update API documentation for endpoint changes
- Include code examples where helpful

**Content Contributions:**
- Follow HTML template structure in `docs/HTML_TEMPLATE.md`
- Maintain consistent styling using CSS variables
- Include detailed explanations and real-world examples
- Add insight boxes for key concepts
- Ensure all code examples are tested and correct

**Testing:**
- Test on multiple browsers (Chrome, Firefox, Safari)
- Verify responsive design on mobile, tablet, desktop
- Check accessibility with screen readers
- Ensure all links and navigation work correctly

### Types of Contributions

**Bug Reports:**
- Search existing issues first
- Include steps to reproduce
- Provide error messages and screenshots
- Specify browser and operating system

**Feature Requests:**
- Describe the feature and its benefits
- Explain use cases and examples
- Consider implementation complexity
- Discuss potential alternatives

**Content Improvements:**
- Fix typos and grammatical errors
- Clarify explanations and examples
- Add missing topics or patterns
- Improve code examples and comments

**Code Improvements:**
- Optimize performance
- Refactor for better readability
- Add error handling
- Improve security

### Code Review Process

1. Maintainers will review your pull request
2. Address any requested changes or feedback
3. Once approved, your code will be merged
4. Your contribution will be acknowledged

### Getting Help

If you need help or have questions:
- Open an issue on GitHub with the `question` label
- Check existing documentation in the `docs/` folder
- Review closed issues for similar problems

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- FastAPI framework for excellent Python web development
- The open-source community for inspiration and tools
- Contributors who help improve this platform

## Contact

- Repository: https://github.com/purple-claw/Rover
- Issues: https://github.com/purple-claw/Rover/issues

---

**Note:** This project is under active development. Features and documentation are continuously being improved.
