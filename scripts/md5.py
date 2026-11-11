"""Empreinte MD5 de fichiers (motifs * acceptés, même sous Windows)."""
import glob
import hashlib
import sys
from pathlib import Path

fichiers = sorted(f for motif in sys.argv[1:] for f in glob.glob(motif))
print("\n".join(
    f"{hashlib.md5(Path(f).read_bytes()).hexdigest()} {f}" for f in fichiers))