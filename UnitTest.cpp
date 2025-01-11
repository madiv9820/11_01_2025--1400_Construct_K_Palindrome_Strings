#include <iostream>
#include <vector>
#include "Solution.hpp"

struct testcase { string s; int k; bool output; };

class UnitTest {
private:
    vector<testcase> testcases;
    Solution obj;

public:
    UnitTest() {
        testcases = {{"annabelle", 2, true}, 
                     {"leetcode", 3, false}, 
                     {"true", 4, true}};
    }
    void test() {
        for(int i = 0; i < testcases.size(); ++i) {
            bool result = obj.canConstruct(testcases[i].s, testcases[i].k);
            cout << "TestCase " <<  i+1 << ": " << ((result == testcases[i].output) ? "passed":"failed") << endl;
        }
    }
};

int main() {
    UnitTest test;
    test.test();
}