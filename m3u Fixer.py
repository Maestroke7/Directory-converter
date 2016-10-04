#Information gathering
name = input("Playlist Name: ");
directory = input("Directory header to be removed: ");

#File I/O Initialization
playlist = open(name, "r+");

#Read contents of the playlist and close it
contents = playlist.readlines()
playlist.close()

#Initializing some temporary variables
contents2 = []
temp = []

#Modification to file name for new playlist
temp = name.split(".")
newname = temp[0], "new" + "."+temp[1]

#Removes contents of "directory" from every entry in playlist
for i in range(len(contents)):
    contents2.append(contents[i].split("C:\\Users\\PhanTom\\Music"))

#Clears contents for reuse
contents = []

#Adds the .. AKA one directory above prefix to every entry in playlist
#Can be replaced with . if playlists are stored in same directory as music.
for i in range(len(contents2)):
    contents2[i][0] = ".."
    contents.append("".join(contents2[i]))

#Creates new file to be written to.
playlist = open(" ".join(newname), "w");
playlist.writelines(contents)
playlist.close()
print("Job's Done!")

