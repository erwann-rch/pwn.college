#!/bin/bash
arg="$1"
name="${arg%%.*}"

as $name.s -o $name.o && ld $name.o -o $name 