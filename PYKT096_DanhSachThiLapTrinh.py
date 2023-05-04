class Team:
    def __init__(self, id, name, school) -> None:
        self.id = "Team{:02d}".format(id)
        self.name = name
        self.school = school

class Candidate:
    def __init__(self, id, name, teamID) -> None:
        self.id = "C{:003d}".format(id)
        self.name = name
        self.teamName, self.schoolName = self.searchInfor(teamID)

    def searchInfor(self, teamID):
        for team in teams:
            if teamID == team.id:
                return (team.name, team.school)
    
    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.teamName} {self.schoolName}"

if __name__ == "__main__":
    n = int(input())
    teams = []
    for i in range(n):
        teams.append(Team(i+1, input(), input()))
    m = int(input())
    candidates = []
    for i in range(m):
        candidates.append(Candidate(i+1, input(), input()))
    candidates.sort(key=lambda x:x.name)
    print(*candidates, sep="\n")