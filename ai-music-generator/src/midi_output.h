#pragma once
#include <vector>
#include <cstdint>

class MidiOutput {
public:
    void playNotes(const std::vector<uint8_t>& notes);
};