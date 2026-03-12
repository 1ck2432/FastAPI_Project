from imagekitio import ImageKit
from config import settings
imagekit = ImageKit(
    private_key = settings.IMAGEKIT_PRIVATE_KEY,
)