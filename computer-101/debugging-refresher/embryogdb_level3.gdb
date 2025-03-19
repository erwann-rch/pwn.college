run
break *main+433
commands
    x/gx $rbp-0x18
    continue
end
continue