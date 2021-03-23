from datetime import datetime
import glob
import os
from itertools import islice
from math import ceil
from django.db import models
import instaloader
from instaloader import Instaloader


class Image(models.Model):
    chemin = models.CharField(max_length=100, default='');
    insta = Instaloader()
    insta.download_comments = False
    insta.save_metadata = False
    insta.download_geotags = False
    insta.download_videos = False
    insta.download_video_thumbnails = False
    insta.resume_prefix = False
    insta.compress_json = False
    insta.post_metadata_txt_pattern = ""

    def downloadImageFromUsername( username, nbPhotos, insta=insta):
        i = 0
        profile = instaloader.Profile.from_username(insta.context, username)
        print("nn" + nbPhotos)
        for post in profile.get_posts():
            if(nbPhotos != ''):
                if(i>=int(nbPhotos)):
                    break

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
        dateStart = dateStart.split("-")
        dateEnd = dateEnd.split("-")


        SINCE = datetime(int(dateStart[0]),int(dateStart[1]),int(dateStart[2]))
        UNTIL = datetime(int(dateEnd[0]),int(dateEnd[1]),int(dateEnd[2]))
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

    def downloadPictureMostLiked(username, pourcentage, instas=insta):
        profile = instaloader.Profile.from_username(instas.context, username)
        X_percentage = int(pourcentage)
        i = 0
        posts_sorted_by_likes = sorted(profile.get_posts(),
                                       key=lambda p: p.likes + p.comments,
                                       reverse=True)

        for post in islice(posts_sorted_by_likes, ceil(profile.mediacount * X_percentage / 100)):
            instas.dirname_pattern = "appli/static/ImagesInsta/" + post.owner_username + "/"
            instas.filename_pattern = post.owner_username + "_" + str(i)
            instas.download_post(post,profile.username)
            i += 1

        path_to_target = 'appli/static/ImagesInsta/' + username + '/'
        path_to_file_list = glob.glob(path_to_target + '*jpg')

        for path_to_file in path_to_file_list:
            cheminImage = "ImagesInsta/" + username + "/" + os.path.basename(path_to_file)
            image = Image(
                chemin=cheminImage)
            image.save()