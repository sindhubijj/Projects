import csv
import pandas as pd

#CSV File Data - Music Playlist Information 
data = [
    ["title", "artist", "genre", "mood"],
    ["Greenlight", "Pitbull, FloRida, LunchMoney Lewis", "Pop", "Upbeat"],
    ["Espresso", "Sabrina Carpenter", "Pop", "Happy"],
    ["I Can See You (Taylor's Version)", "Taylor Swift", "Pop", "Upbeat"],
    ["Too Sweet", "Hozier", "Indie", "Chill"]
]

#Write in CSV
with open('songs.csv', 'w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerows(data)

#Load the dataset
df = pd.read_csv('songs.csv')

def generate_playlist(genre, mood):
    #Filter songs based on genre and mood
    playlist = df[(df['genre'] == genre) & (df['mood'] == mood)]
    return playlist

def main(): 
    print("Welcome to the Personalized Music Playlist Generator!")

    #User Input
    genre = input("Enter your preferred genre: ")
    mood = input("Enter your preferred mood: ")

    #Generate Playlist
    playlist = generate_playlist(genre, mood)

    if not playlist.empty:
        print("\nHere is your personalized playlist: ")
        for index, row in playlist.iterrows():
            print(f"{row['title']} by {row['artist']} ({row['genre']}, {row['mood']})")
    
    else:
        print("\nNo songs found for the given genre and mood.")

if __name__ == "__main__":
    main()
