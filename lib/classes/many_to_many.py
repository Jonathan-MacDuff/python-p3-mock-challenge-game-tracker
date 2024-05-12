class Game:

    all = []

    def __init__(self, title):
        self._title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0 and not hasattr(self, "_title"):
            self._title = title

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        players = []        
        for result in Result.all:
            if result.game == self:
                if not players.__contains__(result.player):
                    players.append(result.player)
        return players


    def average_score(self, player):
        scores_total = 0
        scores_count = 0
        for result in Result.all:
            if result.game == self and result.player == player:
                scores_total += result.score
                scores_count += 1
        return scores_total/scores_count

class Player:

    all = []

    def __init__(self, username):
        self._username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        games = []        
        for result in Result.all:
            if result.player == self:
                if not games.__contains__(result.game):
                    games.append(result.game)
        return games

    def played_game(self, game):
        games = self.games_played()
        return games.__contains__(game)

    def num_times_played(self, game):
        game_count = 0
        for result in Result.all:
            if result.player == self and result.game == game:
                game_count += 1
        return game_count

class Result:

    all = []

    def __init__(self, player, game, score):
        self._player = player
        self._game = game
        self._score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000 and not hasattr(self, "_score"):
            self._score = score

    @property
    def player(self):
        return self._player
    
    @property
    def game(self):
        return self._game