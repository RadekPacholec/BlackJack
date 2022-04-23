from exceptions import GameOverCroupierException, GameOverUserException
from game import Game

try:
	game = Game()
	game.play()
except GameOverCroupierException:
	print('Wygrał Gracz')
except GameOverUserException:
	print('Wygrał Krupier')
