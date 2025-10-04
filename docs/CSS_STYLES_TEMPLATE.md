# 🎨 Rover Landing Page - CSS Styles & Theme Template

> **Complete CSS styling guide and theme documentation for landingPage.html**
> 
> Author: Rover Development Team  
> Last Updated: October 4, 2025  
> Version: 1.0.0

---

## 📋 Table of Contents

1. [CSS Variables & Theme](#css-variables--theme)
2. [Color Palette](#color-palette)
3. [Typography](#typography)
4. [Spacing System](#spacing-system)
5. [Component Styles](#component-styles)
6. [Layout System](#layout-system)
7. [Animation & Transitions](#animation--transitions)
8. [Responsive Design](#responsive-design)
9. [Usage Examples](#usage-examples)

---

## 🎨 CSS Variables & Theme

### Root Variables (`:root`)

All theme variables are defined in the `:root` selector for global access:

```css
:root {
    /* Brand Colors */
    --meta-blue: #1877F2;
    --terminal-green: #00FF00;
    --mclaren-orange: #FF8000;
    --ferrari-red: #FF2800;
    
    /* Background Colors */
    --bg-primary: #000000;
    --bg-secondary: #0a0a0a;
    --bg-card: #121212;
    --bg-hover: #1a1a1a;
    
    /* Text Colors */
    --text-primary: #ffffff;
    --text-secondary: #b3b3b3;
    --text-muted: #666666;
    
    /* Primary Color */
    --color-primary: var(--mclaren-orange);
    
    /* Shadows */
    --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.3);
    --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.4);
    --shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.5);
    --shadow-xl: 0 16px 48px rgba(0, 0, 0, 0.6);
    
    /* Spacing Scale */
    --spacing-xs: 0.5rem;    /* 8px */
    --spacing-sm: 1rem;      /* 16px */
    --spacing-md: 1.5rem;    /* 24px */
    --spacing-lg: 2rem;      /* 32px */
    --spacing-xl: 3rem;      /* 48px */
    --spacing-2xl: 4rem;     /* 64px */
    
    /* Border Radius */
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --radius-xl: 24px;
    --radius-full: 9999px;
    
    /* Transitions */
    --transition-fast: 0.2s ease;
    --transition-base: 0.3s ease;
    --transition-slow: 0.5s ease;
    
    /* Typography */
    --font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    --font-size-xs: 0.75rem;   /* 12px */
    --font-size-sm: 0.875rem;  /* 14px */
    --font-size-base: 1rem;    /* 16px */
    --font-size-lg: 1.125rem;  /* 18px */
    --font-size-xl: 1.25rem;   /* 20px */
    --font-size-2xl: 1.5rem;   /* 24px */
    --font-size-3xl: 2rem;     /* 32px */
    --font-size-4xl: 2.5rem;   /* 40px */
    --font-size-5xl: 3rem;     /* 48px */
}
```

---

## 🎨 Color Palette

### Brand Colors

| Color Name | Hex Code | Usage | Example |
|------------|----------|-------|---------|
| **McLaren Orange** | `#FF8000` | Primary actions, highlights, CTAs | `background: var(--mclaren-orange);` |
| **Meta Blue** | `#1877F2` | Secondary accents, links | `color: var(--meta-blue);` |
| **Terminal Green** | `#00FF00` | Success states, code highlights | `border-color: var(--terminal-green);` |
| **Ferrari Red** | `#FF2800` | Warnings, errors, important notices | `color: var(--ferrari-red);` |

### Background Colors

| Color Name | Hex Code | Usage |
|------------|----------|-------|
| **Primary Background** | `#000000` | Main body background (pure black) |
| **Secondary Background** | `#0a0a0a` | Section backgrounds |
| **Card Background** | `#121212` | Card components, elevated surfaces |
| **Hover Background** | `#1a1a1a` | Hover states for interactive elements |

### Text Colors

| Color Name | Hex Code | Usage |
|------------|----------|-------|
| **Primary Text** | `#ffffff` | Headings, primary content (white) |
| **Secondary Text** | `#b3b3b3` | Body text, descriptions |
| **Muted Text** | `#666666` | Labels, captions, disabled states |

---

## 📝 Typography

### Font Family
```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

### Font Size Scale

| Variable | Size | px | Usage |
|----------|------|----|----|
| `--font-size-xs` | 0.75rem | 12px | Small labels, captions |
| `--font-size-sm` | 0.875rem | 14px | Secondary text, buttons |
| `--font-size-base` | 1rem | 16px | Body text (default) |
| `--font-size-lg` | 1.125rem | 18px | Large body text |
| `--font-size-xl` | 1.25rem | 20px | Small headings |
| `--font-size-2xl` | 1.5rem | 24px | Section headings |
| `--font-size-3xl` | 2rem | 32px | Page headings |
| `--font-size-4xl` | 2.5rem | 40px | Hero headings |
| `--font-size-5xl` | 3rem | 48px | Large hero text |

### Font Weights

| Weight | Value | Usage |
|--------|-------|-------|
| Light | 300 | Subtle text |
| Regular | 400 | Body text |
| Medium | 500 | Navigation, labels |
| Semibold | 600 | Subheadings |
| Bold | 700 | Headings |
| Extrabold | 800 | Hero titles |
| Black | 900 | Display text |

---

## 📏 Spacing System

### Spacing Scale (8px base unit)

| Variable | Value | px | Usage |
|----------|-------|----|----|
| `--spacing-xs` | 0.5rem | 8px | Tight spacing, small gaps |
| `--spacing-sm` | 1rem | 16px | Default component spacing |
| `--spacing-md` | 1.5rem | 24px | Medium gaps |
| `--spacing-lg` | 2rem | 32px | Section spacing |
| `--spacing-xl` | 3rem | 48px | Large section gaps |
| `--spacing-2xl` | 4rem | 64px | Hero sections, major dividers |

### Border Radius

| Variable | Value | Usage |
|----------|-------|-------|
| `--radius-sm` | 8px | Small buttons, badges |
| `--radius-md` | 12px | Cards, inputs |
| `--radius-lg` | 16px | Large cards, modals |
| `--radius-xl` | 24px | Hero sections |
| `--radius-full` | 9999px | Fully rounded (pills, circles) |

---

## 🧩 Component Styles

### 1. Navigation Bar (`.navbar`)

```css
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    background: rgba(0, 0, 0, 0.8);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}
```

**Classes:**
- `.navbar` - Main navigation container
- `.nav-container` - Inner container with max-width
- `.nav-logo` - Logo with icon and text
- `.nav-menu` - Navigation links container
- `.nav-link` - Individual navigation link
- `.nav-link.active` - Active state with orange underline
- `.nav-actions` - Right side buttons
- `.mobile-menu-toggle` - Hamburger menu for mobile

### 2. Buttons

#### Primary Button
```css
.btn-primary {
    background: var(--mclaren-orange);
    color: var(--text-primary);
    padding: 0.75rem 1.5rem;
    border-radius: var(--radius-full);
    border: none;
    font-weight: 600;
    cursor: pointer;
    transition: var(--transition-base);
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}
```

#### Secondary Button
```css
.btn-secondary {
    background: transparent;
    color: var(--text-primary);
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 0.75rem 1.5rem;
    border-radius: var(--radius-full);
}
```

#### Large Button
```css
.btn-large {
    padding: 1rem 2rem;
    font-size: var(--font-size-lg);
    display: inline-flex;
    align-items: center;
    gap: var(--spacing-sm);
}
```

#### Outline Button
```css
.btn-outline {
    background: transparent;
    border: 2px solid var(--mclaren-orange);
    color: var(--mclaren-orange);
}
```

### 3. Cards

#### Feature Card
```css
.feature-card {
    background: var(--bg-card);
    padding: var(--spacing-xl);
    border-radius: var(--radius-lg);
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: var(--transition-base);
}

.feature-card:hover {
    transform: translateY(-8px);
    border-color: var(--meta-blue);
    box-shadow: 0 8px 32px rgba(24, 119, 242, 0.2);
}
```

**Sub-components:**
- `.feature-icon` - Icon container (64x64px)
- `.feature-title` - Card heading
- `.feature-description` - Card body text

#### Template Card
```css
.template-card {
    background: var(--bg-card);
    padding: var(--spacing-xl);
    border-radius: var(--radius-lg);
    border: 1px solid rgba(255, 255, 255, 0.1);
    position: relative;
    overflow: hidden;
}

.template-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: var(--mclaren-orange);
    transform: scaleX(0);
    transition: var(--transition-base);
}

.template-card:hover::before {
    transform: scaleX(1);
}
```

### 4. Hero Section

```css
.hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    padding: 6rem var(--spacing-md);
}

.hero-title {
    font-size: var(--font-size-5xl);
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: var(--spacing-md);
}

.gradient-text {
    color: var(--mclaren-orange);
}
```

**Sub-components:**
- `.hero-background` - Background container with orbs
- `.hero-badge` - Top badge with emoji
- `.hero-title` - Main heading
- `.hero-description` - Subtitle paragraph
- `.hero-cta` - Call-to-action buttons container
- `.hero-stats` - Statistics row

### 5. Gradient Orbs

```css
.gradient-orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    opacity: 0.3;
    animation: float 20s ease-in-out infinite;
}

.orb-1 {
    width: 400px;
    height: 400px;
    top: -100px;
    left: -100px;
    background: radial-gradient(circle, var(--meta-blue) 0%, transparent 70%);
}

.orb-2 {
    width: 500px;
    height: 500px;
    bottom: -150px;
    right: -150px;
    background: radial-gradient(circle, var(--mclaren-orange) 0%, transparent 70%);
    animation-delay: -10s;
}

.orb-3 {
    width: 450px;
    height: 450px;
    top: 50%;
    left: 50%;
    background: radial-gradient(circle, var(--terminal-green) 0%, transparent 70%);
    animation-delay: -5s;
}
```

### 6. Stats Components

```css
.stat-item {
    text-align: center;
}

.stat-number {
    font-size: var(--font-size-3xl);
    font-weight: 800;
    color: var(--mclaren-orange);
}

.stat-label {
    font-size: var(--font-size-sm);
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
```

### 7. Badges

```css
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: var(--spacing-xs);
    background: rgba(255, 128, 0, 0.1);
    border: 1px solid rgba(255, 128, 0, 0.3);
    padding: var(--spacing-xs) var(--spacing-md);
    border-radius: var(--radius-full);
    font-size: var(--font-size-sm);
    font-weight: 500;
    margin-bottom: var(--spacing-lg);
}

.badge-icon {
    font-size: var(--font-size-lg);
}
```

---

## 📐 Layout System

### Container
```css
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 var(--spacing-md);
}
```

### Grid Layouts

#### Features Grid
```css
.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--spacing-lg);
    margin-top: var(--spacing-2xl);
}
```

#### Templates Grid
```css
.templates-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: var(--spacing-lg);
    margin-top: var(--spacing-2xl);
}
```

#### Stats Grid
```css
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--spacing-xl);
}
```

### Flexbox Patterns

#### Horizontal Center
```css
.flex-center {
    display: flex;
    align-items: center;
    justify-content: center;
}
```

#### Space Between
```css
.flex-between {
    display: flex;
    align-items: center;
    justify-content: space-between;
}
```

---

## 🎬 Animation & Transitions

### Keyframe Animations

#### Float Animation
```css
@keyframes float {
    0%, 100% {
        transform: translateY(0) translateX(0);
    }
    25% {
        transform: translateY(-20px) translateX(10px);
    }
    50% {
        transform: translateY(-10px) translateX(-10px);
    }
    75% {
        transform: translateY(-30px) translateX(5px);
    }
}
```

#### Fade In Up
```css
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
```

#### Fade In
```css
@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}
```

#### Scroll Animation
```css
@keyframes scroll {
    0%, 100% {
        transform: translateX(-50%) translateY(0);
        opacity: 1;
    }
    100% {
        transform: translateX(-50%) translateY(12px);
        opacity: 0;
    }
}
```

#### Bounce Animation
```css
@keyframes bounce {
    0%, 100% {
        transform: translateX(-50%) translateY(0);
    }
    50% {
        transform: translateX(-50%) translateY(-10px);
    }
}
```

### Transition Speeds

| Variable | Duration | Usage |
|----------|----------|-------|
| `--transition-fast` | 0.2s | Hover effects, quick interactions |
| `--transition-base` | 0.3s | Default transitions |
| `--transition-slow` | 0.5s | Smooth, deliberate animations |

### Common Transition Patterns

```css
/* Hover Lift */
transition: transform 0.3s ease, box-shadow 0.3s ease;
transform: translateY(-8px);

