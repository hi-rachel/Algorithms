import sys

n = int(sys.stdin.readline().strip())
balls = str(sys.stdin.readline().strip())
cnt = []

rexplore = balls.rstrip("R")
cnt.append(rexplore.count("R"))

rexplore = balls.rstrip("B")
cnt.append(rexplore.count("B"))

lexplore = balls.lstrip("R")
cnt.append(lexplore.count("R"))

lexplore = balls.lstrip("B")
cnt.append(lexplore.count("B"))

print(min(cnt))