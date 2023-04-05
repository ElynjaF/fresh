inject: ~/.config/fish/functions/fish_greeting.fish
	echo fish -N -C "python $(CURDIR)/fresh" > $<
	echo make -C $(CURDIR) >> $<
	echo "exit" >> $<
	

~/.config/fish/functions/fish_greeting.fish: ~/.config/fish/functions
	mkdir -p $<
	touch $@
