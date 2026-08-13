from pocket_tts import TTSModel
from playsound3 import playsound
import scipy.io.wavfile


tts_model = TTSModel.load_model()
voice_state = tts_model.get_state_for_audio_prompt(
    "alba"  # One of the pre-made voices, see above
    # You can also use any voice file you have locally or from Hugging Face:
    # "./some_audio.wav"
    # or "hf://kyutai/tts-voices/expresso/ex01-ex02_default_001_channel2_198s.wav"
)

audio = tts_model.generate_audio_stream(voice_state, "Hello how are you doing")
# Audio is a 1D torch tensor containing PCM data.
scipy.io.wavfile.write(f"output1.wav", tts_model.sample_rate, audio.numpy())


