import numpy as np
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src import MusicGenerator

def test_generate_note_sine():
    gen = MusicGenerator(sample_rate=44100)
    audio = gen.generate_note('C4', 0.5, 'sine')
    assert len(audio) == 22050
    assert np.max(np.abs(audio)) <= 0.5

def test_generate_note_rest():
    gen = MusicGenerator()
    audio = gen.generate_note('rest', 1.0, 'sine')
    assert np.all(audio == 0.0)

def test_generate_melody():
    gen = MusicGenerator()
    notes = ['C4', 'E4', 'G4']
    durations = [0.5, 0.5, 1.0]
    audio = gen.generate_melody(notes, durations, 'sine')
    expected_length = int(44100 * (0.5 + 0.5 + 1.0))
    assert len(audio) == expected_length

def test_invalid_waveform():
    gen = MusicGenerator()
    try:
        gen.generate_note('C4', 0.5, 'triangle')
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

def test_envelope_shape():
    from src.utils import generate_envelope
    env = generate_envelope(1.0, 100)
    assert len(env) == 100
    assert env[0] == 0.0
    assert env[-1] == 0.0