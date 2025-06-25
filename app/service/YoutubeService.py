from googleapiclient.discovery import build
import os


def getYoutubeKey():
    return os.getenv("YOUTUBE_API_KEY");


def getYoutubeReview(productName):
    apikey = getYoutubeKey()
    if apikey is not None:
        youtube = build("youtube", "v3", developerKey=apikey)

        request = youtube.search().list(
            q=productName + " best review",
            part="snippet",
            maxResults=20,
            type="video",
            order="relevance",
            relevanceLanguage="en"
        )
        response = request.execute()

        reviews = []
        for item in response["items"]:
            video_id = item["id"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"

            video_details = youtube.videos().list(
                part="snippet,statistics",
                id=video_id
            ).execute()

            details = video_details["items"][0]
            snippet = details["snippet"]
            stats = details["statistics"]
            engagement = "view - " + stats.get("viewCount", "0")
            engagement = engagement + "|Likes - " + stats.get("likeCount", "0")
            engagement = engagement + "|Comments - " + stats.get("commentCount", "0")
            review = {
                "platform": "YouTube",
                "link": video_url,
                "author": snippet.get("channelTitle"),
                "caption": snippet.get("title"),
                "engagement": engagement
            }
            reviews.append(review)

        return reviews
    return None
