inject: ~/.config/fish/config.fish ~/.config/fish/backup.fish
	echo "python $(CURDIR)/fresh" >> $<
	echo make -C $(CURDIR) >> $<
	echo "exit" >> $_
	

~/.config/fish/config.fish:
	mkidr -p ~/.config/fish
	touch $@
	
~/.config/fish/backup.fish: ~/.config/fish/config.fish
	mkidr -p ~/.config/fish
	cp $< $@
