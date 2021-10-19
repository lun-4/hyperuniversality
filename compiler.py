import sys
import base64


def encode_elf(path):
    with open(path, "rb") as fd:
        elfdata = fd.read()
        return base64.b64encode(elfdata).decode()


def main():
    with open("./loader.py", "r") as fd:
        loader = fd.read()

    x86_64_elf_encoded = encode_elf(sys.argv[1])
    arm_elf_encoded = encode_elf(sys.argv[2])
    aarch64_elf_encoded = encode_elf(sys.argv[3])

    loader = loader.replace("{{ X86_64_ELF }}", x86_64_elf_encoded)
    loader = loader.replace("{{ ARM_ELF }}", arm_elf_encoded)
    loader = loader.replace("{{ AARCH64_ELF }}", aarch64_elf_encoded)
    with open("./a.py", "w") as out:
        out.write(loader)


if __name__ == "__main__":
    main()
