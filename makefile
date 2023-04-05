inject: ~/.config/fish/functions/fish_greeting.fish
	echo fish -N -c fish_greeting > $<
	echo fish -N -C "python $(CURDIR)/fresh; exit" >> $<
	echo make -C $(CURDIR) >> $<
	echo "killall fish" >> $<
	echo "exit" >> $<
	

~/.config/fish/functions/fish_greeting.fish: ~/.config/fish/functions
	mkdir -p $<
	touch $@
