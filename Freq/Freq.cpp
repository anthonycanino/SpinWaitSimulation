
#include <windows.h>
#include <limits.h>
#include <stdio.h>
#include <stdint.h>
#include <intrin.h>
#include <conio.h>
#include <chrono>

int main(int argc, char** argv)
{
    unsigned long long start_tsc = __rdtsc();

    Sleep(10000);

    unsigned long long end_tsc = __rdtsc();

    unsigned long long diff = end_tsc - start_tsc;

    unsigned long long freq = diff / 10;
    unsigned long long ghz = freq / 1e9;

    printf("Cycles: %llu Freq: %llu HZ Freq: %llu GZ\n", diff, freq, ghz);
    

    return 0;
}