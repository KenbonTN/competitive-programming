class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loser_count = defaultdict(int)
        winner =[]
        losers = []
        for match in matches:
            loser_count[match[1]] += 1
        
        for match in matches:
            if match[0] not in loser_count:
                winner.append(match[0])
        
        for loser in loser_count.keys():
            if loser_count[loser] == 1:
                losers.append(loser)
        winner = set(winner)
        return [sorted(list(winner)),sorted(losers)]

            
        