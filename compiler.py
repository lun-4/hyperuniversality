import sys
import base64


def encode_elf(path):
    with open(path, "rb") as fd:
        elfdata = fd.read()
        return base64.b64encode(elfdata).decode()


def main():
    with open("./loader.py", "r") as fd:
        loader = fd.read()

    x86_64_elf_path = sys.argv[1]
    arm_elf_path = sys.argv[2]
    x86_64_elf_encoded = encode_elf(x86_64_elf_path)
    arm_elf_encoded = encode_elf(arm_elf_path)

    loader = loader.replace("{{ X86_64_ELF }}", x86_64_elf_encoded)
    loader = loader.replace("{{ ARM_ELF }}", arm_elf_encoded)
    with open("./a.py", "w") as out:
        out.write(loader)


if __name__ == "__main__":
    main()
