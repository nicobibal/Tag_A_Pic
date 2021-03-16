from datetime import datetime
from itertools import takewhile, dropwhile
import glob
import os
from django.db import models
import instaloader



class Image(models.Model):
    chemin = models.CharField(max_length=100, default='');

    def downloadImageFromUsername( username):
        L = instaloader.Instaloader()
        i = 0
        L.download_comments = False
        L.save_metadata = False
        L.download_geotags = False
        L.download_videos = False
        L.download_video_thumbnails = False
        L.resume_prefix = False
        L.compress_json = False
        L.post_metadata_txt_pattern = ""
        profile = instaloader.Profile.from_username(L.context, username)
        for post in profile.get_posts():
            L.dirname_pattern = "appli/static/ImagesInsta/" + post.owner_username + "/"
            L.filename_pattern = post.owner_username + "_" + str(i)
            L.download_post(post, target=profile.username)
            i += 1

        path_to_target = 'appli/static/ImagesInsta/' + username + '/'

        path_to_file_list = glob.glob(path_to_target + '*jpg')

        for path_to_file in path_to_file_list:
            cheminImage = "ImagesInsta/" + username + "/" + os.path.basename(path_to_file)
            image = Image(
                chemin= cheminImage)
            image.save()


    def downloadPictureInSpecificPeriod(self):
        L = instaloader.Instaloader()

        posts = instaloader.Profile.from_username(L.context, "instagram").get_posts()

        SINCE = datetime(2015, 5, 1)
        UNTIL = datetime(2015, 3, 1)

        for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
            print(post.date)
            L.download_post(post, "instagram")