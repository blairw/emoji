import sys
import pandas as pd
import os

if __name__ == "__main__":
	# adapted from https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python
	script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
	script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
	rel_path = "emojilist.csv"
	abs_file_path = os.path.join(script_dir, rel_path)

	df = pd.read_csv(abs_file_path) 
	if len(sys.argv) < 2:
		print("Please specify the emoji to show!")
		print("Use --list to show possible emoji.")
	elif (sys.argv[1] == "--list"):
		print(df)
	else:
		emoji_row = df.loc[df['name'] == sys.argv[1]]
		emoji = emoji_row['emoji'].values[0]
		print(emoji)