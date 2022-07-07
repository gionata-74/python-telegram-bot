class PostItem:
    def __init__(self, post_id, category, posted_date, exp_date, description=None):
        self.post_id = post_id
        self.category = category
        self.posted_date = posted_date
        self.exp_date = exp_date
        self.description = description