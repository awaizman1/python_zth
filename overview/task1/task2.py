import subprocess
import sys


# ßThis command will run the 'dis' module on this file, it will compile this file to bytecode and disassemble it
subprocess.run([sys.executable, '-m', "dis", __file__])
