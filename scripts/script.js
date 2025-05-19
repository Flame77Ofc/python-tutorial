const toggleButton = document.getElementById('toggle-theme');
let isDark = true;

function toggleTheme() {
    const root = document.documentElement;
    isDark = !isDark;

    root.style.setProperty('--bg-body', isDark ? 'var(--clr-editor-dark)' : 'var(--clr-editor-light)');
    root.style.setProperty('--bg-main', isDark ? 'var(--clr-example-bg-dark)' : 'var(--clr-example-bg-light)');
    root.style.setProperty('--text-color', isDark ? 'var(--clr-text-dark)' : 'var(--clr-text-light)');
    root.style.setProperty('--hover-color', isDark ? 'var(--clr-hover-dark)' : 'var(--clr-hover-light)');
    root.style.setProperty('--button-color', isDark ? 'var(--clr-button-dark)' : 'var(--clr-button-light)');
    root.style.setProperty('--border-color', isDark ? 'var(--clr-border-dark)' : 'var(--clr-border-light)');
    root.style.setProperty('--bg-editor', isDark ? 'var(--clr-editor-dark)' : 'var(--clr-editor-light)');
    root.style.setProperty('--bg-editor-header', isDark ? 'var(--clr-editor-header-dark)' : 'var(--clr-editor-header-light)');
    root.style.setProperty('--bg-dots', isDark ? 'var(--clr-dots-dark)' : 'var(--clr-dots-light)');
    root.style.setProperty('--bg-example', isDark ? 'var(--clr-example-bg-dark)' : 'var(--clr-example-bg-light)');
    root.style.setProperty('--bg-example-header', isDark ? 'var(--clr-example-header-dark)' : 'var(--clr-example-header-light)');
    root.style.setProperty('--text-example', isDark ? 'var(--clr-example-text-dark)' : 'var(--clr-example-text-light)');

    toggleButton.textContent = isDark ? '☀️' : '🌙';
}

toggleButton.addEventListener('click', toggleTheme);
