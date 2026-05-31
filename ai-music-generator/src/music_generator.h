#pragma once
#include <vector>
#include <cstdint>

class MusicGenerator {
public:
    std::vector<uint8_t> generateMelody(int length);
private:
    uint8_t getRandomNote();
};