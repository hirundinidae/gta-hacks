from .models import Profile
from haystack import indexes
class ProfileIndex(indexes.Indexable, indexes.SearchIndex):
    text=indexes.CharField(document=True, use_template=True)
    def get_model(self):
        return Profile