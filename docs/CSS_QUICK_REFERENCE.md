# 🎨 Rover CSS - Quick Reference Card

> **Handy cheat sheet for Rover landing page styles**

---

## 🎨 Colors

```css
/* Brand Colors */
--meta-blue: #1877F2;
--terminal-green: #00FF00;
--mclaren-orange: #FF8000;  /* PRIMARY */
--ferrari-red: #FF2800;

/* Backgrounds */
--bg-primary: #000000;      /* Pure black */
--bg-card: #121212;         /* Card background */

/* Text */
--text-primary: #ffffff;
--text-secondary: #b3b3b3;
--text-muted: #666666;
```

---

## 📏 Spacing (8px base)

```css
--spacing-xs: 0.5rem;    /* 8px */
--spacing-sm: 1rem;      /* 16px */
--spacing-md: 1.5rem;    /* 24px */
--spacing-lg: 2rem;      /* 32px */
--spacing-xl: 3rem;      /* 48px */
--spacing-2xl: 4rem;     /* 64px */
```

---

## 📝 Typography

```css
/* Sizes */
--font-size-xs: 0.75rem;   /* 12px */
--font-size-sm: 0.875rem;  /* 14px */
--font-size-base: 1rem;    /* 16px */
--font-size-lg: 1.125rem;  /* 18px */
--font-size-xl: 1.25rem;   /* 20px */
--font-size-2xl: 1.5rem;   /* 24px */
--font-size-3xl: 2rem;     /* 32px */
--font-size-4xl: 2.5rem;   /* 40px */
--font-size-5xl: 3rem;     /* 48px */

/* Weights */
300 - Light
400 - Regular
500 - Medium
600 - Semibold
700 - Bold
800 - Extrabold
900 - Black
```

---

## 🔘 Buttons

```html
<!-- Primary Button -->
<button class="btn-primary">Click Me</button>

<!-- Secondary Button -->
<button class="btn-secondary">Secondary</button>

<!-- Large Button -->
<button class="btn-large btn-primary">Large</button>

<!-- Outline Button -->
<button class="btn-large btn-outline">Outline</button>
```

---

## 🎴 Cards

```html
<!-- Feature Card -->
<div class="feature-card">
    <div class="feature-icon">🚀</div>
    <h3 class="feature-title">Title</h3>
    <p class="feature-description">Description</p>
</div>

<!-- Template Card -->
<div class="template-card">
    <span class="template-icon">📚</span>
    <h3 class="template-title">Title</h3>
    <p class="template-description">Description</p>
</div>
```

---

## 📐 Layout

```css
/* Container */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 var(--spacing-md);
}

/* Grid */
.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--spacing-lg);
}

/* Flex Center */
display: flex;
align-items: center;
justify-content: center;
```

---

## 🎬 Animations

```css
/* Hover Lift */
transition: var(--transition-base);
transform: translateY(-8px);

/* Scale */
transform: scale(1.05);

/* Fade In */
animation: fadeIn 0.6s ease-in-out;

/* Float */
animation: float 20s ease-in-out infinite;
```

---

## 📱 Breakpoints

```css
/* Tablet */
@media (max-width: 768px) { }

/* Mobile */
@media (max-width: 480px) { }
```

---

## 🎨 Effects

```css
/* Glassmorphism */
background: rgba(18, 18, 18, 0.8);
backdrop-filter: blur(20px);
border: 1px solid rgba(255, 255, 255, 0.1);

/* Gradient Orb */
background: radial-gradient(circle, var(--mclaren-orange) 0%, transparent 70%);
filter: blur(80px);
opacity: 0.3;

/* Box Shadow */
box-shadow: var(--shadow-lg);
```

---

## ⚡ Quick Patterns

```css
/* Hover Card */
.card {
    transition: var(--transition-base);
}
.card:hover {
    transform: translateY(-8px);
    box-shadow: var(--shadow-lg);
}

/* Active Link */
.nav-link.active {
    color: var(--mclaren-orange);
}

/* Badge */
.badge {
    background: rgba(255, 128, 0, 0.1);
    border: 1px solid rgba(255, 128, 0, 0.3);
    padding: var(--spacing-xs) var(--spacing-md);
    border-radius: var(--radius-full);
}
```

---

## 🎯 Common Classes

| Class | Purpose |
|-------|---------|
| `.container` | Max-width container |
| `.gradient-text` | Orange text |
| `.btn-primary` | Orange button |
| `.feature-card` | Feature showcase |
| `.hero` | Hero section |
| `.navbar` | Navigation bar |

---

**Print this for quick reference! 📋**
