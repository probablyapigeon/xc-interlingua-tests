from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent
packet = ROOT / "XC_ROUND4_IMPLEMENTER_PACKET.zip"
out = ROOT / "implementer_packet"
if not packet.exists():
    raise SystemExit(f"Missing packet: {packet}")
out.mkdir(exist_ok=True)
with zipfile.ZipFile(packet) as z:
    z.extractall(out)
print(f"Extracted {packet.name} -> {out}")
print("Read implementer_packet/README_IMPLEMENTER.md first.")
