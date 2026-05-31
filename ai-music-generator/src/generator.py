import numpy as np
from scipy.signal import sawtooth, square
from .utils import note_to_frequency, generate_envelope

class MusicGenerator:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate

    def generate_note(self, note, duration, waveform='sine', amplitude=0.5):
        freq = note_to_frequency(note)
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)
        envelope = generate_envelope(duration, self.sample_rate)

        if waveform == 'sine':
            wave = np.sin(2 * np.pi * freq * t)
        elif waveform == 'saw':
            wave = sawtooth(2 * np.pi * freq * t)
        elif waveform == 'square':
            wave = square(2 * np.pi * freq * t)
        else:
            raise ValueError(f"Unknown waveform: {waveform}")

        return amplitude * wave * envelope

    def generate_melody(self, notes, durations, waveform='sine'):
        audio = np.array([], dtype=np.float64)
        for note, dur in zip(notes, durations):
            note_audio = self.generate_note(note, dur, waveform)
            audio = np.concatenate([audio, note_audio])
        return audio