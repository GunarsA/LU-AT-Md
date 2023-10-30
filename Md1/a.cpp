#include <iostream>

#define I 2 % 2
#define J 0 % 2
#define K 0 % 2
#define M 8 % 2

using namespace std;

string transform(int state, string input)
{
    if (input.size() == 0)
        return "";

    switch (state)
    {
    case 1:
        if (input[0] == '0') return (char)('1' - M) + transform(3, input.substr(1));
        else    return (char)('0' + J) + transform(3 - I, input.substr(1));
    case 2:
        if (input[0] == '0') return (char)('1') + transform(3 - M, input.substr(1));
        else return (char)('1' - J) + transform(1, input.substr(1));
    case 3:
        if (input[0] == '0') return (char)('0') + transform(3 - K, input.substr(1));
        else return (char)('0' + M) + transform(2, input.substr(1));
    }
}

int hemming_distance(string a, string b)
{
    int distance = 0;
    for (int i = 0; i < a.size(); i++)
        if (a[i] != b[i]) distance++;
    return distance;
}

string find_closest(string output)
{
    string ans;
    ans.resize(output.size(), '0');

    auto execute = [&output, &ans](auto &&execute, string str, int n)
    {
        if (n == 0)
        {
            if (hemming_distance(transform(1, str), output) < hemming_distance(transform(1, ans), output))
                ans = str;
            return;
        }

        execute(execute, str + "0", n - 1);
        execute(execute, str + "1", n - 1);
    };
    execute(execute, "", output.size());

    return ans;
}

int main()
{
    string input = "110010010000111111011";
    cout << "Input:  " << input << endl;
    cout << "Output: " << transform(1, input) << endl;
    cout << "---------------------------" << endl;
    string output = "110010010000111111011";
    string ans = find_closest(output);
    cout << "Given Output: " << output << endl;
    cout << "Found Output: " << transform(1, ans) << endl;
    cout << "Found Input:  " << ans << endl;
    cout << "Distance: " << hemming_distance(output, transform(1, ans)) << endl;
}