/* Scale on Hover */
transition: transform 0.2s ease;
transform: scale(1.05);

/* Fade In/Out */
transition: opacity 0.3s ease;
opacity: 0; /* or 1 */

/* Background Color Change */
transition: background-color 0.3s ease;

/* Multiple Properties */
transition: all 0.3s ease;
```

---

## 📱 Responsive Design

### Breakpoints

| Breakpoint | Width | Usage |
|------------|-------|-------|
| Desktop | > 1024px | Full layout |
| Tablet | 768px - 1024px | 2-column layouts |
| Mobile | < 768px | Single column |
| Small Mobile | < 480px | Smallest screens |

### Media Query Examples

#### Tablet (768px)
```css
@media (max-width: 768px) {
    .nav-menu {
        position: fixed;
        top: 60px;
        left: 0;
        right: 0;
        background: rgba(0, 0, 0, 0.98);
        flex-direction: column;
        transform: translateX(-100%);
    }
    
    .features-grid,
    .templates-grid {
        grid-template-columns: 1fr;
    }
    
    .hero-cta {
        flex-direction: column;
        align-items: stretch;
    }
}
```

#### Mobile (480px)
```css
@media (max-width: 480px) {
    .hero-stats {
        flex-direction: column;
        gap: var(--spacing-md);
    }
    
    .stats-grid {
        grid-template-columns: 1fr;
    }
    
    /* Minimize cards on mobile */
    .feature-card,
    .template-card {
        padding: var(--spacing-md);
    }
    
    .feature-icon {
        width: 48px;
        height: 48px;
    }
    
    .feature-title,
    .template-title {
        font-size: var(--font-size-lg);
    }
}
```

---

## 💡 Usage Examples

### Example 1: Creating a New Section

```html
<section class="my-section">
    <div class="container">
        <div class="section-header">
            <span class="section-badge">New Feature</span>
            <h2 class="section-title">Amazing New Feature</h2>
            <p class="section-description">Description of the feature</p>
        </div>
        
        <div class="features-grid">
            <!-- Feature cards here -->
        </div>
    </div>
