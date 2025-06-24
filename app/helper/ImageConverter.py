import base64
from pathlib import Path
from app.settings import MEDIA_ROOT


def encode_image(image_path):
    image_path = Path(MEDIA_ROOT) / str(image_path)
    suffix = image_path.suffix.lower()
    mime_type = "image/jpeg" if suffix in [".jpg", ".jpeg"] else "image/png"
    with open(image_path, "rb") as f:
        base64_str = base64.b64encode(f.read()).decode("utf-8")
    return f"data:{mime_type};base64,{base64_str}"
