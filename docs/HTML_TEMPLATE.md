# Rover HTML Template Structure

## Standard Template for All Content HTML Files

All HTML content files in the `/templates` directory should follow this structure for consistency with the landing page and dashboard theme:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Page Title] | Rover</title>
    <link rel="stylesheet" href="/static/main.css">
    <style>
        /* Page-specific styles following the theme */
        body {
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.8;
        }

        .content-wrapper {
            max-width: 1200px;
            margin: 0 auto;
            padding: var(--spacing-2xl) var(--spacing-lg);
            padding-top: 100px;
        }

        /* Back button - Always include */
        .back-button {
            position: fixed;
            top: 20px;
            left: 20px;
            z-index: 1000;
            background: var(--mclaren-orange);
            color: white;
            padding: var(--spacing-sm) var(--spacing-lg);
            border-radius: var(--radius-full);
            text-decoration: none;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: var(--spacing-xs);
            transition: var(--transition-base);
            box-shadow: 0 4px 12px rgba(255, 128, 0, 0.3);
        }

        .back-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(255, 128, 0, 0.5);
        }

        /* Page Header */
        .page-header {
            text-align: center;
            margin-bottom: var(--spacing-2xl);
            padding: var(--spacing-2xl);
            background: var(--bg-card);
            border-radius: var(--radius-lg);
            border: 1px solid rgba(255, 128, 0, 0.2);
        }

        .page-title {
            font-size: var(--font-size-4xl);
            font-weight: 800;
            color: var(--mclaren-orange);
            margin-bottom: var(--spacing-md);
        }

        /* Content Sections */
        .section {
            background: var(--bg-card);
            border-radius: var(--radius-lg);
            padding: var(--spacing-2xl);
            margin-bottom: var(--spacing-xl);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        /* Code Blocks */
        .code-block {
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: var(--radius-md);
            padding: var(--spacing-lg);
            margin: var(--spacing-md) 0;
            overflow-x: auto;
        }

        .code-block pre {
            margin: 0;
            font-family: 'Monaco', 'Courier New', monospace;
            color: #e2e8f0;
        }

        /* Interactive Elements */
        .progress-bar {
            position: fixed;
            top: 0;
            left: 0;
            height: 4px;
            background: var(--mclaren-orange);
            z-index: 9999;
            transition: width 0.3s ease;
        }
    </style>
</head>
<body>
    <!-- Progress Bar -->
    <div class="progress-bar" id="progressBar"></div>

    <!-- Back Button -->
    <a href="/dashboard" class="back-button">
        <span>←</span>
        <span>Back to Dashboard</span>
    </a>

    <!-- Main Content -->
    <div class="content-wrapper">
        <!-- Page Header -->
        <header class="page-header">
            <h1 class="page-title">[Your Title]</h1>
            <p>[Your introduction]</p>
        </header>

        <!-- Content Sections -->
        <section class="section">
            <!-- Your content here -->
        </section>
    </div>

    <!-- Floating Orbs (optional) -->
    <div class="gradient-orb orb-1"></div>
    <div class="gradient-orb orb-2"></div>
    <div class="gradient-orb orb-3"></div>

    <!-- Interactive Scripts -->
    <script>
        // Progress bar on scroll
        window.addEventListener('scroll', () => {
            const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (winScroll / height) * 100;
            document.getElementById('progressBar').style.width = scrolled + '%';
        });

        // Collapsible sections
        document.querySelectorAll('.section-header').forEach(header => {
            header.addEventListener('click', () => {
                header.parentElement.classList.toggle('collapsed');
            });
        });

        // Copy code button functionality
        document.querySelectorAll('.copy-button').forEach(button => {
            button.addEventListener('click', () => {
                const code = button.parentElement.querySelector('pre').textContent;
                navigator.clipboard.writeText(code).then(() => {
                    button.textContent = '✓ Copied!';
                    setTimeout(() => button.textContent = 'Copy', 2000);
                });
            });
        });
    </script>
</body>
</html>
```

## Key Features to Include:

### 1. **Navigation**
- Back button to dashboard (fixed position)
- Progress bar showing reading progress
- Optional breadcrumb navigation

### 2. **Color Scheme** (Use CSS variables from main.css)
- Primary: `var(--mclaren-orange)` - #FF8000
- Text: `var(--text-primary)` - White
- Background: `var(--bg-primary)` - Pitch black
- Cards: `var(--bg-card)` - Dark gray with transparency
- Accent colors: Meta Blue, Terminal Green, Ferrari Red (use sparingly)

### 3. **Interactive Elements**
- Collapsible sections with smooth animations
- Copy buttons on code blocks
- Scroll-triggered animations
- Search functionality (optional)
- Theme toggle (optional)

### 4. **Typography**
- Use font-size variables: `var(--font-size-xs)` through `var(--font-size-4xl)`
- Consistent spacing: `var(--spacing-xs)` through `var(--spacing-2xl)`
- Line height: 1.6-1.8 for readability

### 5. **Responsive Design**
- Mobile-first approach
- Breakpoints at 480px, 768px, 1024px
- Stack sections vertically on mobile
- Adjust font sizes and padding

### 6. **Code Styling**
- Dark background with syntax highlighting
- Monaco or Courier font family
- Copy button in top-right
- Horizontal scroll for long lines

### 7. **Content Structure**
- Clear hierarchy with h1-h6
- Semantic HTML5 elements
- Proper spacing between sections
- Visual indicators for important info (borders, backgrounds)

## Example Components:

### Pattern Card:
```html
<div class="pattern-card">
    <h3 class="pattern-title">🎯 Pattern Name</h3>
    <p class="pattern-subtitle">Short description</p>
    <div class="pattern-content">
        <!-- Content here -->
    </div>
</div>
```

### Code Block with Copy:
```html
<div class="code-block">
    <button class="copy-button">Copy</button>
    <pre><code>
def example():
    return "code here"
    </code></pre>
</div>
```

### Insight Box:
```html
<div class="insight-box">
    <div class="insight-title">💡 The Insight:</div>
    <p>Key takeaway or important point</p>
</div>
```

### Step-by-Step:
```html
<div class="step">
    <span class="step-number">1</span>
    <span>Step description</span>
</div>
```

## CSS Variables Reference:

From `/static/main.css`:

```css
--mclaren-orange: #FF8000
--meta-blue: #1877F2
--terminal-green: #00FF00
--ferrari-red: #FF2800

--bg-primary: #0a0a0a
--bg-secondary: #121212
--bg-card: rgba(26, 26, 26, 0.8)

--text-primary: #ffffff
--text-secondary: #a0aec0
--text-muted: #718096

--font-size-xs: 0.75rem
--font-size-sm: 0.875rem
--font-size-base: 1rem
--font-size-lg: 1.125rem
--font-size-xl: 1.25rem
--font-size-2xl: 1.5rem
--font-size-3xl: 1.875rem
--font-size-4xl: 2.25rem

--spacing-xs: 0.25rem
--spacing-sm: 0.5rem
--spacing-md: 1rem
--spacing-lg: 1.5rem
--spacing-xl: 2rem
--spacing-2xl: 3rem

--radius-sm: 0.375rem
--radius-md: 0.5rem
--radius-lg: 0.75rem
--radius-full: 9999px

--transition-base: all 0.3s ease
```

## Usage Instructions:

1. Copy the base template
2. Replace [Page Title] with your content title
3. Add your content in semantic HTML structure
4. Use the pre-defined component classes
5. Include interactive JavaScript as needed
6. Test responsiveness on mobile/tablet/desktop
7. Ensure back button links to correct page

## Best Practices:

- Keep color usage consistent (Orange as primary)
- Use smooth transitions (300ms ease)
- Add hover states for interactive elements
- Include loading states where appropriate
- Ensure accessibility (alt text, ARIA labels)
- Optimize images and resources
- Test on multiple browsers
- Validate HTML and CSS

