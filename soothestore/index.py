import algoliasearch_django as algoliasearch

from .models import MassageChair

from algoliasearch_django import AlgoliaIndex

class ChairIndex(AlgoliaIndex):
    fields = ('title', 'brand', 'price', 'description', 'purchased', 'rating',
              'posted', 'color_options', 'chair_features')

    settings = {
        'searchableAttributes': ['title', 'brand', 'price', 'description', 'rating', 'posted']
        }

algoliasearch.register(MassageChair, ChairIndex)