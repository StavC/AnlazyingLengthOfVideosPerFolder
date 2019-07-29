import moviepy
import matplotlib.pyplot as plt
from moviepy.editor import *
import os


def main():
    list_of_videos = []
    curr_sum_of_length = 0
    list_of_videos_length = []
    path = input("which folder do you want to analayze ?")
    paths = []
    paths_names = []
    dirs = os.scandir(path)
    print("We are going to analayze these folders: ")
    for dir in dirs:
        print(dir.name)
        paths_names.append(dir.name)
        paths.append(dir.path)

    for i in range(0, len(paths)):
        #print("Analyzing Videos...")
        #print(paths[i])
        list_of_items_to_check = os.listdir(paths[i])
        for j in range(0, len(list_of_items_to_check)):
            if list_of_items_to_check[j].endswith('.mp4'):
                list_of_videos.append(list_of_items_to_check[j])
        print(list_of_videos)
        print("Finished calculating Duration")
        for h in range(0, len(list_of_videos)):
            my_clip = VideoFileClip(paths[i] + "\\" + list_of_videos[h])
            curr_sum_of_length += my_clip.duration
            my_clip.reader.close()
            my_clip.audio.reader.close_proc()

        list_of_videos.clear()
        curr_sum_of_length = curr_sum_of_length / 60
       # print(curr_sum_of_length)
        list_of_videos_length.append(curr_sum_of_length)
        curr_sum_of_length = 0
   # print(list_of_videos_length)

    fig, ax = plt.subplots()
    plt.bar(paths_names, list_of_videos_length)

    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha="right")
    plt.gcf().subplots_adjust(bottom=0.25)
    plt.show()


if __name__ == '__main__':
    main()
