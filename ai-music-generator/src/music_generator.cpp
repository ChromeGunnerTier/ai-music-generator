#include "music_generator.h"
#include <cstdlib>
#include <ctime>

std::vector<uint8_t> MusicGenerator::generateMelody(int length) {
    std::srand(std::time(0));
    std::vector<uint8_t> melody;

    for (int i = 0; i < length; ++i) {
        melody.push_back(getRandomNote());
    }

    return melody;
}

uint8_t MusicGenerator::getRandomNote() {
    return 60 + (std::rand() % 24); // Middle C (60) to C two octaves up
}