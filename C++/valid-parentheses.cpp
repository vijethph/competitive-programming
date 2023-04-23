class Solution {
public:
    bool isValid(string s) {
        map<char,char> brackts={ 
            {'}','{'},{']','['},{')','('}
        };
        stack<char> braces;
        for(int i=0;i<s.size();i++){
            if(s[i]=='(' || s[i]=='[' || s[i]=='{')
                braces.push(s[i]);
            else if(s[i]=='}' ||s[i]==']' ||s[i]==')'){
                if(braces.empty() || (braces.top()!=brackts[s[i]]))
                    return false;
                else
                    braces.pop();
            }
            else
                return false;
        }
        if(braces.empty())
            return true;
        return false;
    }
};