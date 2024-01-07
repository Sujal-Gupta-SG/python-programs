# Jarvis - Your Personal AI Assistant



Jarvis is a Python-based personal AI assistant that can perform a variety of tasks, from answering questions to automating daily routines. This README file provides an overview of Jarvis and instructions on how to set it up.

## Features

- **Voice Activation**: Wake up Jarvis by saying "Wake up Jarvis."
- **Password Protection**: Secure your assistant with a password.
- **Voice Interaction**: Communicate with Jarvis using voice commands.
- **Task Scheduling**: Schedule and manage your daily tasks.
- **Internet Speed Test**: Check your internet speed.
- **Screenshot Capture**: Take screenshots.
- **Camera Capture**: Capture photos using your camera.
- **Focus Mode**: Block distracting websites.
- **Language Translation**: Translate text.
- **Media Control**: Control media playback (pause, play, mute, volume control).
- **Web Search**: Search Google, YouTube, and Wikipedia.
- **News Updates**: Get the latest news.
- **Calculator**: Perform calculations and math operations.
- **WhatsApp Integration**: Send WhatsApp messages.
- **Weather Updates**: Get current weather and temperature.
- **Alarm Clock**: Set alarms.
- **System Control**: Shutdown your system.

## Setup

Before you can use Jarvis, you need to perform the following setup steps:


### Password Setup

1. Open the `rem.txt` file and set your desired password.

### Voice Activation

1. Run Jarvis and enter the password when prompted.
2. Say "Wake up Jarvis" to activate the assistant.

### Task Scheduling

1. Use the voice command "Jarvis schedule my day" to schedule your tasks.
2. Follow the on-screen instructions to enter your tasks.

### Focus Mode

1. Use the voice command "Focus mode" to enter focus mode.
2. Choose whether to clear old tasks and enter the websites you want to block.

### Language Translation

1. Use the voice command "Translate" followed by the text you want to translate.

### Media Control

1. Use voice commands to control media playback, adjust volume, and take screenshots or photos.

### Web Search

1. Use voice commands to search Google, YouTube, or Wikipedia.

### News Updates

1. Use the voice command "News" to get the latest news updates.

### Calculator

1. Use voice commands to perform calculations and math operations.

### WhatsApp Integration

1. Use the voice command "Send a WhatsApp" to send WhatsApp messages.

### Weather Updates

1. Use voice commands to get current weather and temperature information.

### Alarm Clock

1. Set alarms using the voice command "Set an alarm."

### System Control

1. Shutdown your system using the voice command "Jarvis shutdown the system."

## Usage

- Activate Jarvis by saying "Wake up Jarvis."
- Issue voice commands to interact with Jarvis.
- Enjoy the convenience of a personal AI assistant!

## Credits

- Jarvis is developed by sujal.
- Special thanks to the open-source community for their contributions.

# Project Setup Guide

This guide will help you set up the necessary configurations and dependencies for the different functionalities of this project. Please follow the steps below:


## 1. Alarm Functionality

In the `alarm` file:

1. On line 37, you will find `os.system`. After that line, enter the path to your desired music file that you want to play as an alarm.

## 2. Bard Functionality

In the `bard` file:

1. On line 150, you will find `filename_date`. After that line, enter the folder address where Jarvis (your AI assistant) is located.

## 3. Cookies Setup

In the `cookies.json` file:

1. Open Google Chrome and download the "EditThisCookie" extension.
2. Open the Bard website in your Chrome browser.
3. Click on the EditThisCookie extension icon in the upper-right corner (next to the bookmarks).
4. Copy the code provided by the extension and paste it into the `cookies.json` file.

## 4. Focus Mode

In the `focus_mode` file:

1. On line 47, enter the website URL you want to block when activating the focus mode.
2. On line 160 , enter you file directery address in main.py

## 5. News API Integration

In the `newread` file:

1. On line 47, search for the website of the News API: [https://newsapi.org/](https://newsapi.org/).
2. Copy the API name and API key from the News API website.
3. Paste the API name and API key in the appropriate location in the `newread` file.

## 6. WhatsApp Integration

In the `whatsapp` file:

1. Enter your family members' WhatsApp mobile numbers on lines 51, 56, and 61 to enable WhatsApp integration.

## 7. Wolfram Alpha Integration

In the `calculate` file:

1. Create an account on [https://www.wolframalpha.com/](https://www.wolframalpha.com/).
2. Copy your API key from Wolfram Alpha.
3. Paste the API key on line 18 in the `calculate` file to enable calculations using Wolfram Alpha.

With these configurations in place, you should be able to use the various functionalities of this project effectively. Make sure to follow any additional instructions provided within each functionality's code to maximize their utility.
