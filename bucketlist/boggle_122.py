import sys, copy
import numpy as np

# ===================== Dictionary Class Start =================================
class Dictionary(object):
  def __init__(self, letters, diclist):
    self.letters, self.diclist = letters, diclist
    self.couples, self.size, self.idx = set(), 0, 0
    self.matrix = self.make_board(letters)
    self.diags = [self.matrix[::-1,:].diagonal(i) for i in range(-3, 4)]
    self.diags.extend(self.matrix.diagonal(i) for i in range(3, -4, -1))
    self.reduce()
    self.fitwords()
    
  def __str__(self): return str(self.ws)
  def __iter__(self): return self
  def __next__(self):
    self.idx += 1
    try: return list(self.ws)[self.idx-1]
    except IndexError:
      self.idx = 0
      raise StopIteration

  def make_board(self, letters, n=4):
    return np.array([list(letters[i:i+n]) for i in range(0, len(letters), n)])

  def pairs(self, s):
    s1, s2 = s, s[::-1]
    return set([''.join(pair) for pair in zip(s[:-1], s[1:])] + [''.join(pair) for pair in zip(s2[:-1], s2[1:])])
  
  def reduce(self):
    for row in self.matrix: self.couples |= (self.pairs("".join(row)))
    for i in range(4): self.couples |= (self.pairs("".join(np.concatenate(self.matrix[:,[i]]))))
    for n in self.diags:
      if len(n) > 1: self.couples |= (self.pairs("".join(list(n))))

    board = set(self.letters)

    self.ws = set([w for w in self.diclist if set(w) < board and w[:2] in self.couples])
    self.size = len(self.ws)

  def fitwords(self):
    self.ws = [w for w in self.ws if all([w.count(l) <= self.letters.count(l) for l in w])]


# ===================== Checker Class Start =================================
class Checker(object):
  def __init__(self, board):
    self.board, self.letters, self.adj_list = board, {}, {}
    ds = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for i in range(4):
      for j in range(4):
          if board[i][j] not in self.letters: self.letters[board[i][j]] = []
          self.letters[board[i][j]].append((i, j))
          self.adj_list[(board[i][j], i, j)] = []
          for d1, d2 in ds:
            k,l = i + d1, j + d2
            if k >= 0 and k < 4 and l >= 0 and l < 4:
              self.adj_list[(board[i][j], i, j)].append((board[k][l], k, l))
  
  def dfs(self, word):
    if len(word) < 3 or word[0] not in self.letters: return False
    stack =[(word[0], word, (word[0], i, j), set([(i, j)])) for i, j in self.letters[word[0]]]
    
    while len(stack) > 0:
      sub, word, let, positions = stack.pop()
      if sub == word: return True
      next_letter = word[len(sub)]
      
      for l, i, j in self.adj_list[let]:
        if l == next_letter and (i, j) not in positions:
          p2 = copy.deepcopy(positions)
          p2.add((i, j))
          stack.append((sub+next_letter, word, (l, i, j), p2))
    
    return False
# ======================== Classes End ===================================

def p(word):
  if len(word) < 8: return {3:1,4:1,5:2,6:3,7:5}[(len(word))]
  elif len(word) >= 8: return 11
  else: return 0

def its_boggle_time_baby(b):
  board = list(zip(*[iter(b)]*4))
  g = Checker(board)
  words = [(word, p(word)) for word in d if g.dfs(word)]
  total_points = 0
  for word, points in words: total_points += points
  print("Possible points: {}".format(total_points))

def main():
  dic = [w.strip() for w in open(sys.argv[2]) if len(w) > 3 and len(w) < 15]
  boardz = [bz.strip() for bz in open(sys.argv[1]).readlines()]
  for bz in boardz:
    global d
    d = Dictionary(bz, dic)
    its_boggle_time_baby(bz)

if __name__ == '__main__':
  main()