</section>
```

```css
.my-section {
    padding: var(--spacing-2xl) 0;
    background: var(--bg-secondary);
}

.section-header {
    text-align: center;
    margin-bottom: var(--spacing-2xl);
}

.section-title {
    font-size: var(--font-size-3xl);
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: var(--spacing-md);
}
```

### Example 2: Custom Card Component

```html
<div class="custom-card">
    <div class="card-icon">🚀</div>
    <h3 class="card-title">Title</h3>
    <p class="card-description">Description</p>
    <button class="btn-primary">Action</button>
</div>
```

```css
.custom-card {
    background: var(--bg-card);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: var(--radius-lg);
    padding: var(--spacing-xl);
    transition: var(--transition-base);
}

.custom-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
    border-color: var(--mclaren-orange);
}

.card-icon {
    font-size: var(--font-size-4xl);
    margin-bottom: var(--spacing-md);
}

.card-title {
    font-size: var(--font-size-xl);
    font-weight: 700;
    margin-bottom: var(--spacing-sm);
    color: var(--text-primary);
}

.card-description {
    color: var(--text-secondary);
    line-height: 1.6;
}
```

### Example 3: Gradient Text Effect

```html
<h1 class="gradient-text">Amazing Title</h1>
```

```css
.gradient-text {
    color: var(--mclaren-orange);
    /* For multi-color gradients (if needed later): */
    /* background: linear-gradient(45deg, var(--meta-blue), var(--mclaren-orange));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text; */
}
```

---

## 🎯 Best Practices

### 1. Use CSS Variables
Always use CSS variables instead of hard-coded values:
```css
/* Good ✅ */
padding: var(--spacing-md);
color: var(--text-secondary);

