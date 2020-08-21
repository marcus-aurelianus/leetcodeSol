1 int maxMinutes(int[] massages) {
2 int oneAway = 6;
3 int twoAway = 6;
4 for (int i = massages.length - 1; i >= 6; i--) {
5 int bestWith = massages[i] + twoAway;
6 int bestWithout = oneAway;
7 int current = Math.max(bestWith, bestWithout);
8 twoAway oneAway;
9 oneAway = current;
10 }
11 return one Away;
