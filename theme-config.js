/**
 * ROVER THEME CONFIGURATION
 * ==========================
 * 
 * This file contains all theme-related configurations and color schemes
 * for the Rover landing page. Use this as a reference for maintaining
 * consistent styling across the application.
 * 
 * Author: Rover Development Team
 * Version: 1.0.0
 * Last Updated: October 4, 2025
 */

// ============================================================================
// BRAND COLORS
// ============================================================================

const BRAND_COLORS = {
    // Primary Brand Color - Used for main CTAs, highlights, and emphasis
    primary: {
        name: 'McLaren Orange',
        hex: '#FF8000',
        rgb: 'rgb(255, 128, 0)',
        rgba: (alpha) => `rgba(255, 128, 0, ${alpha})`,
        usage: [
            'Primary buttons',
            'CTAs (Call-to-Actions)',
            'Active states',
            'Links',
            'Important highlights',
            'Statistics numbers',
            'Badges',
            'Underlines'
        ]
    },

    // Secondary Brand Colors
    secondary: {
        metaBlue: {
            name: 'Meta Blue',
            hex: '#1877F2',
            rgb: 'rgb(24, 119, 242)',
            rgba: (alpha) => `rgba(24, 119, 242, ${alpha})`,
            usage: [
                'Feature card accents',
                'Secondary highlights',
                'Hover states',
                'Social media links'
            ]
        },
        terminalGreen: {
            name: 'Terminal Green',
            hex: '#00FF00',
            rgb: 'rgb(0, 255, 0)',
            rgba: (alpha) => `rgba(0, 255, 0, ${alpha})`,
            usage: [
                'Success states',
                'Code syntax highlighting',
                'Active indicators',
                'Growth metrics'
            ]
        },
        ferrariRed: {
            name: 'Ferrari Red',
            hex: '#FF2800',
            rgb: 'rgb(255, 40, 0)',
            rgba: (alpha) => `rgba(255, 40, 0, ${alpha})`,
            usage: [
                'Error messages',
                'Warnings',
                'Critical notifications',
                'Urgent actions'
            ]
        }
    }
};

// ============================================================================
// BACKGROUND COLORS
// ============================================================================

const BACKGROUNDS = {
    primary: {
        name: 'Pure Black',
        hex: '#000000',
        rgb: 'rgb(0, 0, 0)',
        usage: 'Main body background'
    },
    secondary: {
        name: 'Dark Gray',
        hex: '#0a0a0a',
        rgb: 'rgb(10, 10, 10)',
        usage: 'Section backgrounds'
    },
    card: {
        name: 'Card Background',
        hex: '#121212',
        rgb: 'rgb(18, 18, 18)',
        usage: 'Card components, elevated surfaces'
    },
    hover: {
        name: 'Hover State',
        hex: '#1a1a1a',
        rgb: 'rgb(26, 26, 26)',
        usage: 'Hover states for interactive elements'
    }
};

// ============================================================================
// TEXT COLORS
// ============================================================================

const TEXT_COLORS = {
    primary: {
        name: 'White',
        hex: '#ffffff',
        rgb: 'rgb(255, 255, 255)',
        usage: 'Headings, primary content'
    },
    secondary: {
        name: 'Light Gray',
        hex: '#b3b3b3',
        rgb: 'rgb(179, 179, 179)',
        usage: 'Body text, descriptions'
    },
    muted: {
        name: 'Gray',
        hex: '#666666',
        rgb: 'rgb(102, 102, 102)',
        usage: 'Labels, captions, disabled states'
    }
};

// ============================================================================
// SPACING SCALE (8px base unit)
// ============================================================================

const SPACING = {
    xs: { rem: '0.5rem', px: '8px' },
    sm: { rem: '1rem', px: '16px' },
    md: { rem: '1.5rem', px: '24px' },
    lg: { rem: '2rem', px: '32px' },
    xl: { rem: '3rem', px: '48px' },
    '2xl': { rem: '4rem', px: '64px' }
};

// ============================================================================
// TYPOGRAPHY SCALE
// ============================================================================

const TYPOGRAPHY = {
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
    
    sizes: {
        xs: { rem: '0.75rem', px: '12px', usage: 'Small labels, captions' },
        sm: { rem: '0.875rem', px: '14px', usage: 'Secondary text, buttons' },
        base: { rem: '1rem', px: '16px', usage: 'Body text (default)' },
        lg: { rem: '1.125rem', px: '18px', usage: 'Large body text' },
        xl: { rem: '1.25rem', px: '20px', usage: 'Small headings' },
        '2xl': { rem: '1.5rem', px: '24px', usage: 'Section headings' },
        '3xl': { rem: '2rem', px: '32px', usage: 'Page headings' },
        '4xl': { rem: '2.5rem', px: '40px', usage: 'Hero headings' },
        '5xl': { rem: '3rem', px: '48px', usage: 'Large hero text' }
    },
    
    weights: {
        light: 300,
        regular: 400,
        medium: 500,
        semibold: 600,
        bold: 700,
        extrabold: 800,
        black: 900
    }
};

// ============================================================================
// BORDER RADIUS
// ============================================================================

const BORDER_RADIUS = {
    sm: '8px',
    md: '12px',
    lg: '16px',
    xl: '24px',
    full: '9999px'
};

// ============================================================================
// SHADOWS
// ============================================================================

