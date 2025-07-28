# 🌌 CHRONOS: UNIVERSAL DATA TERMINAL 🌌

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
</p>

## ✨ Project Overview

**CHRONOS** is a sleek, cyberpunk-themed universal data terminal built with Streamlit. It offers a suite of utility modules for data manipulation, time translation, random data generation, and simulated system monitoring, all wrapped in a custom, neon-drenched user interface. This application demonstrates advanced Streamlit customization techniques to create a unique and immersive user experience.

**🚀 Access the Live App Here:** Chronos.streamlit.app
## 🚀 Features

Chronos comes packed with several specialized modules:

1.  **Time Translator**:
    * Displays current local datetime, UNIX timestamp (Epoch), ISO 8601 format, and Julian Date.
    * "Synchronize Temporal Flux" button for interactive flair.
2.  **Text Utility**:
    * **Case Conversion**: Convert text to UPPERCASE, lowercase, Title Case, or Sentence case.
    * **Text Cleaning & Organize**: Trim whitespace, remove duplicate lines, and sort lines (Ascending/Descending).
    * **Text Metrics**: Displays word count, character count, and line count.
3.  **Data Decryptor / Encryptor**:
    * **Base64 Operations**: Convert strings to and from Base64.
4.  **Inter-Unit Converter**:
    * (Placeholder for future expansion) Designed to convert values between various units across categories like Length, Mass, Time, and Temperature.
    * Provides interactive selectors for 'From' and 'To' unit categories and specific units.
5.  **Random Data Generator**:
    * Generate various types of random data with the click of a button:
        * **Random Integer**: Within a specified range.
        * **Random Float**: Within a specified range, with adjustable decimal places.
        * **Random String (Alphanumeric)**: Of a specified length.
        * **UUID**: Generate Universally Unique Identifiers (v4).
        * **Random Hex Color**: Generate a random hexadecimal color code.
6.  **System Monitor (Simulated)**:
    * Visualizes simulated CPU Load, Memory Usage, Network Latency, and Server Temperature with dynamic progress bars and color-coded status.
    * "Run Diagnostic Scan" button with a loading spinner.
7.  **Settings**:
    * Provides toggles for display options (e.g., header glitch effect, background grid).
    * "Purge All Temporary Data Cache" button for interactive system maintenance.

## 🎨 Cyberpunk Theme & Customization

The app features a distinct cyberpunk aesthetic, achieved through:

* **Custom CSS (`style.css`)**: Extensive styling for fonts, colors, backgrounds, borders, shadows, and animations (e.g., text glow, glitch effects, scanlines, progress bars).
* **CSS Variables**: Utilizes CSS variables for a consistent and easily modifiable color palette (cyan, magenta, neon green accents on a deep blue-black background).
* **Google Fonts**: Integration of 'Oxanium' for display text and 'Roboto Mono' for monospace elements.
* **JavaScript Injection**: A robust JavaScript snippet (`streamlit.components.v1`) is injected to ensure that Streamlit's dynamically rendered elements, especially the display text within selectboxes and dropdowns, maintain the custom theme's text colors and styling. It uses a `MutationObserver` for continuous application, handling Streamlit's dynamic DOM updates.
* **Sidebar Toggle Fix**: Specific CSS rules are included to ensure the sidebar collapse/expand button is always visible, positioned correctly, and styled to match the theme, even when the sidebar is minimized.
