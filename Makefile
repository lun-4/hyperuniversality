.PHONY: all

all:
	zig build-exe -target x86_64-linux main.zig --name main-x86_64.elf
	zig build-exe -target arm-linux main.zig --name main-arm.elf
	python ./compiler.py ./main-x86_64.elf ./main-arm.elf
