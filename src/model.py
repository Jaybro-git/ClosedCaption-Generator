import whisper
from .utils import convert_timestamp

class CaptionModel:
    def __init__(self, model_size="small"):
        """ Initialize the Whisper model."""
        self.model = whisper.load_model(model_size)

    def transcribe(self, video_path, task="transcribe"):
        """ Takes a video path, runs Whisper, and returns the SRT content string."""
        try:
            # Run Whisper: audio extraction + transcription
            result = self.model.transcribe(video_path, task=task, fp16=False)
            
            plain_text = result["text"].strip()

            srt_content = ""
            for index, segment in enumerate(result["segments"]):
                segment_index = index + 1
                start_time = convert_timestamp(segment["start"])
                end_time = convert_timestamp(segment["end"])
                text = segment["text"].strip()
                
                # Building the SRT string block by block
                srt_content += f"{segment_index}\n"
                srt_content += f"{start_time} --> {end_time}\n"
                srt_content += f"{text}\n\n"
            
            return srt_content, plain_text
            
        except Exception as e:
            raise RuntimeError(f"Transcription failed: {str(e)}")