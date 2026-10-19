import qrcode
import qrcode.image.svg

url = "https://project-unwind-mu.vercel.app/"

# --- PNG version ---
qr_png = qrcode.make(url)
qr_png.save("qr-code.png")

# --- SVG version (basic) ---
factory_svg = qrcode.image.svg.SvgImage
qr_svg = qrcode.make(url, image_factory=factory_svg)
qr_svg.save("qr-code.svg")

# --- SVG version (path-based, cleaner) ---
factory_path = qrcode.image.svg.SvgPathImage
qr_svg_path = qrcode.make(url, image_factory=factory_path)
qr_svg_path.save("qr-code-path.svg")

# --- SVG version (fragment, for embedding inline) ---
factory_fragment = qrcode.image.svg.SvgFragmentImage
qr_svg_fragment = qrcode.make(url, image_factory=factory_fragment)
qr_svg_fragment.save("qr-code-fragment.svg")
