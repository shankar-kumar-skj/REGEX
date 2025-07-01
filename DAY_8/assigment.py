# # AIzaSyBIKFD89DC0aum_8cJP0aeU18V46oxQGE0
import requests
import pandas as pd
search=input("ENTER THE CONTENT YOU WANT TO ANALYSIS : ")
# === Configuration ===
API_KEY = 'AIzaSyBIKFD89DC0aum_8cJP0aeU18V46oxQGE0'  # Replace with your actual API key
SEARCH_QUERY = search
MAX_RESULTS = 100000000  # Increase if needed

# === Step 1: YouTube search API call ===
search_url = 'https://www.googleapis.com/youtube/v3/search'
search_params = {
    'part': 'snippet',
    'q': SEARCH_QUERY,
    'type': 'video',
    'maxResults': MAX_RESULTS,
    'key': API_KEY
}

response = requests.get(search_url, params=search_params)
search_data = response.json()

# === Step 2: Extract video and channel data ===
video_data = []
video_ids = []

for item in search_data.get('items', []):
    video_id = item['id']['videoId']
    video_ids.append(video_id)
    video_data.append({
        'Video ID': video_id,
        'Title': item['snippet']['title'],
        'Channel': item['snippet']['channelTitle'],
        'Channel ID': item['snippet']['channelId'],
        'Published At': item['snippet']['publishedAt'],
        'Video URL': f"https://www.youtube.com/watch?v={video_id}"
    })

df = pd.DataFrame(video_data)

# === Step 3: Fetch statistics for videos ===
stats_url = 'https://www.googleapis.com/youtube/v3/videos'
stats_params = {
    'part': 'statistics',
    'id': ','.join(video_ids),
    'key': API_KEY
}
stats_response = requests.get(stats_url, params=stats_params).json()

# Merge likes with video data
like_map = {}
for item in stats_response.get('items', []):
    video_id = item['id']
    like_count = int(item['statistics'].get('likeCount', 0))
    like_map[video_id] = like_count

df['Likes'] = df['Video ID'].map(like_map)

# === Step 4: Group by Channel and Calculate Aggregates ===
grouped = df.groupby('Channel').agg(
    Total_Videos=('Video ID', 'count'),
    Total_Likes=('Likes', 'sum'),
    Average_Likes=('Likes', 'mean'),
    Minimum_Likes=('Likes', 'min')
).reset_index()

# === Output Results ===
print("📊 Channel-wise Like Statistics:")
print(grouped)

# Optional: Save to CSV
df.to_csv('youtube_search_results.csv', index=False)
grouped.to_csv('channel_like_summary.csv', index=False)
