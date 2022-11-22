class Band:

    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def __str__(self):
        band_member = [musician for musician in self.musicians]
        return f"{self.name}, ({band_member})"

    def add(self, member):
        self.musicians.append(member)

    def play(self):
        musicians_play = [musician.play() for musician in self.musicians]
        return '\n'.join(musicians_play)

