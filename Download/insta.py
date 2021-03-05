import instaloader

def downloadPicturesFromUsername(username):
    L = instaloader.Instaloader()
    L.download_comments = False
    L.save_metadata = False
    L.download_geotags = False
    profile = instaloader.Profile.from_username(L.context, username)
    for post in profile.get_posts():
        L.download_post(post, target=profile.username)
