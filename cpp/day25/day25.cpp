#include <iostream>
// #include "reader.hpp"

int main()
{
    uint64_t i1(2069194), i2(16426071);
    uint64_t modv(20201227), sn(7), l1(1), v(1), v2(1);

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
        l1++;
    }
    std::cout << "Encryption Key: " << v2 << std::endl;
}
