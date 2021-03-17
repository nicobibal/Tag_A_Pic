from datetime import datetime
from itertools import takewhile, dropwhile
import glob
import os

from django.db import models
import instaloader



class Image(models.Model):
    chemin = models.CharField(max_length=100, default='');
    insta = instaloader.Instaloader()
    insta.download_comments = False
    insta.save_metadata = False
    insta.download_geotags = False
    insta.download_videos = False
    insta.download_video_thumbnails = False
    insta.resume_prefix = False
    insta.compress_json = False
    insta.post_metadata_txt_pattern = ""

    def downloadImageFromUsername( username, insta=insta):
        i = 0
        profile = instaloader.Profile.from_username(insta.context, username)

        for post in profile.get_posts():
            insta.dirname_pattern = "appli/static/ImagesInsta/" + post.owner_username + "/"
            insta.filename_pattern = post.owner_username + "_" + str(i)
            insta.download_post(post, target=profile.username)
            i += 1

        path_to_target = 'appli/static/ImagesInsta/' + username + '/'
        path_to_file_list = glob.glob(path_to_target + '*jpg')

        for path_to_file in path_to_file_list:
            cheminImage = "ImagesInsta/" + username + "/" + os.path.basename(path_to_file)
            image = Image(
                chemin= cheminImage)
            image.save()


    def downloadPictureInSpecificPeriod(dateStart, dateEnd, username, insta=insta):

        profile = instaloader.Profile.from_username(insta.context, username)


        SINCE = datetime(2020,8,1)
        UNTIL = datetime(2020,9,30)
        k = 0
        i = 0
        for post in profile.get_posts():
            postdate = post.date
            insta.dirname_pattern = "appli/static/ImagesInsta/" + post.owner_username + "/"
            insta.filename_pattern = post.owner_username + "_" + str(i)

            if postdate > UNTIL:
                continue
            elif postdate <= SINCE:
                k += 1
                if k == 50:
                    break
                else:
                    continue
            else:
                insta.download_post(post, target=profile.username)
                # if you want to tune k, uncomment below to get your k max
                # k_list.append(k)
                i +=1
                k = 0
        path_to_target = 'appli/static/ImagesInsta/' + username + '/'
        path_to_file_list = glob.glob(path_to_target + '*jpg')

        for path_to_file in path_to_file_list:
            cheminImage = "ImagesInsta/" + username + "/" + os.path.basename(path_to_file)
            image = Image(
                chemin=cheminImage)
            image.save()