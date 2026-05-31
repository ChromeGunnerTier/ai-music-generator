#include "../src/music_generator.h"
#include <cassert>

void testMelodyLength() {
    MusicGenerator generator;
    auto melody = generator.generateMelody(5);
    assert(melody.size() == 5);
}

int main() {
    testMelodyLength();
    return 0;
}