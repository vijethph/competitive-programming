class Solution {
public:
    int romanToInt(string s) {
        map<char,int> things={
            { 'I',1 },{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}
        }; 
        int sum=things[s.back()];
        for(int i=s.length()-2;i>=0;i--){
            if(things[s[i]]<things[s[i+1]])
                sum-=things[s[i]];
            else
                sum+=things[s[i]];
        }
        return sum;
    }
};