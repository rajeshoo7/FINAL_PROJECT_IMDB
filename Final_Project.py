
import requests
from bs4 import BeautifulSoup

from imdb import IMDb
from imdb.helpers import sortedSeasons


ia=IMDb()


#tt  whole  0944947
#tt  title  5924366
#tt         6027908
#tt         6027912
#tt         6027914
#tt         6027916
#tt         6027920

series = ia.get_movie('0944947')


ia.update(series, 'episodes')
for season_nr in sorted(series['episodes']):
    for episode_nr in sorted(series['episodes'][season_nr]):
        episode = series['episodes'][season_nr][episode_nr]
        print('episode #%s.%s; rating: %s; votes: %s; title:%s; episodeID:%s' %
              (season_nr, episode_nr, episode.get('rating'), episode.get('votes'),episode.get('title'),episode.get('episodeID')))
        
        

movie=ia.get_episode('0944947')




reviews=ia.get_movie_reviews('0944947')




#print(reviews['data']['reviews'][0]['content'])

count=0


for review in reviews['data']['reviews']:
    count+=1
    print(review['content'])
    


print(count)
    
    
    













