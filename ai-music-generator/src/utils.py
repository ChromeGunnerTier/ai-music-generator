import numpy as np

NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def note_to_frequency(note):
    if note == 'rest':
        return 0.0
    octave = int(note[-1])
    name = note[:-1]
    semitone = NOTE_NAMES.index(name)
    return 440.0 * (2 ** ((semitone - 9) / 12.0 + (octave - 4)))

def generate_envelope(duration, sample_rate, attack=0.01, decay=0.1, sustain=0.7, release=0.2):
    total_samples = int(sample_rate * duration)
    envelope = np.ones(total_samples)

    attack_samples = int(sample_rate * attack)
    decay_samples = int(sample_rate * decay)
    release_samples = int(sample_rate * release)

    if attack_samples > 0:
        envelope[:attack_samples] = np.linspace(0, 1, attack_samples)

    if decay_samples > 0:
        decay_end = attack_samples + decay_samples
        if decay_end <= total_samples:
            envelope[attack_samples:decay_end] = np.linspace(1, sustain, decay_samples)

    if release_samples > 0 and total_samples - release_samples > 0:
        envelope[-release_samples:] = np.linspace(sustain, 0, release_samples)

    return envelope