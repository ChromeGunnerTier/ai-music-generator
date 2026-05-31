#include "music_generator.h"
#include "midi_output.h"
#include <iostream>

int main() {
    MusicGenerator generator;
    MidiOutput midi;

    std::cout << "AI Music Generator\n";
    std::cout << "Generating 8-note melody...\n";

    auto melody = generator.generateMelody(8);
    midi.playNotes(melody);

    return 0;
}