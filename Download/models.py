from django.db import models
import instaloader



class Image(models.Model):
    chemin = models.CharField(max_length=100, default='');

    def downloadImageFromUsername( username):
        L = instaloader.Instaloader()
        i = 0
        L.dirname_pattern = "ImagesInsta"
        L.download_comments = False
        L.save_metadata = False
        L.download_geotags = False
        L.download_videos = False
        profile = instaloader.Profile.from_username(L.context, username)
        for post in profile.get_posts():
            L.filename_pattern = post.owner_username + "_" + str(i)
            L.download_post(post, target=profile.username)
            image = Image(  chemin= "ImageInsta/" + post.owner_username + "_" + str(i) + ".jpg" )
            image.save()
            i += 1
