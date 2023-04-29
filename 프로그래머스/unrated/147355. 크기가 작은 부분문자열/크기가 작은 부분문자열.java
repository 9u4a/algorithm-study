class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        Long pvalue = Long.parseLong(p);
        
        for(int i = 0; i <=t.length() - p.length(); i++){
            Long tnum = Long.parseLong(t.substring(i, i + p.length()));
            if(tnum <= pvalue)
                answer += 1;
        }
        return answer;
    }
}