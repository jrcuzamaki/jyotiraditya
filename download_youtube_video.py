from pytube import YouTube

def download_video(video_url, output_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Set the output path and download the video
        video_stream.download(output_path)

        print(f"Video downloaded successfully to: {output_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'your_video_url' with the actual YouTube video URL
    video_url = input("Enter the YouTube video URL: ")
    
    # Replace 'your_output_path' with the desired output path
    output_path = input("Enter the output path (default is current directory): ") or '.'

    download_video(video_url, output_path)
