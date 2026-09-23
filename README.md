[![Static Badge](https://img.shields.io/badge/github-repo-blue?logo=github)](https://github.com/noamopilo/minipy)

# **Minipy**

Minipy is a CLI tool that combines Python tools and games into one program.
I created this program to become better in Python and to learn new things.
I used some blogs and YouTube videos to make the base of some tools/games, then I customized them and experimented with them.

![preview](https://raw.githubusercontent.com/noamopilo/minipy/main/preview.png)

---

## Table of contents

- [**Minipy**](#minipy)
  - [Table of contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Features](#features)
  - [| tool | weather | A weather app to get the current weather of any city in the world. | requests, pathlib, os, dotenv | yes, API key |](#-tool--weather--a-weather-app-to-get-the-current-weather-of-any-city-in-the-world--requests-pathlib-os-dotenv--yes-api-key-)
  - [File structure](#file-structure)
  - [Configuration](#configuration)
  - [Support](#support)
  - [License](#license)
  - [Status](#status)

---

## Installation

Python 3.10 or higher is required.
To install minipy run this command in your terminal:

```bash
pip install minipy-tools

```

---

## Usage

To run the program run this command on your computer:

```bash

minipy

```

You can use the **arrows** on your keyboard to navigate through the menus, and **Enter** to select an option.
Each app has a different way to use it but most of them are like all the other CLI tools.
Everything is explained in the tools/games.
Some tools/games have a GUI using Tkinter which is very intuitive to use.

---

## Features

| **tool/game** | **name** | **short description** | **tools used** | **setup?** |
|:---:|:---:|:---:|---|---|
| game | hangman | A basic hangman game. | random |  |
| game | number guessing | A simple number guessing game. | random |  |
| game | rock paper scissors | You know the game. | random |  |
| game | snake | A snake game with GUI. | random, Tkinter |  |
| game | tic tac toe | A tic tac toe game where you can choose to play against another player or a computer. (With GUI) | random, Tkinter |  |
| tool | auto clicker | An autoclicker. | time, threading, pynput |  |
| tool | calculator | A calculator with GUI. | Tkinter |  |
| tool | dice | A very simple dice rolling system. | random |  |
| tool | image editor | An image editor to apply some filters (with GUI). | Tkinter, Pillow |  |
| tool | ip locator | A tool to locate any public IP address. | requests, os, Pillow, io, Tkinter, dotenv, pathlib | yes, API key |
| tool | link shortener | A link shortener (works with Cutt.ly). | requests, os, dotenv, pathlib | yes, API key |
| tool | pdf merger | A PDF merger (To merge 2 PDFs). | PyPDF2, sys, os, shutil, pathlib |  |
| tool | QR code generator | A simple QR code generator. | qrcode, pathlib, Tkinter, Pillow |  |
| tool | random password generator | A random password generator to generate a password with some requirements and a specific length. | random, string |  |
| tool | send email | A simple program to send emails with your Gmail. | os, click, smtplib, pathlib, email.message, dotenv | yes, Google app password |
| tool | voice recorder | A voice recorder program (with GUI). | os, wave, time, threading, Tkinter, pyaudio, pathlib |  |
| tool | weather | A weather app to get the current weather of any city in the world. | requests, pathlib, os, dotenv | yes, API key |
---

## File structure

This is the file structure of the package:

```text
└── 📁minipy
    └── 📁games
        ├── hangman.py
        ├── number_guessing.py
        ├── rock_paper_scissor.py
        ├── snake.py
        ├── tic_tac_toe.py
    └── 📁tools
        ├── auto_clicker.py
        ├── calculator.py
        ├── dice.py
        ├── image_editor.py
        ├── ip_locator.py
        ├── link_shortner.py
        ├── pdf_merger.py
        ├── QR_code_generator.py
        ├── random_password_generator.py
        ├── send_email.py
        ├── voice_recorder.py
        ├── weather.py
    ├── __init__.py
    └── main.py
```

---

## Configuration

For some tools/games you need some configuration. The configuration will redirect you to README for instructions. You can find those here:

> ### Link shortener

You need to have a Cutt.ly API key to be able to shorten links.
To create one follow these steps:

1. Go to [https://cutt.ly](https://cutt.ly)
2. Create an account / login
3. In your dashboard, go to **API** and then **API key** on the left menu

![menu](https://raw.githubusercontent.com/noamopilo/minipy/main/image-1.png)

4. You can find your API key on the right side of that page
5. Copy it and paste it in the configuration when asked

> ### Send email

You need to have a Google app password to be able to send an email.
This is a second password to your Google account, we can use it in our app to send an email with Gmail.
To create one follow these steps:

1. Go to your [Google account settings](https://myaccount.google.com/)
2. In the menu on the left click **Security**
3. Click on **2-step verification** and ensure it is turned **ON**, if not turn it on
4. Scroll down until you see **App passwords** and click on it
5. Type a name for your new app password (this can be anything, like _Email sender_)
6. Click on make
7. Copy or write down the 16 chars password you see (This is important, because you can't see it again later!)
8. Enter it in the configuration when asked

> ### Weather App

You need to have an OpenWeatherMap API key to be able to see the weather data.
To find it follow these steps:

1. Go to [https://openweathermap.org/](https://openweathermap.org/)
2. Click on the **Get API key** button
3. Login or make an account
4. Go to the **API keys** section

![menu](https://raw.githubusercontent.com/noamopilo/minipy/main/image-2.png)

5. Copy the default key or create a new one
6. Enter it in the configuration when asked.

---

## Support

For support you can make an **Issue** on the GitHub repo, thanks for helping with my project.

---

## License

[MIT](https://github.com/noamopilo/minipy/blob/main/LICENSE)

---

## Status

Ongoing: I'm still working on this project and constantly adding new tools/games and features...

---