const SHADOWS = {
    sm: '0 2px 8px rgba(0, 0, 0, 0.3)',
    md: '0 4px 16px rgba(0, 0, 0, 0.4)',
    lg: '0 8px 32px rgba(0, 0, 0, 0.5)',
    xl: '0 16px 48px rgba(0, 0, 0, 0.6)'
};

// ============================================================================
// TRANSITIONS
// ============================================================================

const TRANSITIONS = {
    fast: '0.2s ease',
    base: '0.3s ease',
    slow: '0.5s ease'
};

// ============================================================================
// BREAKPOINTS
// ============================================================================

const BREAKPOINTS = {
    mobile: '480px',
    tablet: '768px',
    desktop: '1024px',
    wide: '1200px'
};

// ============================================================================
// Z-INDEX SCALE
// ============================================================================

const Z_INDEX = {
    background: -1,
    base: 0,
    dropdown: 100,
    sticky: 200,
    fixed: 300,
    modal: 400,
    popover: 500,
    tooltip: 600,
    notification: 700
};

// ============================================================================
// COMPONENT SPECIFIC STYLES
// ============================================================================

const COMPONENTS = {
    navbar: {
        height: '60px',
        background: 'rgba(0, 0, 0, 0.8)',
        backdropFilter: 'blur(20px)',
        border: '1px solid rgba(255, 255, 255, 0.1)'
    },
    
    button: {
        primary: {
            background: BRAND_COLORS.primary.hex,
            color: TEXT_COLORS.primary.hex,
            padding: '0.75rem 1.5rem',
            borderRadius: BORDER_RADIUS.full,
            fontWeight: TYPOGRAPHY.weights.semibold
        },
        secondary: {
            background: 'transparent',
            color: TEXT_COLORS.primary.hex,
            border: '1px solid rgba(255, 255, 255, 0.2)',
            padding: '0.75rem 1.5rem',
            borderRadius: BORDER_RADIUS.full
        }
    },
    
    card: {
        background: BACKGROUNDS.card.hex,
        border: '1px solid rgba(255, 255, 255, 0.1)',
        borderRadius: BORDER_RADIUS.lg,
        padding: SPACING.xl.rem,
        transition: TRANSITIONS.base
    }
};

// ============================================================================
// ANIMATION KEYFRAMES
// ============================================================================

const ANIMATIONS = {
    float: {
        name: 'float',
        duration: '20s',
        timing: 'ease-in-out',
        iteration: 'infinite'
    },
    fadeIn: {
        name: 'fadeIn',
        duration: '0.6s',
        timing: 'ease-in-out'
    },
    fadeInUp: {
        name: 'fadeInUp',
        duration: '0.8s',
        timing: 'ease-out'
    },
    bounce: {
        name: 'bounce',
        duration: '2s',
        timing: 'ease-in-out',
        iteration: 'infinite'
    },
    scroll: {
        name: 'scroll',
        duration: '1.5s',
        timing: 'ease-in-out',
        iteration: 'infinite'
    }
};

// ============================================================================
// GRADIENT PATTERNS
// ============================================================================

const GRADIENTS = {
    orbs: {
        blue: `radial-gradient(circle, ${BRAND_COLORS.secondary.metaBlue.hex} 0%, transparent 70%)`,
        orange: `radial-gradient(circle, ${BRAND_COLORS.primary.hex} 0%, transparent 70%)`,
        green: `radial-gradient(circle, ${BRAND_COLORS.secondary.terminalGreen.hex} 0%, transparent 70%)`
    },
    glassmorphism: {
        background: 'rgba(18, 18, 18, 0.8)',
        backdropFilter: 'blur(20px)',
        border: '1px solid rgba(255, 255, 255, 0.1)'
    }
};

// ============================================================================
// USAGE GUIDELINES
// ============================================================================

const GUIDELINES = {
    spacing: {
        description: 'Use the 8px spacing scale for all margins and paddings',
        example: 'padding: var(--spacing-md); /* 24px */'
    },
    
    colors: {
        description: 'Always use CSS variables for colors',
        example: 'color: var(--mclaren-orange);',
        avoid: 'color: #FF8000;'
    },
    
    typography: {
        description: 'Use the defined font size scale',
        example: 'font-size: var(--font-size-xl);',
        avoid: 'font-size: 22px;'
    },
    
    transitions: {
        description: 'Add smooth transitions to interactive elements',
        example: 'transition: var(--transition-base);'
    }
};

// ============================================================================
// EXPORT CONFIGURATION
// ============================================================================

const ROVER_THEME = {
    colors: {
        brand: BRAND_COLORS,
        backgrounds: BACKGROUNDS,
        text: TEXT_COLORS
    },
    spacing: SPACING,
    typography: TYPOGRAPHY,
    borderRadius: BORDER_RADIUS,
    shadows: SHADOWS,
    transitions: TRANSITIONS,
    breakpoints: BREAKPOINTS,
    zIndex: Z_INDEX,
    components: COMPONENTS,
    animations: ANIMATIONS,
    gradients: GRADIENTS,
    guidelines: GUIDELINES
};

// For ES6 modules
// export default ROVER_THEME;

// For CommonJS
// module.exports = ROVER_THEME;

// For browser console testing
console.log('🎨 Rover Theme Configuration Loaded');
console.log('Primary Color:', BRAND_COLORS.primary.hex);
console.log('Full Config:', ROVER_THEME);
