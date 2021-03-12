from django.db import models
import instaloader



class Image(models.Model):
    chemin = models.CharField(max_length=100, default='');

    def downloadImageFromUsername( username):
        L = instaloader.Instaloader()
        L.dirname_pattern = "ImagesInsta"
        L.download_comments = False
        L.save_metadata = False
        L.download_geotags = False
        L.download_videos = False
        profile = instaloader.Profile.from_username(L.context, username)
        for post in profile.get_posts():
            L.download_post(post, target=profile.username)
            image = Image( chemin= "ImagesInsta/" + post.date_utc)
            image.save()
