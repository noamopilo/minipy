[![Static Badge](https://img.shields.io/badge/github-repo-blue?logo=github)](https://github.com/noamopilo/minipy)

# **Minipy**

Minipy is a CLI tool that combines small/big python tools and games in one big tool.

---

## Table of contents

- [**Minipy**](#minipy)
  - [Table of contents](#table-of-contents)
  - [Installation](#installation)
  - [File structure](#file-structure)
  - [Configuration](#configuration)
  - [Support](#support)
  - [License](#license)
  - [Status](#status)

---

## Installation

To install minipy run this command in your terminal:

```bash
pip install minipy-tools

```

---

## File structure

This is the file structure of the package:

```md
└── 📁minipy
└── 📁games
├── number_guessing.py
├── rock_paper_scissor.py
├── snake.py
├── tic_tac_toe.py
└── 📁tools
├── auto_clicker.py
├── calculator.py
├── dice.py
├── ip_locator.py
├── link_shortner.py
├── pdf_merger.py
├── QR_code_generator.py
├── random_password_generator.py
├── send_email.py
├── voice_recorder.py
├── youtube_downloader.py
├── **init**.py
└── main.py
```

---

## Configuration

For some tools/games you need some configuration. The configuration will redirect you to README for instructions. You can find those here:

> ### Link shortner

You need to have a cuttly API key to be able to shorten links.
To create one follow these steps:

1. Go to [https://cutt.ly](https://cutt.ly)
2. Create an account / login
3. In your dashboard, go to **API** and then **API key** on the left menu

![menu](https://raw.githubusercontent.com/noamopilo/minipy/main/image-1.png)

4. You can find your API key on the right side of that page
5. Copy it and Paste it in the configuration when asked

> ### Send email

You need to have a Google App-password to be able to send an email.
This is a second password to your Google account, we can use it in our app to send an mail with Gmail.
To create one follow these steps:

1. Go to your [Google account settings](https://myaccount.google.com/)
2. In the menu on the left click **Security**
3. Click on **2-step verification** and ensure it is turned **ON**, if not turn it on
4. Scroll down untill you see **App passwords** and click on it
5. Type a name for your new App password (this can be anything, like _Email sender_)
6. Click on make
7. Copy or write down the 16 chars password you see (This is important, because you can't see it again later!)
8. Enter it in the configuration when asked

> ### Weather App

You need to have a Open Weather Map API key to be able to see the weather data.
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

For support you can make an **Issue** on the Github repo, thanks for helping with my project.

---

## License

[MIT](https://choosealicense.com/licenses/mit/)

---

## Status

Ongoing: I'm still working on this project and constantly adding new tools and features...

---