/* Bad ❌ */
padding: 24px;
color: #b3b3b3;
```

### 2. Consistent Spacing
Use the spacing scale for all margins and paddings:
```css
/* Good ✅ */
margin-bottom: var(--spacing-lg);
gap: var(--spacing-sm);

/* Bad ❌ */
margin-bottom: 35px;
gap: 13px;
```

### 3. Transitions on Interactive Elements
Always add smooth transitions to interactive elements:
```css
.button {
    transition: var(--transition-base);
}

.button:hover {
    transform: translateY(-2px);
}
```

### 4. Mobile-First Approach
Write base styles for mobile, then add desktop styles:
```css
/* Mobile first (default) */
.grid {
    grid-template-columns: 1fr;
}

/* Desktop */
@media (min-width: 768px) {
    .grid {
        grid-template-columns: repeat(3, 1fr);
    }
}
```

### 5. Glassmorphism Effect
For modern frosted glass effect:
```css
.glass-card {
    background: rgba(18, 18, 18, 0.8);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
}
```

---

## 🔧 Customization Guide

### Changing Primary Color

To change the primary brand color from McLaren Orange to another color:

1. Update the color variable:
```css
:root {
    --mclaren-orange: #YOUR_COLOR_HERE;
    --color-primary: var(--mclaren-orange);
}
```

2. All components using `var(--mclaren-orange)` will automatically update.

### Adding New Color

```css
:root {
    --your-new-color: #123456;
}

