"""Build the English demo PDF from canonical page images."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = ROOT / "resources/images/books/ElMetodoCabelloSaludable/en/demo-pages"
BUILD = HERE / "build"
OUTPUT = ROOT / "public/The-Healthy-Hair-Method-demo.pdf"

PAGE_WIDTH = 621.12
PAGE_HEIGHT = 810
PAGE_NUMBERS = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 24, 31, 36, 51, 52, 69, 70, 77, 78, 83, 85]
PROMO_AFTER = {13, 15, 17, 19, 21}

AMAZON_URL = "https://www.amazon.com/dp/B0HJ55BM9L"
GOOGLE_URL = "https://play.google.com/store/books/details?id=Gm8KEgAAQBAJ"


def page_path(number: int) -> Path:
    return SOURCE / f"The_Healthy_Hair_Method_page_{number:03d}_en.jpg"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    names = [
        "C:/Windows/Fonts/georgiab.ttf" if bold else "C:/Windows/Fonts/georgia.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
    ]
    for name in names:
        if Path(name).exists():
            return ImageFont.truetype(name, size)
    raise FileNotFoundError("Install Georgia, Arial, or DejaVu Serif fonts.")


def centered(draw: ImageDraw.ImageDraw, y: int, text: str, selected_font: ImageFont.FreeTypeFont, fill: str) -> None:
    box = draw.textbbox((0, 0), text, font=selected_font)
    draw.text(((2588 - (box[2] - box[0])) // 2, y), text, font=selected_font, fill=fill)


def create_promo_page() -> Path:
    background = Image.open(page_path(2)).convert("RGB")
    draw = ImageDraw.Draw(background)
    green = "#315B45"
    muted = "#74685A"

    centered(draw, 160, "This is a demo", font(132, True), green)
    centered(draw, 330, "English sample from The Healthy Hair Method by Yeney López-Pérez", font(42), muted)
    centered(draw, 470, "More information is available in the complete edition", font(62, True), green)
    centered(draw, 565, "Discover a practical, conscious approach to understanding and caring for your hair.", font(37), muted)

    cover = Image.open(page_path(1)).convert("RGB")
    cover.thumbnail((930, 1215), Image.Resampling.LANCZOS)
    cover_x = (2588 - cover.width) // 2
    cover_y = 790
    draw.rounded_rectangle((cover_x - 25, cover_y - 25, cover_x + cover.width + 25, cover_y + cover.height + 25), radius=24, fill="#D9C8AB")
    background.paste(cover, (cover_x, cover_y))

    buttons = [
        (2425, "Amazon - Printed book and Kindle", "#D79A31"),
        (2705, "Google Play Books - PDF/ePub", "#177A71"),
    ]
    for y, label, color in buttons:
        draw.rounded_rectangle((300, y, 2288, y + 205), radius=42, fill=color)
        centered(draw, y + 38, label, font(55, True), "#FFFFFF")
        url = AMAZON_URL if "Amazon" in label else GOOGLE_URL
        centered(draw, y + 121, url, font(31), "#FFFFFF")

    centered(draw, 3105, "THE HEALTHY HAIR METHOD", font(34, True), green)
    centered(draw, 3160, "Yeney López-Pérez", font(30), muted)

    BUILD.mkdir(parents=True, exist_ok=True)
    promo = BUILD / "english-demo-promo.jpg"
    background.save(promo, quality=95, subsampling=0)
    return promo


def draw_page(pdf: canvas.Canvas, image_path: Path) -> None:
    pdf.drawImage(ImageReader(str(image_path)), 0, 0, width=PAGE_WIDTH, height=PAGE_HEIGHT, preserveAspectRatio=True, anchor="c")
    pdf.showPage()


def draw_promo(pdf: canvas.Canvas, promo: Path) -> None:
    pdf.drawImage(ImageReader(str(promo)), 0, 0, width=PAGE_WIDTH, height=PAGE_HEIGHT)
    pdf.linkURL(AMAZON_URL, (72, 178, 549, 227), relative=0)
    pdf.linkURL(GOOGLE_URL, (72, 111, 549, 160), relative=0)
    pdf.showPage()


def main() -> None:
    required = [page_path(number) for number in [2, *PAGE_NUMBERS]]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Missing source pages: {missing}")

    promo = create_promo_page()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(OUTPUT), pagesize=(PAGE_WIDTH, PAGE_HEIGHT), pageCompression=1)
    pdf.setTitle("The Healthy Hair Method - Demo")
    pdf.setAuthor("Yeney López-Pérez")
    pdf.setSubject("English demo with Amazon and Google Play Books links")

    draw_promo(pdf, promo)
    for index, number in enumerate(PAGE_NUMBERS, start=1):
        draw_page(pdf, page_path(number))
        if index in PROMO_AFTER or index == len(PAGE_NUMBERS):
            draw_promo(pdf, promo)
    pdf.save()
    print(f"Created {OUTPUT} with 30 pages.")


if __name__ == "__main__":
    main()

