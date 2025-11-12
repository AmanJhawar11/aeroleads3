🚀 AI Blog Generator (with Local Storage)

Welcome to the AI Blog Generator! This is a simple, single-page web application that lets you run your own personal blog right from your browser. You can write your own posts, or you can use a built-in "AI Agent" powered by the Google Gemini API to write new blog posts for you on any topic.

All blog posts are saved directly to your browser's Local Storage, so you don't need a database or any backend setup.

✨ Key Features

Create Posts: Write and save your own blog posts with a title and content.

AI Agent: Automatically generate entire blog posts by just providing a topic or prompt.

Persistent Local Storage: All posts are saved in your browser. As long as you use the same browser and don't clear your site data, your posts will be there.

Read & Delete: View all your posts in a clean list and delete old ones.

Single-Page App: Everything runs from a single index.html file. No server needed!

⚙️ Technology Stack

This project is built to be as simple as possible:

Frontend: HTML5, Tailwind CSS (for styling)

Backend (Client-side): JavaScript

Database: Browser Local Storage

AI: Google Gemini API (to generate blog posts)

Setup and Installation Guide (for Newbies)

Follow these simple steps to get the application running.

Step 1: Get Your Google AI (Gemini) API Key

This is the only thing you need. This key lets your app talk to the AI to generate posts.

Go to Google AI Studio.

Click "Create API key in new project".

A new API key will be generated. Copy this key. It will look something like AIzaSy....

Step 2: Configure the Application File

Now you just need to paste your key into the app.

Open the main file of this project (index.html) in a text editor (like VS Code, Notepad, or Sublime Text).

Scroll to the bottom, inside the <script> tag.

Find the section that looks like this:

// --- START: CONFIGURATION ---

// PASTE YOUR GEMINI API KEY HERE
const GEMINI_API_KEY = "YOUR_KEY_HERE";

// --- END: CONFIGURATION ---


Replace "YOUR_KEY_HERE" with the Gemini API key you copied in Step 1.

Save the file.

Step 3: Run the Application!

You're done! There is no server to run.
