#include <iostream>

#define I 2 % 2
#define J 0 % 2
#define K 0 % 2
#define M 8 % 2

using namespace std;

bool accept(int state, string input)
{
    if (input.size() == 0)
        if (state == 2 - M || state == 2 - J)
            return true;
        else
            return false;

    switch (state)
    {
    case 1:
        if (input[0] == '0')
            return accept(3, input.substr(1));
        else
            return accept(2 - K, input.substr(1));
    case 2:
        if (input[0] == '0')
            return accept(1, input.substr(1));
        else
            return accept(I + 1, input.substr(1));
    case 3:
        if (input[0] == '0')
            return accept(4, input.substr(1));
        else
            return accept(3 - M, input.substr(1));
    case 4:
        if (input[0] == '0')
            return accept(J + 2, input.substr(1));
        else
            return accept(2, input.substr(1));
    }

    return false;
}

void print_accepted(int max_len = 5)
{
    auto execute = [](auto &&execute, string str, int n)
    {
        if (n == 0)
        {
            if (accept(1, str))
                cout << str << endl;

            return;
        }

        execute(execute, str + "0", n - 1);
        execute(execute, str + "1", n - 1);
    };

    for (int i = 1; i <= max_len; i++)
        execute(execute, "", i);
}

int main()
{
    print_accepted();
}