# storage_estimator.py
# Estimates how much storage a collection of files needs.

PHOTO_MB = 4      # average size of one photo
SONG_MB = 5       # average size of one song
VIDEO_MB = 500    # average size of one video


def main():
    print("Storage Estimator")
    photos = int(input("How many photos? "))
    songs = int(input("How many songs? "))
    videos = int(input("How many videos? "))

    if photos < 0 or songs < 0 or videos < 0:
        print("Please enter non-negative numbers.")
        return

    total_mb = photos * PHOTO_MB + songs * SONG_MB + videos * VIDEO_MB
    total_gb = total_mb / 1024

    print("Estimated storage needed:", round(total_mb, 1), "MB")
    print("That is about", round(total_gb, 2), "GB")


main()