/* Usage */
.my-element {
    background: var(--your-new-color);
}
```

### Creating Custom Spacing

```css
:root {
    --spacing-custom: 2.5rem; /* 40px */
}
```

### Adding New Font Size

```css
:root {
    --font-size-custom: 1.75rem; /* 28px */
}
```

---

## 📦 Component Class Reference

### Navigation
- `.navbar` - Fixed navigation bar
- `.nav-container` - Navigation container
- `.nav-logo` - Logo component
- `.nav-menu` - Menu links container
- `.nav-link` - Navigation link
- `.nav-actions` - Action buttons container
- `.mobile-menu-toggle` - Mobile hamburger menu

### Buttons
- `.btn` - Base button
- `.btn-primary` - Primary CTA button (orange)
- `.btn-secondary` - Secondary button (transparent)
- `.btn-outline` - Outlined button
- `.btn-large` - Large size button

### Cards
- `.feature-card` - Feature showcase card
- `.template-card` - Template preview card
- `.stat-card` - Statistics card

### Layout
- `.container` - Content container (max-width: 1200px)
- `.hero` - Hero section
- `.features` - Features section
- `.templates` - Templates section
- `.stats` - Statistics section
- `.footer` - Footer section

### Utilities
- `.gradient-text` - Orange colored text
- `.gradient-orb` - Floating background orbs
- `.grid-overlay` - Grid pattern overlay
- `.scroll-indicator` - Scroll down indicator

---

## 🎨 Color Usage Guidelines

### When to Use Each Color

**McLaren Orange (`#FF8000`)** - PRIMARY
- Primary buttons and CTAs
- Active states
- Important highlights
- Statistics numbers
- Links and emphasis

**Meta Blue (`#1877F2`)** - SECONDARY
- Secondary accents
- Feature icons (alternate)
- Hover states for certain cards
- Social media links

**Terminal Green (`#00FF00`)** - SUCCESS
- Success messages
- Code syntax highlighting
- Active/online indicators
- Growth metrics

**Ferrari Red (`#FF2800`)** - ALERT
- Error messages
- Warnings
- Critical notifications
- Urgent actions

---

## 📊 Summary

This template provides:
- ✅ Complete CSS variable system
- ✅ 4-color brand palette
- ✅ Spacing scale (8px base)
- ✅ Typography system (9 sizes)
- ✅ Pre-built components
- ✅ Responsive breakpoints
- ✅ Animation system
- ✅ Best practices guide

**Total Variables:** 60+  
**Components:** 20+  
**Animations:** 5+  
**Breakpoints:** 3

---

## 🚀 Quick Start

1. Include `main.css` in your HTML:
```html
<link rel="stylesheet" href="/static/main.css">
```

2. Use the Inter font:
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
```

3. Start building with components:
```html
<button class="btn-primary">Click Me</button>
<div class="feature-card">Content</div>
```

---

**Made with 🧡 by the Rover Team**

For questions or contributions, visit: [GitHub Repository](https://github.com/purple-claw/Rover)
