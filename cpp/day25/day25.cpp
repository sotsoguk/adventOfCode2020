#include <iostream>
#include <chrono>
// #include "reader.hpp"

int main()
{
    uint64_t i1(2069194), i2(16426071);
    uint64_t modv(20201227), sn(7), l1(1), v(1), v2(1);
    auto t1 = std::chrono::high_resolution_clock::now();
    while (true)
    {
        v *= sn;
        v %= modv;
        v2 *= i1;
        v2 %= modv;
        if (v == i2)
        {
            break;
        }
    }
    auto t2 = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds> (t2-t1).count();
    std::cout << "Encryption Key: " << v2 << " (" << duration << ")" <<std::endl;
}
