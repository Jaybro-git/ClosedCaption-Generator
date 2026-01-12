import streamlit as st
import os
from src.model import CaptionModel

st.set_page_config(
    page_title="CCaption",
    page_icon="🎬"
)

# Caching the model
@st.cache_resource
def load_engine():
    return CaptionModel(model_size="small")

def main():
    st.markdown(
        """
            <style>
                .no-padding h3 {
                    margin: 0 !important;
                    padding: 0 !important;
                    color: #FF4B4B;
                    font-style: italic;
                    font-weight: 800;
                    font-size: 1.9rem;
                    letter-spacing: 0.3px;
                }
            </style>

            <div class="no-padding">
                <h3>ClosedCaptions</h3>
            </div>
        """,
        unsafe_allow_html=True
    )

    st.title("Convert video and audio files into SRT subtitle files with fast and reliable speech recognition.")
    st.write("")

    # Load the engine immediately
    with st.spinner("Loading AI Model..."):
        engine = load_engine()

    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi", "mp3", "wav", "m4a"])

    if uploaded_file is not None:
        os.makedirs("temp", exist_ok=True)
        temp_path = os.path.join("temp", f"temp_{uploaded_file.name}")
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Audio file or Video file preview
        file_extension = os.path.splitext(uploaded_file.name)[1].lower()

        if file_extension in [".mp4", ".mov", ".avi"]:
            st.video(uploaded_file)
        else:
            st.audio(uploaded_file)

        st.write("")

        task_choice = st.radio(
            "Choose your task:",
            ["Transcribe (Keep original language)", "Translate to English"],
            help="Translate will automatically convert any spoken language into English subtitles."
        )

        task_arg = "translate" if "Translate" in task_choice else "transcribe"

        if st.button("Generate Subtitles", type="primary"):
            with st.spinner("Transcribing audio..."):
                try:
                    # Calling the logic from the imported module
                    srt_data, text_data = engine.transcribe(temp_path, task=task_arg)
                    
                    st.divider()
                    st.success("Transcription Complete!")
                    
                    # Download Button
                    st.download_button(
                        label="Download .SRT File",
                        data=srt_data,
                        file_name=f"{uploaded_file.name.split('.')[0]}.srt",
                        mime="text/plain"
                    )

                    with st.expander("View Generated Subtitles"):
                        st.text_area("Transcription", text_data, height=300)
                    
                except Exception as e:
                    st.error(f"Error: {e}")
                finally:
                    # Cleanup
                    if os.path.exists(temp_path):
                        os.remove(temp_path)

if __name__ == "__main__":
    main()