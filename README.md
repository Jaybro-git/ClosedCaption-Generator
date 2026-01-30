---
title: AI Caption Generator
emoji: 🎬
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 7860
pinned: false
---

# 🎬 AI Closed Caption Generator

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![OpenAI Whisper](https://img.shields.io/badge/OpenAI%20Whisper-74aa9c?style=for-the-badge&logo=openai&logoColor=white)](https://github.com/openai/whisper)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

> **An automated tool to transcribe and translate video/audio content into `.srt` subtitles using OpenAI's Whisper model.**

## 🚀 Live Demo
Check out the running application on Hugging Face Spaces:
<br>
<a href="https://huggingface.co/spaces/Jaybro-HF/ClosedCaption-Generator">
  <img src="https://huggingface.co/datasets/huggingface/badges/raw/main/open-in-hf-spaces-lg.svg" alt="Open in Spaces">
</a>

---

## 🧐 About The Project

This application solves the problem of manual subtitling by leveraging state of the art AI. It takes raw video (`.mp4`, `.mov`) or audio (`.mp3`, `.wav`) files, extracts the speech using **FFmpeg**, and processes it through **OpenAI's Whisper** model to generate frame-perfect timestamps.

It is fully containerized with **Docker** and set up with a **CI/CD pipeline** via GitHub Actions for seamless deployment.

## 🧠 How It Works: The AI Model

This project relies on **OpenAI's Whisper**, a state-of-the-art automatic speech recognition (ASR) system. Specifically, we utilize the **`small`** model architecture, which offers the optimal balance between accuracy and computational efficiency for local deployment.

### The Architecture
Whisper is a **Transformer-based sequence-to-sequence model**. It treats audio processing as a language modeling task, trained on **680,000 hours** of multilingual and multitask supervised data collected from the web.

### The Pipeline
1.  **Preprocessing**:
    * The input video/audio is processed by **FFmpeg** to extract the audio track.
    * The audio is resampled to **16,000 Hz** (mono).
2.  **Feature Extraction**:
    * The raw audio waveform is converted into a **Log-Mel Spectrogram**, a visual representation of the audio frequencies over time.
3.  **Encoder-Decoder Processing**:
    * **The Encoder**: Reads the spectrogram and extracts high-level features (patterns in speech).
    * **The Decoder**: Predicts the next text token based on the audio features and the previous tokens. It uses an **attention mechanism** to focus on the specific part of the audio that corresponds to the word it is currently writing.
4.  **Timestamp Prediction**:
    * Unlike traditional models, Whisper is trained to predict **timestamp tokens** alongside text tokens. This allows the model to output precise start and end times for every segment of speech, which we format into the `.srt` standard.

### Why the `Small` Model?
We selected the `small` model (~244 Million parameters) for this deployment because:
* **Accuracy**: It significantly outperforms the `tiny` and `base` models, especially on low-resource languages and complex accents.
* **Efficiency**: It requires approximately **2GB of VRAM/RAM**, making it feasible to run on the **Hugging Face Free Tier** (CPU Basic) without crashing, unlike the `medium` or `large` models.

### Key Features
* **🎥 Multi-Format Support**: Handles both Video (MP4, AVI) and Audio (MP3, WAV) inputs.
* **📝 Auto-Transcription**: Generates precise text transcripts from speech.
* **🌍 AI Translation**: Automatically translates foreign languages (e.g., Sinhala, French) into English subtitles.
* **⏱️ Precision Subtitles**: Exports standard `.srt` files ready for YouTube or VLC.
* **🐳 Dockerized**: Runs consistently across any environment using Docker containers.
* **☁️ Cloud Native**: Deployed on Hugging Face Spaces with automated sync.

---

## 🛠️ Built With

* **[Python 3.9](https://www.python.org/)**: Core logic.
* **[OpenAI Whisper](https://github.com/openai/whisper)**: Automatic Speech Recognition (ASR) model.
* **[Streamlit](https://streamlit.io/)**: Interactive web frontend.
* **[FFmpeg](https://ffmpeg.org/)**: Multimedia processing engine.
* **[Docker](https://www.docker.com/)**: Containerization.
* **[GitHub Actions](https://github.com/features/actions)**: CI/CD Pipeline.

---

## 💻 Getting Started (Local)

Follow these steps to run the project locally on your machine.

### Prerequisites
* Python 3.8+ installed.
* **FFmpeg** installed and added to your system PATH.
    * *Windows*: [Download here](https://www.gyan.dev/ffmpeg/builds/)
    * *Mac*: `brew install ffmpeg`
    * *Linux*: `sudo apt install ffmpeg`

### Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/caption-generator.git](https://github.com/YOUR_USERNAME/caption-generator.git)
    cd caption-generator
    ```

2.  **Create a virtual environment (Optional but Recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the App**
    ```bash
    streamlit run app.py
    ```

---

## 🐳 Running with Docker

If you have Docker installed, you can run the app without installing Python or FFmpeg manually.

1.  **Build the Image**
    ```bash
    docker build -t caption-generator .
    ```

2.  **Run the Container**
    ```bash
    docker run -p 7860:7860 caption-generator
    ```
    *Access the app at `http://localhost:7860`*

---

## 📂 Project Structure

```text
caption-generator/
├── .github/workflows/   # CI/CD Pipeline for Hugging Face
├── src/                 # Source Code
│   ├── model.py         # Whisper Model Logic
│   └── utils.py         # Timestamp Formatting Helpers
├── app.py               # Main Streamlit Application
├── Dockerfile           # Docker Configuration
├── requirements.txt     # Python Dependencies
└── README.md            # Documentation