class Solution {
    public int solution(String s) {
        int answer = 0;
        int same = 0;
        int diff = 0;
        char sFirst = s.charAt(0);
        for(int i = 0; i < s.length(); i++){
            if(same == diff){
                answer ++;
                sFirst = s.charAt(i);
            }
            if(sFirst == s.charAt(i)){
                same++;
            }
            else diff++;
        }
        return answer;
    }
}