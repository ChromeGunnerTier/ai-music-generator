#include "midi_output.h"
#include <RtMidi.h>
#include <iostream>
#include <thread>

void MidiOutput::playNotes(const std::vector<uint8_t>& notes) {
    RtMidiOut midiOut;
    try {
        midiOut.openVirtualPort("AI Music Generator");
    } catch (RtMidiError& error) {
        std::cerr << "MIDI error: " << error.getMessage() << std::endl;
        return;
    }

    std::vector<unsigned char> message;
    for (auto note : notes) {
        message = {0x90, note, 100}; // Note on
        midiOut.sendMessage(&message);
        std::this_thread::sleep_for(std::chrono::milliseconds(500));

        message = {0x80, note, 100}; // Note off
        midiOut.sendMessage(&message);
    }
}