import os
import random
from shutil import copyfile
print("---------------For Logo--------------------")
# Set the path to your video dataset
video_path = 'E:/User Sahil/Desktop/Miniproject/Raw dataset/Logo/'

# Set the proportion of data to allocate to the training set
train_ratio = 0.9

# Set the path to where you want to save the train and test splits
train_path = 'E:/User Sahil/Desktop/Miniproject/Dataset/train/Logo/'
test_path = 'E:/User Sahil/Desktop/Miniproject/Dataset/test/Logo/'

# Create the train and test directories if they don't exist
os.makedirs(train_path, exist_ok=True)
os.makedirs(test_path, exist_ok=True)

# Get a list of all the videos in the dataset directory
videos = os.listdir(video_path)

# Shuffle the videos randomly
random.shuffle(videos)

# Calculate the number of videos to allocate to the training set
num_train_videos = int(len(videos) * train_ratio)

# Loop over each video in the dataset
for i, video in enumerate(videos):
    # Determine the destination directory based on the split
    if i < num_train_videos:
        dest_dir = train_path
    else:
        dest_dir = test_path
    
    # Copy the video to the appropriate split directory
    src_file = os.path.join(video_path, video)
    dest_file = os.path.join(dest_dir, video)
    copyfile(src_file, dest_file)

    print(f"Video {video} moved to {dest_dir}")
print(" ")
print(" ")
print(" ")
print(" ")

print("---------------For Animation--------------------")
# Set the path to your video dataset
video_path = 'E:/User Sahil/Desktop/Miniproject/Raw dataset/Animation/'

# Set the proportion of data to allocate to the training set
train_ratio = 0.8

# Set the path to where you want to save the train and test splits
train_path = 'E:/User Sahil/Desktop/Miniproject/Dataset/train/Animation/'
test_path = 'E:/User Sahil/Desktop/Miniproject/Dataset/test/Animation/'

# Create the train and test directories if they don't exist
os.makedirs(train_path, exist_ok=True)
os.makedirs(test_path, exist_ok=True)

# Get a list of all the videos in the dataset directory
videos = os.listdir(video_path)

# Shuffle the videos randomly
random.shuffle(videos)

# Calculate the number of videos to allocate to the training set
num_train_videos = int(len(videos) * train_ratio)

# Loop over each video in the dataset
for i, video in enumerate(videos):
    # Determine the destination directory based on the split
    if i < num_train_videos:
        dest_dir = train_path
    else:
        dest_dir = test_path
    
    # Copy the video to the appropriate split directory
    src_file = os.path.join(video_path, video)
    dest_file = os.path.join(dest_dir, video)
    copyfile(src_file, dest_file)

    print(f"Video {video} moved to {dest_dir}")

print(" ")
print(" ")
print(" ")
print(" ")

print("---------------For IndoorLab--------------------")
# Set the path to your video dataset
video_path = 'E:/User Sahil/Desktop/Miniproject/Raw dataset/IndoorLab/'

# Set the proportion of data to allocate to the training set
train_ratio = 0.9

# Set the path to where you want to save the train and test splits
train_path = 'E:/User Sahil/Desktop/Miniproject/Dataset/train/IndoorLab/'
test_path = 'E:/User Sahil/Desktop/Miniproject/Dataset/test/IndoorLab/'

# Create the train and test directories if they don't exist
os.makedirs(train_path, exist_ok=True)
os.makedirs(test_path, exist_ok=True)

# Get a list of all the videos in the dataset directory
videos = os.listdir(video_path)

# Shuffle the videos randomly
random.shuffle(videos)

# Calculate the number of videos to allocate to the training set
num_train_videos = int(len(videos) * train_ratio)

# Loop over each video in the dataset
for i, video in enumerate(videos):
    # Determine the destination directory based on the split
    if i < num_train_videos:
        dest_dir = train_path
    else:
        dest_dir = test_path
    
    # Copy the video to the appropriate split directory
    src_file = os.path.join(video_path, video)
    dest_file = os.path.join(dest_dir, video)
    copyfile(src_file, dest_file)

    print(f"Video {video} moved to {dest_dir}")