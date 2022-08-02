import requests

refined = open("./_chat.txt", "r")

# Authenticate with Spotify to get token
# https://accounts.spotify.com/en/authorize?client_id=b2b30cb199c142eb8125ef651ee47c05&response_type=token&redirect_uri=https:%2F%2Flocalhost:5000&scope=playlist-modify-public

playlistID = "0OvfqzHA03TVmGvVgJwSmc"
spotifyLink = "https://open.spotify.com/track/"
token = "BQBCl3_6asqza42qhZGuKmkdNIGJYlBzTHaF3CelK76JjeVSZyrUKFcwj6eW5yNg7FlJKNdALVFM5SoQhhEDIClKnAbIwgCV5i6ZU0rHiwN96rSlm5eh6_N4ckhZSKzzvRqqsCdn4Pot-s5PcLmr8514HDsseYXpBstT_NziK6ef_EeFSJ_PtpZx3uQWHO4_LJF16PLqWqmDpXo"

for line in refined:
  if spotifyLink in line:
    parts = line.split(spotifyLink)
    trackID = parts[1].split('?')[0]
    spotifyUri = 'spotify:track:' + trackID
    url = 'https://api.spotify.com/v1/playlists/' + playlistID + '/tracks?uris=' + spotifyUri
    print("Adding to playlist" + url)
    r = requests.post(url, headers={"Authorization": "Bearer " + token})
    print("Response " + r.text)