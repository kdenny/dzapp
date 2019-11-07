from spleeter.utils.audio.adapter import get_default_audio_adapter

audio_loader = get_default_audio_adapter()
sample_rate = 44100
waveform, _ = audio_loader.load('/path/to/audio/file', sample_rate=sample_rate)

