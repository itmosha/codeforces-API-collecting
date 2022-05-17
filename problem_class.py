class Problem:
    def __init__(self, id, title, difficulty, tags, solved_cnt = None):
        self.id = id
        self.title = title
        self.difficulty = difficulty
        self.tags = tags
        self.solved_cnt = solved_cnt

    def __str__(self):
        tags_str = ''
        for tag in self.tags:
            tags_str += tag + ' '
        tags_str.strip()

        return f'{self.id}: {self.title} - difficulty {self.difficulty}, solved {self.solved_cnt},  tags {tags_str}'

    def show(self):
        print(str(self))