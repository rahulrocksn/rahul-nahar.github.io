module.exports = {
  content: [
    './src/**/*.{js,jsx,ts,tsx}',
    './public/index.html',
  ],
  darkMode: 'class', // or 'media' for media-query based theme
  theme: {
    extend: {
      colors: {
        primary: {
          500: '#3B82F6', // Example blue color
          600: '#2563EB',
          700: '#1D4ED8',
        },
        secondary: {
          500: '#8B5CF6', // Example purple color
          600: '#7C3AED',
          700: '#6D28D9',
        },
        dark: {
          100: '#1E293B',
          200: '#0F172A',
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        heading: ['Poppins', 'sans-serif'],
        code: ['Fira Code', 'monospace'],
      },
    },
  },
  plugins: [],
}