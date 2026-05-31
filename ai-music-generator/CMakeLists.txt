cmake_minimum_required(VERSION 3.10)
project(AIMusicGenerator)

set(CMAKE_CXX_STANDARD 17)

find_package(RtMidi REQUIRED)

add_executable(ai_music_generator
    src/main.cpp
    src/music_generator.cpp
    src/midi_output.cpp
)

target_link_libraries(ai_music_generator RtMidi::RtMidi)