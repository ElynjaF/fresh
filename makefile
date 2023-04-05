inject: ~/.config/fish/backup.fish
	echo "python $(CURDIR)/fresh" > ~/.config/fish/config.fish
	echo make -C $(CURDIR)
	
~/.config/fish/backup.fish:
	mv ~/.config/fish/config.fish ~/.config/fish/backup.fish
